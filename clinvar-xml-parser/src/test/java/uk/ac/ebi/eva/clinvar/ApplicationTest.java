package uk.ac.ebi.eva.clinvar;

import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.TemporaryFolder;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.zip.GZIPInputStream;

import static org.junit.Assert.assertEquals;

public class ApplicationTest {

    @Rule
    public TemporaryFolder outputFolder = new TemporaryFolder();

    @Test
    public void clinvar47IntegrationTest() throws Exception {
        // application command line arguments
        Path inputFilePath = Paths.get(this.getClass().getResource("/ClinvarExample.xml.gz").toURI());
        String outputFolderAbsolutePath = outputFolder.getRoot().getAbsolutePath();
        String[] args = {"--inputFileName", inputFilePath.toString(),
                "--outputDir", outputFolderAbsolutePath,
                "--clinvarVersion", "47"};

        // execute application
        Application.main(args);

        // check that an output gzipped file containing 10 lineas has been generated
        GZIPInputStream gzipJsonFile = new GZIPInputStream(
                new FileInputStream(outputFolderAbsolutePath + "/" + Application.OUTPUT_FILE_NAME));
        BufferedReader br = new BufferedReader(new InputStreamReader(gzipJsonFile));
        assertEquals(10, br.lines().count());
    }

}