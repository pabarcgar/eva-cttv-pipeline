import org.codehaus.groovy.control.customizers.ImportCustomizer

def importCustomizer = new ImportCustomizer()

// TODO: look how to inject the version number in this configuration script using gradle build
importCustomizer.addImport('uk.ac.ebi.eva.clinvar.model.v47.PublicSetType')

configuration.addCompilationCustomizers(importCustomizer)
