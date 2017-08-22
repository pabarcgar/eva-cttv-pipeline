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
