package uk.ac.ebi.eva.clinvar;

import uk.ac.ebi.eva.clinvar.model.ClinvarSet;

import javax.xml.bind.JAXBException;
import javax.xml.stream.XMLStreamException;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.nio.file.Files;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
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


        GZIPInputStream is = new GZIPInputStream(new FileInputStream("ClinVarFullRelease_2017-06.xml.gz"));
        ArrayBlockingQueue<String> xmlStringsQueue = new ArrayBlockingQueue<>(1000);

        XmlClinVarReader reader = new XmlClinVarReader(is, xmlStringsQueue);

        ArrayBlockingQueue<ClinvarSet> clinvarSetsQueue = new ArrayBlockingQueue<>(1000);
        ClinvarSetTransformer clinvarSetTransformer = new ClinvarSetTransformer(xmlStringsQueue, clinvarSetsQueue, "47");
        BufferedWriter bw = new BufferedWriter(
                new OutputStreamWriter(new GZIPOutputStream(Files.newOutputStream("clinvar.json.gz"))));
        ClinvarSetWriter clinvarSetWriter = new ClinvarSetWriter(clinvarSetsQueue, bw);

        executor = Executors.newFixedThreadPool(3);
        executor.submit(reader);
        executor.submit(clinvarSetTransformer);
        executor.submit(clinvarSetWriter);

        // TODO: close executor
    }

    public static void closeExecutor() {
        try {
            System.out.println("attempt to shutdown executor");
            executor.shutdown();
            executor.awaitTermination(5, TimeUnit.SECONDS);
        }
        catch (InterruptedException e) {
            System.err.println("tasks interrupted");
        }
        finally {
            if (!executor.isTerminated()) {
                System.err.println("cancel non-finished tasks");
            }
            executor.shutdownNow();
            System.out.println("shutdown finished");
        }
    }
}
