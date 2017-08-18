package uk.ac.ebi.eva.clinvar;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.ObjectWriter;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import uk.ac.ebi.eva.clinvar.model.v47.PublicSetType;
import uk.ac.ebi.eva.clinvar.model.v47.ReleaseType;

import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBElement;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Unmarshaller;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.zip.GZIPInputStream;
import java.util.zip.GZIPOutputStream;

/**
 * Hello world!
 *
 */
public class ClinvarParser
{

    private static final Logger logger = LoggerFactory.getLogger(ClinvarParser.class);
    
    public static void main( String[] args )
    {
        // TODO: CLI parser
        String versionNumber = args[1];
        String inputFileName = args[2];
        Path outputFilePath = Paths.get("clinvar.json.gz");

        try {
            // set up json serializer
            ObjectMapper jsonObjectMapper = new ObjectMapper();
            jsonObjectMapper.setSerializationInclusion(JsonInclude.Include.NON_EMPTY);
            ObjectWriter writer = jsonObjectMapper.writer();
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new GZIPOutputStream(Files.newOutputStream(outputFilePath))));

            ReleaseType clinvarRelease = unmarshallXmlFIle(versionNumber, inputFileName);
            for (PublicSetType clinvarRecord : clinvarRelease.getClinVarSet()){
                writer.writeValue(bw, clinvarRecord);
            }
        } catch (JAXBException e) {
            logger.error("Cannot unmarshall XML file: {}", e.getMessage());
        } catch (FileNotFoundException e) {
            logger.error(e.getMessage());
        } catch (IOException e) {
            logger.error("Error reading file: {}", e.getMessage());
        }
    }

    private static ReleaseType unmarshallXmlFIle(String versionNumber,
                                          String inputFileName) throws JAXBException, IOException {
        String contextPath = "uk.ac.ebi.eva.clinvar.model.v" + versionNumber;
        JAXBContext jaxbContext = JAXBContext.newInstance(contextPath);
        Unmarshaller unmarshaller = jaxbContext.createUnmarshaller();

        GZIPInputStream inputFileStream = new GZIPInputStream(new FileInputStream(new File(inputFileName)));
        logger.info("Unmarshalling {}", inputFileName);
        JAXBElement<ReleaseType> xmlRootElement = (JAXBElement<ReleaseType>) unmarshaller.unmarshal(inputFileStream);

        return xmlRootElement.getValue();
    }
}
