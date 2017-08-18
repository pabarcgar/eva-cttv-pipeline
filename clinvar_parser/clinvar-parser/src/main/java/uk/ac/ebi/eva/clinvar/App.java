package uk.ac.ebi.eva.clinvar;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.ObjectWriter;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.zip.GZIPOutputStream;

public class App {

    public static void main(String[] args) {
        // TODO: CLI parser
        int versionNumber = Integer.parseInt(args[1]);
        String inputFileName = args[2];
        // TODO: output directory
        Path outputFilePath = Paths.get("clinvar.json.gz");

        ClinvarParser parser = new ClinvarParser();
        try {
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new GZIPOutputStream(
                    Files.newOutputStream(outputFilePath))));
            parser.parse(inputFileName, versionNumber, bw);
        } catch (IOException e) {
            // TODO: log message
//            logger.error("Error reading file: {}", e.getMessage());
        }
    }
}
