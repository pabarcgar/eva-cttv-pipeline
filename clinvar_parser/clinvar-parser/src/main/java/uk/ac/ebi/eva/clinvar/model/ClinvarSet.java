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
package uk.ac.ebi.eva.clinvar.model;

/**
 * This class encapsulates a "clinvarSet" record in a convenient way for being serialized to Json. In addition to that,
 * it allows us to abstract {@link uk.ac.ebi.eva.clinvar.PublicSetParser} from the actual version of Clinvar that is
 * being parsed, so is not necessary to recompile the code for processing different clinvar versions
 */
public class ClinvarSet {
    private Object clinvarSet;

    public ClinvarSet(Object clinvarSet) {
        this.clinvarSet = clinvarSet;
    }

    public Object getClinvarSet() {
        System.out.println(clinvarSet.getClass().getCanonicalName());
        return clinvarSet;
    }

    public void setClinvarSet(Object clinvarSet) {
        this.clinvarSet = clinvarSet;
    }
}
