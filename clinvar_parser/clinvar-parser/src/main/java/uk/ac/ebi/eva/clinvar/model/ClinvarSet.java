package uk.ac.ebi.eva.clinvar.model;

import uk.ac.ebi.eva.clinvar.ClinvarParser;

public class ClinvarSet<T> {
    private T clinvarSet;

    public ClinvarSet(T clinvarSet) {
        this.clinvarSet = clinvarSet;
    }

    public T getClinvarSet() {
        return clinvarSet;
    }

    public void setClinvarSet(T clinvarSet) {
        this.clinvarSet = clinvarSet;
    }
}
