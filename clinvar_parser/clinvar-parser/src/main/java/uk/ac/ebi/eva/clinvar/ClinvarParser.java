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
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.Writer;
import java.util.zip.GZIPInputStream;

/**
 * Hello world!
 *
 */
public class ClinvarParser<T>
{

    private static final Logger logger = LoggerFactory.getLogger(ClinvarParser.class);

    public void parse(String inputFileName, int versionNumber, Writer outputWriter) {
        try {
            // set up json serializer
            ObjectMapper jsonObjectMapper = new ObjectMapper();
            jsonObjectMapper.setSerializationInclusion(JsonInclude.Include.NON_EMPTY);
            ObjectWriter writer = jsonObjectMapper.writer();

            ReleaseType clinvarRelease = unmarshallXmlFIle(inputFileName, versionNumber);
            for (PublicSetType clinvarRecord : clinvarRelease.getClinVarSet()){
                writer.writeValue(outputWriter, clinvarRecord);
            }
        } catch (JAXBException e) {
            logger.error("Cannot unmarshall XML file: {}", e.getMessage());
        } catch (FileNotFoundException e) {
            logger.error(e.getMessage());
        } catch (IOException e) {
            logger.error("Error reading file: {}", e.getMessage());
        }
    }

    private ReleaseType unmarshallXmlFIle(String inputFileName, int versionNumber) throws JAXBException, IOException {
        String contextPath = "uk.ac.ebi.eva.clinvar.model.v" + versionNumber;
        JAXBContext jaxbContext = JAXBContext.newInstance(contextPath);
        Unmarshaller unmarshaller = jaxbContext.createUnmarshaller();

        GZIPInputStream inputFileStream = new GZIPInputStream(new FileInputStream(new File(inputFileName)));
        logger.info("Unmarshalling {}", inputFileName);
        JAXBElement<ReleaseType> xmlRootElement = (JAXBElement<ReleaseType>) unmarshaller.unmarshal(inputFileStream);

        return xmlRootElement.getValue();
    }

}
