package uk.ac.ebi.eva.clinvar.model;

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
