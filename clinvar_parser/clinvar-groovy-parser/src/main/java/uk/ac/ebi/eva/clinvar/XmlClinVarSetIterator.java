package uk.ac.ebi.eva.clinvar;

import javax.xml.stream.XMLEventReader;
import javax.xml.stream.XMLEventWriter;
import javax.xml.stream.XMLInputFactory;
import javax.xml.stream.XMLOutputFactory;
import javax.xml.stream.XMLStreamException;
import javax.xml.stream.events.EndElement;
import javax.xml.stream.events.StartElement;
import javax.xml.stream.events.XMLEvent;
import java.io.InputStream;
import java.io.StringWriter;

// TODO: document this class
public class XmlClinVarSetIterator {

    public static final String CLINVAR_SET = "ClinVarSet";

    private final XMLEventReader xr;

    public XmlClinVarSetIterator(InputStream inputStream) throws XMLStreamException {
        xr = XMLInputFactory.newInstance().createXMLEventReader(inputStream);
    }

    public String next() throws XMLStreamException {
        StringWriter sw = new StringWriter();
        XMLOutputFactory of = XMLOutputFactory.newInstance();
        XMLEventWriter xw = null;

        // TODO: refactor
        while (xr.hasNext()) {
            XMLEvent e = xr.nextEvent();
            if (e.isStartElement() && ((StartElement) e).getName().getLocalPart().equals(CLINVAR_SET)) {
                xw = of.createXMLEventWriter(sw);
                xw.add(e);
            } else if (e.isEndElement() && ((EndElement) e).getName().getLocalPart().equals(CLINVAR_SET)) {
                xw.add(e);
                break;
            } else if (xw != null) {
                xw.add(e);
            }
        }

        if (xw != null) {
            xw.close();
            return sw.toString();
        } else {
            return null;
        }

    }
}
