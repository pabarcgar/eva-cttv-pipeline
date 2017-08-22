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
