package uk.ac.ebi.eva.clinvar;

import javax.xml.stream.XMLStreamException;
import java.io.InputStream;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.Callable;

// TODO: document and license
public class XmlClinVarReader implements Callable<Integer> {

    private InputStream inputStream;

    private ArrayBlockingQueue<String> queue;

    public static final String FINISHED = "";

    public XmlClinVarReader(InputStream inputStream, ArrayBlockingQueue<String> outputQueue) {
        this.inputStream = inputStream;
        this.queue = outputQueue;
    }

    @Override
    public Integer call() {
        int processedRecords = 0;

        try {
            XmlClinVarSetIterator xmlClinVarSetIterator = new XmlClinVarSetIterator(inputStream);
            String clinvarPublicSet;
            while ((clinvarPublicSet = xmlClinVarSetIterator.next()) != null) {
                queue.put(clinvarPublicSet);
                processedRecords++;
            }
            queue.put(FINISHED);
        } catch (XMLStreamException e) {
            // TODO treat errors
            e.printStackTrace();
        } catch (InterruptedException e) {
            // thrown by queue.put
            e.printStackTrace();
        }

        return processedRecords;
    }
}
