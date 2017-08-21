package uk.ac.ebi.eva.clinvar;

import uk.ac.ebi.eva.clinvar.model.ClinvarSet;

import javax.xml.bind.JAXBException;
import javax.xml.stream.XMLStreamException;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;
import java.util.zip.GZIPInputStream;
import java.util.zip.GZIPOutputStream;

public class App {

    private static ExecutorService executor;

    public static void main(String[] args) throws IOException, XMLStreamException, JAXBException {

        //        // TODO: CLI parser
//        int versionNumber = Integer.parseInt(args[1]);
//        String inputFileName = args[2];
        //        // TODO: output directory

        String inputFileName = "ClinVarFullRelease_2017-06.xml.gz";


        // build XML reader
        ArrayBlockingQueue<String> xmlStringsQueue = new ArrayBlockingQueue<>(1000);
        GZIPInputStream is = new GZIPInputStream(new FileInputStream(inputFileName));
        XmlClinVarReader reader = new XmlClinVarReader(is, xmlStringsQueue);

        // build transformer
        ArrayBlockingQueue<ClinvarSet> clinvarSetsQueue = new ArrayBlockingQueue<>(1000);
        ClinvarSetTransformer clinvarSetTransformer = new ClinvarSetTransformer(xmlStringsQueue, clinvarSetsQueue, "47");

        // build Json serializer
        String outputFileName = "clinvar.json.gz";
        BufferedWriter bw = new BufferedWriter(
                new OutputStreamWriter(new GZIPOutputStream(Files.newOutputStream(Paths.get(outputFileName)))));
        ClinvarJsonSerializer clinvarJsonSerializer = new ClinvarJsonSerializer(clinvarSetsQueue, bw);

        // submit each task (read, transform, serialize) in a thread
        executor = Executors.newFixedThreadPool(3);
        Future<Integer> readRecords = executor.submit(reader);
        Future<Integer> transformedRecords = executor.submit(clinvarSetTransformer);
        Future<Integer> writtenRecords = executor.submit(clinvarJsonSerializer);

        try {
            if (readRecords.get().equals(transformedRecords.get()) && readRecords.get().equals(writtenRecords.get())) {
                System.out.println(
                        "Clinvar file " + inputFileName + " transformed successfully to json file " + outputFileName);
                System.out.println(readRecords.get() + " clinvar records processed");
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (ExecutionException e) {
            e.printStackTrace();
        }

        closeExecutor();
    }

    public static void closeExecutor() {
        try {
            executor.shutdown();
            executor.awaitTermination(5, TimeUnit.SECONDS);
        }
        catch (InterruptedException e) {
            System.err.println("Executor interrupted");
        }
        finally {
            if (!executor.isTerminated()) {
                System.err.println("The executor is being closed with non-finished tasks");
            }
            executor.shutdownNow();
        }
    }
}
