import gzip
import argparse
import sys
import urllib.request
import shutil
import subprocess
import os

SCHEMA_LOCATION_ATTRIBUTE = 'SchemaLocation'


def launch():
    parser = ArgParser(sys.argv)

    # get clinvar schema xsd file
    schema_url = get_schema_url(parser)
    schema_temp_file = donwload_schema_file(schema_url)

    # compile xsd schema
    generate_java_binding_classes('uk.ac.ebi.eva.clinvar.model.jaxb', parser, schema_temp_file)

    remove_schema_file(schema_temp_file)


def get_schema_url(parser):
    with gzip.open(parser.input_file, 'rt') as xml_file:
        schema_url = None
        for line in xml_file:
            if SCHEMA_LOCATION_ATTRIBUTE in line:
                schema_url = line.split(SCHEMA_LOCATION_ATTRIBUTE)[1].split('"')[1]
                break

        if schema_url is None:
            print('Error: XSD schema URL not found in ' + parser.input_file)
            sys.exit(1)

    return schema_url


def donwload_schema_file(schema_url):
    schema_temp_file = schema_url.split('/')[-1]
    print('Downloading ' + schema_url + ' ... ')
    urllib.request.urlretrieve(schema_url, schema_temp_file)
    print('Done\n')
    return schema_temp_file


def generate_java_binding_classes(package_name, parser, schema_temp_file):
    java_sources_dir = parser.java_sources_dir
    package_folder = java_sources_dir + '/' + package_name.replace('.', '/')
    if os.path.isdir(package_folder):
        print('Deleting previous version of ' + package_name + '...\n')
        shutil.rmtree(package_folder)
    # execute xjc to compile the XSD schema
    print('Generating JAXB classes in ' + package_name + ' ...')
    subprocess.run(['xjc', '-p', package_name, '-d', java_sources_dir, schema_temp_file])
    print('Done\n')


def remove_schema_file(schema_temp_file):
    # remove schema_temp_file
    print('Removing temporary schema file ' + schema_temp_file + ' ...')
    os.remove(schema_temp_file)
    print('Done\n')


class ArgParser:
    def __init__(self, argv):
        script_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
        root_dir = os.path.abspath(os.path.join(script_dir, os.pardir))
        java_default_sources_folder = os.path.join(root_dir, 'clinvar-xml-parser/src/main/java')

        description = '''Script for downloading a Clinvar release schema definition file and compile it using Jaxb'''

        parser = argparse.ArgumentParser(description=description)

        parser.add_argument('-i', dest='input_file', required=True, help='Clinvar XML input file')

        parser.add_argument('-j', dest='java_sources_folder', required=False,
                            help='Java Clinvar Parser sources folder', default=java_default_sources_folder)

        args = parser.parse_args(args=argv[1:])

        # validate parameters
        if not os.path.isfile(args.input_file):
            print('Error: input file ' + args.input_file + ' not found')
            sys.exit(1)
        if not os.path.isdir(args.java_sources_folder):
            print('Error: java sources folder ' + args.java_sources_folder + ' not found')
            sys.exit(1)

        self.input_file = args.input_file
        self.java_sources_dir = args.java_sources_folder


if __name__ == '__main__':
    launch()
