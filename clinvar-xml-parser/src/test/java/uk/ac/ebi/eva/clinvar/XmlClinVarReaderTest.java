package uk.ac.ebi.eva.clinvar;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.InputStream;
import java.util.Iterator;
import java.util.List;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.stream.Collectors;

import static org.junit.Assert.*;

/**
 * Created by pagarcia on 29/08/17.
 */
public class XmlClinVarReaderTest {

    private static final int CLINVAR_RECORDS_IN_TEST_FILE = 10;

    @Test
    public void testCall() throws Exception {
        InputStream  clinvarExampleInputStrema = this.getClass().getResourceAsStream("/ClinvarExample.xml");
        // the capacity of the queue is the number of records in the test file plus one, because the reader
        // adds an object at the end to indicate it has finished reading
        ArrayBlockingQueue<String> queue = new ArrayBlockingQueue<>(CLINVAR_RECORDS_IN_TEST_FILE + 1);
        XmlClinVarReader reader = new XmlClinVarReader(clinvarExampleInputStrema, queue);

        int clinvarRecordsRead = reader.call();

        // collect the queue objects into a list because is more convenient to assert the results
        List<String> clinvarRecords = queue.stream().collect(Collectors.toList());

        assertEquals(CLINVAR_RECORDS_IN_TEST_FILE, clinvarRecordsRead);
        assertEquals(CLINVAR_RECORDS_IN_TEST_FILE + 1 ,clinvarRecords.size());

        // the last record in the queue is the one that the reader adds to indicate it has finished
        assertEquals(XmlClinVarReader.FINISHED, clinvarRecords.get(CLINVAR_RECORDS_IN_TEST_FILE));

    }
}