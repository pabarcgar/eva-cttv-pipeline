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
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.ObjectWriter;

import uk.ac.ebi.eva.clinvar.model.ClinvarSet;

import java.io.BufferedWriter;
import java.io.IOException;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.Callable;

public class ClinvarJsonSerializer implements Callable<Integer> {

    private final ObjectWriter jsonObjectWriter;

    private final BufferedWriter bw;

    private ArrayBlockingQueue<ClinvarSet> clinvarSetsQueue;

    public ClinvarJsonSerializer(ArrayBlockingQueue<ClinvarSet> clinvarSetsQueue,
                                 BufferedWriter bw) throws IOException {
        this.clinvarSetsQueue = clinvarSetsQueue;
        ObjectMapper jsonObjectMapper = new ObjectMapper();
        jsonObjectMapper.setSerializationInclusion(JsonInclude.Include.NON_EMPTY);
        jsonObjectWriter = jsonObjectMapper.writer();
        this.bw = bw;
    }

    @Override
    public Integer call() {
        int serialized = 0;
        try {
            ClinvarSet clinvarSet = clinvarSetsQueue.take();
            while (clinvarSet != ClinvarSetTransformer.FINISHED_TRANSFORMING) {
                bw.write(jsonObjectWriter.writeValueAsString(clinvarSet));
                bw.newLine();
                serialized++;
                if ((serialized % 25000) == 0) {
                    System.out.println(serialized + " records serialized");
                }
                clinvarSet = clinvarSetsQueue.take();
            }
            bw.close();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return serialized;
    }
}
