package uk.ac.ebi.eva.clinvar;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.ObjectWriter;

import uk.ac.ebi.eva.clinvar.model.ClinvarSet;

import java.io.BufferedWriter;
import java.io.IOException;
import java.util.concurrent.ArrayBlockingQueue;

public class ClinvarSetWriter implements Runnable {

    private final ObjectWriter jsonObjectWriter;

    private final BufferedWriter bw;

    private ArrayBlockingQueue<ClinvarSet> clinvarSetsQueue;

    public ClinvarSetWriter(ArrayBlockingQueue<ClinvarSet> clinvarSetsQueue, BufferedWriter bw) throws IOException {

        this.clinvarSetsQueue = clinvarSetsQueue;
        ObjectMapper jsonObjectMapper = new ObjectMapper();
        jsonObjectMapper.setSerializationInclusion(JsonInclude.Include.NON_EMPTY);
        jsonObjectWriter = jsonObjectMapper.writer();
        this.bw = bw;
    }

    @Override
    public void run() {
        try {
            int serialized = 0;
            ClinvarSet clinvarSet = clinvarSetsQueue.take();
            while (clinvarSet != ClinvarSetTransformer.FINISHED_TRANSFORMING) {
                bw.write(jsonObjectWriter.writeValueAsString(clinvarSet));
                bw.newLine();
                serialized++;
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
        App.closeExecutor();
    }
}
