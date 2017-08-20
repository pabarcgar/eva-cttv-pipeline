package uk.ac.ebi.eva.clinvar

import javax.xml.bind.JAXBContext
import javax.xml.bind.JAXBElement
import javax.xml.bind.Unmarshaller
import javax.xml.transform.stream.StreamSource

class PublicSetParser {

    Unmarshaller unmarshaller

    PublicSetParser(String contextPath) {
        JAXBContext jaxbContext = JAXBContext.newInstance(contextPath)
        this.unmarshaller = jaxbContext.createUnmarshaller()
    }

    PublicSetType parse(String clinvarPublicSetXmlString) {
        def source = new StreamSource(new StringReader(clinvarPublicSetXmlString))
        JAXBElement<PublicSetType> xmlElement = unmarshaller.unmarshal(source)
        return xmlElement.getValue()
    }

}
