package uk.ac.ebi.eva.clinvar;

import uk.ac.ebi.eva.clinvar.model.ClinvarSet;

import javax.xml.bind.JAXBException;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.Callable;

public class ClinvarSetTransformer implements Callable<Integer> {

    private ArrayBlockingQueue<String> inputQueue;

    private final ArrayBlockingQueue<ClinvarSet> outputQueue;

    private PublicSetParser publicSetParser;

    public static final ClinvarSet FINISHED_TRANSFORMING = new ClinvarSet(null);

    public ClinvarSetTransformer(ArrayBlockingQueue<String> inputQueue, ArrayBlockingQueue<ClinvarSet> outputQueue,
                                 int clinvarVersion) throws JAXBException {
        this.inputQueue = inputQueue;
        this.outputQueue = outputQueue;
        publicSetParser = new PublicSetParser("uk.ac.ebi.eva.clinvar.model.v" + clinvarVersion + ".jaxb");
    }

    @Override
    public Integer call() {
        Integer recordsProcessed = 0;

        try {
            String clinvarSetXmlString = inputQueue.take();
            // we are not comparing with equals because we are interested in the object reference and not in the string
            // content
            while (clinvarSetXmlString != XmlClinVarReader.FINISHED) {
                ClinvarSet clinvarSet = publicSetParser.parse(clinvarSetXmlString);
                outputQueue.put(clinvarSet);
                recordsProcessed++;

                clinvarSetXmlString = inputQueue.take();
            }
            outputQueue.put(FINISHED_TRANSFORMING);
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (JAXBException e) {
            e.printStackTrace();
        }

        return recordsProcessed;
    }
}
