package uk.ac.ebi.eva.clinvar;

import uk.ac.ebi.eva.clinvar.model.ClinvarSet;

import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBElement;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Unmarshaller;
import javax.xml.transform.stream.StreamSource;
import java.io.StringReader;

class PublicSetParser {

    Unmarshaller unmarshaller;

    public PublicSetParser(String contextPath) throws JAXBException {
        JAXBContext jaxbContext = JAXBContext.newInstance(contextPath);
        this.unmarshaller = jaxbContext.createUnmarshaller();
    }

    public ClinvarSet parse(String clinvarPublicSetXmlString) throws JAXBException {
        StreamSource source = new StreamSource(new StringReader(clinvarPublicSetXmlString));
        JAXBElement xmlElement = (JAXBElement) unmarshaller.unmarshal(source);
        return new ClinvarSet(xmlElement.getValue());
    }

}
