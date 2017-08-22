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

import uk.ac.ebi.eva.clinvar.model.ClinvarSet;

import javax.xml.bind.JAXBException;
import javax.xml.stream.XMLStreamException;
import java.io.BufferedWriter;
import java.io.FileInputStream;
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

    @Parameter(names={"--inputFileName", "-i"}, required = true)
    private String inputFileName;

    @Parameter(names={"--outputDir", "-o"})
    private String outputDir = "";

    @Parameter(names={"--clinvarVersion", "-v"}, required = true)
    private int versionNumber;

    public static void main(String[] args) throws IOException, XMLStreamException, JAXBException {
        Application app = new Application();
        JCommander.newBuilder()
                  .addObject(app)
                  .build()
                  .parse(args);
        app.run();
    }

    public void run() {
        ArrayBlockingQueue<String> xmlStringsQueue = new ArrayBlockingQueue<>(1000);

        XmlClinVarReader reader = buildXmlClinVarReader(xmlStringsQueue);

        ArrayBlockingQueue<ClinvarSet> clinvarSetsQueue = new ArrayBlockingQueue<>(1000);
        ClinvarSetTransformer clinvarSetTransformer = getClinvarSetTransformer(xmlStringsQueue, clinvarSetsQueue);

        // TODO check if output directory and output file exist
        Path outputFilePath = Paths.get(outputDir + "/clinvar.json.gz");
        ClinvarJsonSerializer clinvarJsonSerializer = getClinvarJsonSerializer(clinvarSetsQueue, outputFilePath);

        if (reader != null && clinvarSetTransformer != null && clinvarJsonSerializer != null) {
            System.out.println(
                    "Transforming clinvar file " + inputFileName + " into Json file " + outputFilePath + " ...");
            multiThreadExecute(reader, clinvarSetTransformer, clinvarJsonSerializer);
        }

    }

    private void multiThreadExecute(XmlClinVarReader reader, ClinvarSetTransformer clinvarSetTransformer,
                                    ClinvarJsonSerializer clinvarJsonSerializer) {
        // submit each task (read, transform, serialize) in a thread
        ExecutorService executor = Executors.newFixedThreadPool(3);
        Future<Integer> readRecords = executor.submit(reader);
        Future<Integer> transformedRecords = executor.submit(clinvarSetTransformer);
        Future<Integer> writtenRecords = executor.submit(clinvarJsonSerializer);

        try {
            if (readRecords.get().equals(transformedRecords.get()) &&
                    readRecords.get().equals(writtenRecords.get())) {
                System.out.println("Finished successfully: " + readRecords.get() + " clinvar records processed");
            }
        } catch (InterruptedException e) {
            System.out.println("Thread interrupted: " + e.getMessage());
        } catch (ExecutionException e) {
            System.out.println("Exception in thread execution: " + e.getMessage());
        }

        closeExecutor(executor);
    }

    private ClinvarJsonSerializer getClinvarJsonSerializer(ArrayBlockingQueue<ClinvarSet> clinvarSetsQueue,
                                                           Path outputFilePath) {
        // build Json serializer
        ClinvarJsonSerializer clinvarJsonSerializer;
        try {

            BufferedWriter bw = new BufferedWriter(
                    new OutputStreamWriter(new GZIPOutputStream(Files.newOutputStream(outputFilePath))));
            clinvarJsonSerializer = new ClinvarJsonSerializer(clinvarSetsQueue, bw);
        } catch (IOException e) {
            System.out.println("Error: output file " + outputFilePath + " cannot be written: " + e.getMessage());
            return null;
        }
        return clinvarJsonSerializer;
    }

    private ClinvarSetTransformer getClinvarSetTransformer(ArrayBlockingQueue<String> xmlStringsQueue,
                                                           ArrayBlockingQueue<ClinvarSet> clinvarSetsQueue) {
        ClinvarSetTransformer clinvarSetTransformer;

        try {
            // build transformer
            clinvarSetTransformer = new ClinvarSetTransformer(xmlStringsQueue, clinvarSetsQueue,
                                                              versionNumber);
        } catch (JAXBException e) {
            System.out.println("Error: clinvar version " + versionNumber + " cannot be parsed: " + e.getMessage());
            return null;
        }
        return clinvarSetTransformer;
    }

    private XmlClinVarReader buildXmlClinVarReader(ArrayBlockingQueue<String> xmlStringsQueue) {
        XmlClinVarReader reader;
        try {
            // build XML reader
            GZIPInputStream is = new GZIPInputStream(new FileInputStream(inputFileName));
            reader = new XmlClinVarReader(is, xmlStringsQueue);
        } catch (IOException e) {
            System.out.println("Error: input file " + inputFileName + " cannot be read: " + e.getMessage());
            return null;
        }
        return reader;
    }

    public void closeExecutor(ExecutorService executor) {
        try {
            executor.shutdown();
            executor.awaitTermination(5, TimeUnit.SECONDS);
        }
        catch (InterruptedException e) {
            System.out.println("Executor interrupted");
        }
        finally {
            if (!executor.isTerminated()) {
                System.out.println("The executor is being closed with non-finished tasks");
            }
            executor.shutdownNow();
        }
    }
}
