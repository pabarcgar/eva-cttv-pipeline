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

// TODO: document this class, and add license
public class XmlClinVarSetIterator {

    public static final String CLINVAR_SET_XML_TAG = "ClinVarSet";

    private final XMLEventReader xmlReader;

    private final XMLOutputFactory xmlOutputFactory;

    public XmlClinVarSetIterator(InputStream inputStream) throws XMLStreamException {
        xmlReader = XMLInputFactory.newInstance().createXMLEventReader(inputStream);
        xmlOutputFactory = XMLOutputFactory.newInstance();
    }

    public String next() throws XMLStreamException {
        StringWriter sw = new StringWriter();
        XMLEventWriter xmlWriter = null;

        // TODO: refactor
        boolean parsedElement = false;
        while (!parsedElement && xmlReader.hasNext()) {
            XMLEvent xmlEvent = xmlReader.nextEvent();
            if (isClinvarSetStartElement(xmlEvent)) {
                xmlWriter = xmlOutputFactory.createXMLEventWriter(sw);
                xmlWriter.add(xmlEvent);
            } else if (isClinvarSetEndElement(xmlEvent)) {
                xmlWriter.add(xmlEvent);
                parsedElement = true;
            } else if (xmlWriter != null) {
                xmlWriter.add(xmlEvent);
            }
        }

        if (parsedElement) {
            xmlWriter.close();
            return sw.toString();
        } else {
            return null;
        }

    }

    private boolean isClinvarSetEndElement(XMLEvent xmlEvent) {
        return xmlEvent.isEndElement() && ((EndElement) xmlEvent).getName().getLocalPart().equals(CLINVAR_SET_XML_TAG);
    }

    private boolean isClinvarSetStartElement(XMLEvent xmlEvent) {
        return xmlEvent.isStartElement() && ((StartElement) xmlEvent).getName().getLocalPart().equals(
                CLINVAR_SET_XML_TAG);
    }
}
