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

/**
 * Iterates over an input XML Stream, returning a full "ClinvarSet" XML Record in each iteration
 */
public class XmlClinVarSetIterator {

    public static final String CLINVAR_SET_XML_TAG = "ClinVarSet";

    private final XMLEventReader xmlReader;

    private final XMLOutputFactory xmlOutputFactory;

    public XmlClinVarSetIterator(InputStream inputStream) throws XMLStreamException {
        xmlReader = XMLInputFactory.newInstance().createXMLEventReader(inputStream);
        xmlOutputFactory = XMLOutputFactory.newInstance();
    }

    /**
     * Method that reads and return a "ClinvarSet" XML record from the input Stream, ignoring all the XML elements that
     * are not part of the "ClinvarSet"
     * @return "ClinvarSet" XML record
     * @throws XMLStreamException If the input XML stream cannot be parsed
     */
    public String next() throws XMLStreamException {
        boolean parsedElement = false;

        StringWriter sw = new StringWriter();
        XMLEventWriter xmlWriter = xmlOutputFactory.createXMLEventWriter(sw);
        boolean inClinvarSetElement = false;

        while (!parsedElement && xmlReader.hasNext()) {
            XMLEvent xmlEvent = xmlReader.nextEvent();

            // if we are in the start or end of a clinvarSet element, we set the corresponding flag
            if (isClinvarSetStartElement(xmlEvent)) {
                inClinvarSetElement = true;
            } else if (isClinvarSetEndElement(xmlEvent)) {
                parsedElement = true;
            }

            // the xml event content is written to the output just if it is a subelement of a clinvarSet one
            if (inClinvarSetElement) {
                xmlWriter.add(xmlEvent);
            }
        }

        // the xml writer needs to be closed to be sure the whole XML element is written to the output
        xmlWriter.close();

        return parsedElement ? sw.toString() : null;
    }

    private boolean isClinvarSetEndElement(XMLEvent xmlEvent) {
        return xmlEvent.isEndElement() && ((EndElement) xmlEvent).getName().getLocalPart().equals(CLINVAR_SET_XML_TAG);
    }

    private boolean isClinvarSetStartElement(XMLEvent xmlEvent) {
        return xmlEvent.isStartElement() && ((StartElement) xmlEvent).getName().getLocalPart().equals(
                CLINVAR_SET_XML_TAG);
    }
}
