package uk.ac.ebi.eva.clinvar;

import uk.ac.ebi.eva.clinvar.model.ClinvarSet;

import javax.xml.bind.JAXBException;
import java.util.concurrent.ArrayBlockingQueue;

public class ClinvarSetTransformer implements Runnable {

    private ArrayBlockingQueue<String> inputQueue;

    private final ArrayBlockingQueue<ClinvarSet> outputQueue;

    private PublicSetParser publicSetParser;

    public static final ClinvarSet FINISHED_TRANSFORMING = new ClinvarSet(null);

    public ClinvarSetTransformer(ArrayBlockingQueue<String> inputQueue, ArrayBlockingQueue<ClinvarSet> outputQueue,
                                 String clinvarVersion) throws JAXBException {
        this.inputQueue = inputQueue;
        this.outputQueue = outputQueue;
        publicSetParser = new PublicSetParser("uk.ac.ebi.eva.clinvar.model.v" + clinvarVersion + ".jaxb");
    }

    @Override
    public void run() {
        int i = 0;
        String clinvarSet = null;
        try {
            clinvarSet = inputQueue.take();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        try {
            while (clinvarSet != XmlClinVarReader.FINISHED) {
                // TODO clean this
                ClinvarSet objectToWrite = publicSetParser.parse(clinvarSet);
                outputQueue.put(objectToWrite);

                i++;
                clinvarSet = inputQueue.take();
            }
            outputQueue.put(FINISHED_TRANSFORMING);
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (JAXBException e) {
            e.printStackTrace();
        }
    }
}
