package uk.ac.ebi.eva.clinvar;

import uk.ac.ebi.eva.clinvar.model.ClinvarSet;
import uk.ac.ebi.eva.clinvar.model.v47.ClinvarSetV47;

import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBElement;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Unmarshaller;
import javax.xml.transform.stream.StreamSource;
import java.io.StringReader;

class PublicSetParser<T> {

    Unmarshaller unmarshaller;

    public PublicSetParser(String contextPath) throws JAXBException {
        JAXBContext jaxbContext = JAXBContext.newInstance(contextPath);
        this.unmarshaller = jaxbContext.createUnmarshaller();
    }

    public ClinvarSet parse(String clinvarPublicSetXmlString) throws JAXBException {
        StreamSource source = new StreamSource(new StringReader(clinvarPublicSetXmlString));
        JAXBElement<T> xmlElement = (JAXBElement<T>) unmarshaller.unmarshal(source);
        return new ClinvarSet<T>(xmlElement.getValue());
    }

}
