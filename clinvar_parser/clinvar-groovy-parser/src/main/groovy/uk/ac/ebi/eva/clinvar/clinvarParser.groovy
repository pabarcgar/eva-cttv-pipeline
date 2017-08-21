package uk.ac.ebi.eva.clinvar

import java.util.concurrent.ArrayBlockingQueue
import java.util.concurrent.ExecutorService
import java.util.concurrent.Executors
import java.util.zip.GZIPInputStream
import java.util.zip.GZIPOutputStream

println "Parsing clinvar ..."

// TODO: read input file name from CLI args
String inputFileName = 'ClinVarFullRelease_2017-06.xml.gz'

GZIPInputStream is = new GZIPInputStream(new FileInputStream(inputFileName))

ArrayBlockingQueue<String> queue = new ArrayBlockingQueue<>(1000)

XmlClinVarReader reader = new XmlClinVarReader(is, queue)

OutputStream outputStream = new GZIPOutputStream(new FileOutputStream("clinvar.json.gz"))
PublicSetWriter publicSetWriter = new PublicSetWriter(queue, "47", outputStream)

ExecutorService executor = Executors.newFixedThreadPool(5)
executor.submit(reader)
executor.submit(publicSetWriter)
println 'Threads submitted to executor'

// TODO: shutdown executor