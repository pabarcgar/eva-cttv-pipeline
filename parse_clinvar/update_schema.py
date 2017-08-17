import gzip
import argparse
import sys
import urllib.request
import subprocess

SCHEMA_LOCATION_ATTRIBUTE = 'SchemaLocation'

def launch():
	parser = ArgParser(sys.argv)
	with gzip.open(parser.input_file, 'rt') as xml_file:
		i = 0
		for line in xml_file:
			if SCHEMA_LOCATION_ATTRIBUTE in line:
				schema_url = line.split(SCHEMA_LOCATION_ATTRIBUTE)[1].split('"')[1]
				break

		if schema_url is None:
			print('Error: XSD schema URL not found in ' + parser.input_file)
			sys.exit(1)

	# download file
	schema_temp_file = schema_url.split('/')[-1]
	urllib.request.urlretrieve(schema_url, schema_temp_file)

	clinvar_schema_version = schema_temp_file.split('.')[1]
	package_name = 'uk.ac.ebi.eva.clinvar.model.v' + clinvar_schema_version
	print (package_name)

	# execute jaxc
	# subprocess.run(['xjc', '-p', 'uk.ac.ebi.eva.clinvar.model.v' ])

	# remove schema_temp_file


class ArgParser:

	def __init__(self, argv):
		description = '''
				Script for downloading a Clinvar release schema definition file and compile it using Jaxb
				'''
		parser = argparse.ArgumentParser(description=description)

		parser.add_argument('-i', dest='input_file', required=True, help='Clinvar XML input file')

		args = parser.parse_args(args=argv[1:])

		self.input_file = args.input_file

if __name__ == '__main__':
	launch()
