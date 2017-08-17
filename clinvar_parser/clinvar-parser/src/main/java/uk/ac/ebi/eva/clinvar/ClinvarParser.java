package uk.ac.ebi.eva.clinvar;

import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBElement;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Unmarshaller;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.zip.GZIPInputStream;

/**
 * Hello world!
 *
 */
public class ClinvarParser
{
    public static void main( String[] args )
    {
        // CLI parser
        String contextPath = args[1];
        String inputFileName = args[2];

        try {
            JAXBContext jaxbContext = JAXBContext.newInstance(contextPath);
            Unmarshaller unmarshaller = jaxbContext.createUnmarshaller();
            Object obj = unmarshaller.unmarshal(new GZIPInputStream(new FileInputStream(new File(inputFileName))));
        } catch (JAXBException e) {
            System.out.println(e.getMessage());
            e.printStackTrace();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println( "Hello World!");
    }
}
