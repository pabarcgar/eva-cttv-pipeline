package uk.ac.ebi.eva.clinvar;

import javax.xml.stream.XMLStreamException;
import java.io.InputStream;
import java.util.concurrent.ArrayBlockingQueue;

public class XmlClinVarReader implements Runnable {

    private InputStream inputStream;

    private ArrayBlockingQueue<String> queue;

    public static final String FINISHED = "";

    public XmlClinVarReader(InputStream inputStream, ArrayBlockingQueue<String> queue) {
        this.inputStream = inputStream;
        this.queue = queue;
    }

    @Override
    public void run() {
        try {
            XmlClinVarSetIterator xmlClinVarSetIterator = new XmlClinVarSetIterator(inputStream);
            String clinvarPublicSet;
            int i = 0;
            while ((clinvarPublicSet = xmlClinVarSetIterator.next()) != null) {
                queue.put(clinvarPublicSet);
                i++;
                if ((i % 1000) == 0) {
                    System.out.println(i + " records read");
                }
            }
            queue.put(FINISHED);
            System.out.println("Finished reading " + i + "records");
        } catch (XMLStreamException e) {
            // TODO treat errors
            e.printStackTrace();
        } catch (InterruptedException e) {
            // thrown by queue.put
            e.printStackTrace();
        }

    }
}
