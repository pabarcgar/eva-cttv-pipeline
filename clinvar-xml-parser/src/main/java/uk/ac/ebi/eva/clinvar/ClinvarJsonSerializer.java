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

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.ObjectWriter;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import uk.ac.ebi.eva.clinvar.model.ClinvarSet;

import java.io.BufferedWriter;
import java.io.IOException;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.Callable;

/**
 * Class that takes ClinvarSet objects from a queue and serialize them in Json format into a Buffered writer. This class
 * extends callable so it can be run in a thread
 */
public class ClinvarJsonSerializer implements Callable<Integer> {

    private static final Logger logger = LoggerFactory.getLogger(ClinvarJsonSerializer.class);

    private final ObjectWriter jsonObjectWriter;

    private final BufferedWriter writer;

    private ArrayBlockingQueue<ClinvarSet> inputQueue;

    private Application application;

    public ClinvarJsonSerializer(ArrayBlockingQueue<ClinvarSet> inputQueue, BufferedWriter writer,
                                 Application application) throws IOException {

        this.inputQueue = inputQueue;
        this.application = application;
        ObjectMapper jsonObjectMapper = new ObjectMapper();
        jsonObjectMapper.setSerializationInclusion(JsonInclude.Include.NON_EMPTY);
        jsonObjectWriter = jsonObjectMapper.writer();
        this.writer = writer;
    }

    /**
     * Take ClinvarSet objects from the input queue, serializing them. It stops when it founds in the queue an special
     * {@link uk.ac.ebi.eva.clinvar.ClinvarSetTransformer#FINISHED_TRANSFORMING object} that is used to indicate that
     * there are not more records
     * @return Number of serialized records
     */
    @Override
    public Integer call() throws IOException, InterruptedException {
        int serialized = 0;
        try {
            ClinvarSet clinvarSet = inputQueue.take();
            while (clinvarSet != ClinvarSetTransformer.FINISHED_TRANSFORMING) {
                writer.write(jsonObjectWriter.writeValueAsString(clinvarSet));
                writer.newLine();
                serialized++;
                if ((serialized % 25000) == 0) {
                    logger.info("{} records serialized", serialized);
                }
                clinvarSet = inputQueue.take();
            }
            writer.close();
        } catch (IOException e) {
            logger.error("Error serializing to Json: '{}", e.getMessage());
            throw e;
        }

        return serialized;
    }
}
