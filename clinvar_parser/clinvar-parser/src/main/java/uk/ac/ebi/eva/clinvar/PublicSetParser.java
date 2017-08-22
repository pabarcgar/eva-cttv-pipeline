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

import uk.ac.ebi.eva.clinvar.model.ClinvarSet;

import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBElement;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Unmarshaller;
import javax.xml.transform.stream.StreamSource;
import java.io.StringReader;

public class PublicSetParser {

    private Unmarshaller unmarshaller;

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
