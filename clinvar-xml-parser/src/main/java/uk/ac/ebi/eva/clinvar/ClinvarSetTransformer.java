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

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import uk.ac.ebi.eva.clinvar.model.ClinvarSet;

import javax.xml.bind.JAXBException;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.Callable;

/**
 * Class that takes Strings from a input queue (each string containing a "ClinVarSet" XML record), transforming each of
 * them into a {@link uk.ac.ebi.eva.clinvar.model.ClinvarSet ClinvarSet} object, and inserting them into an output
 * queue. This class extends callable so it can be run in a thread
 */
public class ClinvarSetTransformer implements Callable<Integer> {

    private static final Logger logger = LoggerFactory.getLogger(ClinvarSetTransformer.class);

    private ArrayBlockingQueue<String> inputQueue;

    private final ArrayBlockingQueue<ClinvarSet> outputQueue;

    private PublicSetParser publicSetParser;

    /** Special object that we add to the end of the queue when there are no more records to transform */
    public static final ClinvarSet FINISHED_TRANSFORMING = new ClinvarSet(null);

    public ClinvarSetTransformer(ArrayBlockingQueue<String> inputQueue, ArrayBlockingQueue<ClinvarSet> outputQueue,
                                 int clinvarVersion) throws JAXBException {
        this.inputQueue = inputQueue;
        this.outputQueue = outputQueue;
        publicSetParser = new PublicSetParser("uk.ac.ebi.eva.clinvar.model.v" + clinvarVersion + ".jaxb");
    }

    /**
     * Take strings from the input queue, transforming and inserting them into the output queue. It stops when it founds
     * in the input queue an special {@link uk.ac.ebi.eva.clinvar.XmlClinVarReader#FINISHED String}, adding a
     * {@link uk.ac.ebi.eva.clinvar.ClinvarSetTransformer#FINISHED_TRANSFORMING object} to the output queue
     * @return Number of serialized records
     */
    @Override
    public Integer call() throws JAXBException, InterruptedException {
        Integer recordsProcessed = 0;

        try {
            String clinvarSetXmlString = inputQueue.take();
            // we are not comparing with equals because we are interested in the object reference and not in the String
            // content
            while (clinvarSetXmlString != XmlClinVarReader.FINISHED) {
                ClinvarSet clinvarSet = publicSetParser.parse(clinvarSetXmlString);
                outputQueue.put(clinvarSet);
                recordsProcessed++;

                clinvarSetXmlString = inputQueue.take();
            }
            outputQueue.put(FINISHED_TRANSFORMING);
        } catch (JAXBException e) {
            logger.error("Error transforming clinvar records: '{}", e.getMessage());
            throw e;
        }

        return recordsProcessed;
    }
}
