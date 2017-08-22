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

import javax.xml.stream.XMLStreamException;
import java.io.InputStream;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.Callable;

/**
 * Class that reads a Clinvar release XML in an input stream, extracting each "ClinvarSet" XML record and putting them
 * as Strings into an output queue. This class extends callable so it can be run in a thread
 */
public class XmlClinVarReader implements Callable<Integer> {

    private InputStream inputStream;

    private ArrayBlockingQueue<String> queue;

    /** Special String used to indicate all the records have been extracted from the input XML */
    public static final String FINISHED = "";

    public XmlClinVarReader(InputStream inputStream, ArrayBlockingQueue<String> outputQueue) {
        this.inputStream = inputStream;
        this.queue = outputQueue;
    }

    /**
     * Parse the input XML, putting the "ClinvarSet" XML records into the output queue, adding an special
     * {@link uk.ac.ebi.eva.clinvar.XmlClinVarReader#FINISHED String} to the output queue when there are no more records
     * in the input Stream.
     * @return Number of read records
     */
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
