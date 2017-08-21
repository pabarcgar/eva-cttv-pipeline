package uk.ac.ebi.eva.clinvar

import com.fasterxml.jackson.annotation.JsonInclude
import com.fasterxml.jackson.core.JsonGenerator
import com.fasterxml.jackson.databind.ObjectMapper
import com.fasterxml.jackson.databind.ObjectWriter
import com.fasterxml.jackson.databind.SerializationFeature

import java.util.concurrent.ArrayBlockingQueue

class PublicSetWriter implements Runnable {

    ArrayBlockingQueue<String> inputQueue
//    ObjectWriter objectWriter
    ObjectMapper jsonObjectMapper
//    OutputStreamWriter outputWriter
    PublicSetParser publicSetParser
    OutputStream outputStream

    PublicSetWriter(ArrayBlockingQueue<String> inputQueue, String clinvarVersion, OutputStream outputStream) {
        this.inputQueue = inputQueue
        jsonObjectMapper = new ObjectMapper()
        jsonObjectMapper.setSerializationInclusion(JsonInclude.Include.NON_EMPTY)
        jsonObjectMapper.configure(JsonGenerator.Feature.AUTO_CLOSE_TARGET, false)
//        jsonObjectMapper.configure(SerializationFeature.CLOSE_CLOSEABLE, false)
        this.outputStream = outputStream
//        objectWriter = jsonObjectMapper.writer()
//        outputWriter = writer

        publicSetParser = new PublicSetParser("uk.ac.ebi.eva.clinvar.model.v" + clinvarVersion)
    }

    @Override
    void run() {

        int i = 0
        String clinvarSet = inputQueue.take()
        try {
            while (clinvarSet != XmlClinVarReader.FINISHED) {
//                println 'transforming'
                PublicSetType objectToWrite = publicSetParser.parse(clinvarSet)
//                println 'transformed. Writting ...'

                    jsonObjectMapper.writeValue(outputStream, objectToWrite)

//                println 'written'
                i++
//                println i + ' written'
//                println 'taking second'
                clinvarSet = inputQueue.take()
//                println 'taken'
            }
        } catch(IOException e) {
            println 'Cannot write: ' + e.getLocalizedMessage()
        }
        outputStream.close()
        println 'Finished writting ' + i + ' records'

    }
}
