/*
 *  Copyright 2017 EMBL - European Bioinformatics Institute
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *       http://www.apache.org/licenses/LICENSE-2.0
 *
 *   Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */
package uk.ac.ebi.eva.clinvar;

import com.beust.jcommander.JCommander;
import com.beust.jcommander.Parameter;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import uk.ac.ebi.eva.clinvar.model.ClinvarSet;

import javax.xml.bind.JAXBException;
import javax.xml.stream.XMLStreamException;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;
import java.util.zip.GZIPInputStream;
import java.util.zip.GZIPOutputStream;

public class Application {

    private static final Logger logger = LoggerFactory.getLogger(Application.class);

    public static final String OUTPUT_FILE_NAME = "clinvar.json.gz";

    @Parameter(names={"--inputFileName", "-i"}, required = true)
    private String inputFileName;

    @Parameter(names={"--outputDir", "-o"})
    private String outputDir = "";

    private ExecutorService executor;

    public static void main(String[] args) throws IOException, XMLStreamException, JAXBException {
        Application app = new Application();
        JCommander.newBuilder()
                  .addObject(app)
                  .build()
                  .parse(args);
        app.run();
    }

    public void run() {
        try {
            ArrayBlockingQueue<String> xmlStringsQueue = new ArrayBlockingQueue<>(1000);
            XmlClinVarReader reader = getXmlClinVarReader(xmlStringsQueue);

            ArrayBlockingQueue<ClinvarSet> clinvarSetsQueue = new ArrayBlockingQueue<>(1000);
            ClinvarSetTransformer clinvarSetTransformer = getClinvarSetTransformer(xmlStringsQueue, clinvarSetsQueue);

            Path outputFilePath = Paths.get(outputDir + "/" + OUTPUT_FILE_NAME);
            ClinvarJsonSerializer clinvarJsonSerializer = getClinvarJsonSerializer(clinvarSetsQueue, outputFilePath);

            logger.info("Transforming clinvar file {} into Json file {} ...", inputFileName, outputFilePath);
            multiThreadExecute(reader, clinvarSetTransformer, clinvarJsonSerializer);
        } catch (IOException | JAXBException e) {
            logger.error("Cannot set up clinvar parser. Stopping execution ...");
        }
    }

    private void multiThreadExecute(XmlClinVarReader reader, ClinvarSetTransformer clinvarSetTransformer,
                                    ClinvarJsonSerializer clinvarJsonSerializer) {
        // submit each task (read, transform, serialize) in a thread
        executor = Executors.newFixedThreadPool(3);
        Future<Integer> readRecords = executor.submit(reader);
        Future<Integer> transformedRecords = executor.submit(clinvarSetTransformer);
        Future<Integer> writtenRecords = executor.submit(clinvarJsonSerializer);

        try {
            if (readRecords.get().equals(transformedRecords.get()) &&
                    readRecords.get().equals(writtenRecords.get())) {
                logger.info("Finished successfully: {} clinvar records processed", readRecords.get());
            }
        } catch (InterruptedException e) {
            logger.error("Thread interrupted: '{}'", e.getMessage());
        } catch (ExecutionException e) {
            logger.error("Error in thread execution. Stopping application ...");
        }

        closeExecutor();
    }

    private ClinvarJsonSerializer getClinvarJsonSerializer(ArrayBlockingQueue<ClinvarSet> clinvarSetsQueue,
                                                           Path outputFilePath) throws IOException {
        // build Json serializer
        ClinvarJsonSerializer clinvarJsonSerializer;
        try {
            checkOutputDirectory(outputFilePath);
            BufferedWriter bw = new BufferedWriter(
                    new OutputStreamWriter(new GZIPOutputStream(Files.newOutputStream(outputFilePath))));
            clinvarJsonSerializer = new ClinvarJsonSerializer(clinvarSetsQueue, bw);
        } catch (IOException e) {
            logger.error("Output file {} cannot be written: '{}'", outputFilePath, e.getMessage());
            throw e;
        }
        return clinvarJsonSerializer;
    }

    private void checkOutputDirectory(Path outputFilePath) throws IOException {
        File outputDirectory = outputFilePath.getParent().toFile();
        if (!outputDirectory.exists()) {
            logger.info("Creating output directory {} ...", outputDirectory);
            if (!outputDirectory.mkdirs()) {
               throw new IOException("Cannot create output diretory " + outputDirectory);
            }
        }
    }

    private ClinvarSetTransformer getClinvarSetTransformer(ArrayBlockingQueue<String> xmlStringsQueue,
                                                           ArrayBlockingQueue<ClinvarSet> clinvarSetsQueue) throws
            JAXBException {
        ClinvarSetTransformer clinvarSetTransformer;

        try {
            // build transformer
            clinvarSetTransformer = new ClinvarSetTransformer(xmlStringsQueue, clinvarSetsQueue);
        } catch (JAXBException e) {
            logger.error("Cannot create JAXB XML unmarshaller: {}", e.getMessage());
            throw e;
        }
        return clinvarSetTransformer;
    }

    private XmlClinVarReader getXmlClinVarReader(
            ArrayBlockingQueue<String> xmlStringsQueue) throws IOException {
        XmlClinVarReader reader;
        try {
            // build XML reader
            GZIPInputStream is = new GZIPInputStream(new FileInputStream(inputFileName));
            reader = new XmlClinVarReader(is, xmlStringsQueue);
        } catch (FileNotFoundException e) {
            logger.error("Input file {} does not exist", inputFileName);
            throw e;
        } catch (IOException e) {
            logger.error("Input file {} cannot be read: '{}'", inputFileName, e.getMessage());
            throw e;
        }
        return reader;
    }

    public void closeExecutor() {
        try {
            executor.shutdown();
            executor.awaitTermination(5, TimeUnit.SECONDS);
        }
        catch (InterruptedException e) {
            logger.warn("Executor interrupted: {}", e.getMessage());
        }
        finally {
            if (!executor.isTerminated()) {
                logger.warn("Forcing execution shutdown ...");
            }
            executor.shutdownNow();
        }
    }

}
