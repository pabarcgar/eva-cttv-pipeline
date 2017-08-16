from lxml import etree

from eva_cttv_pipeline.xml_element_json_encoder import XMLElementEncoder

import unittest


class XMLElementEncoderTest(unittest.TestCase):

    def test_encode_xml(self):
        # read XML resource file
        tree = etree.parse('resources/simple.xml')

        # pass xml element to encoder
        encoder = XMLElementEncoder()
        result = encoder.default(tree.getroot())

        # assert result
        charlie_one_list = ['sublabel CharlieOne a', 'sublabel CharlieOne b', 'sublabel CharlieOne c']
        dict_charlie = dict(id='id Charlie', CharlieOne=charlie_one_list)
        dict_delta = dict(id='id Delta', value='label Delta')
        dict_alpha = dict(id='id Alpha', Beta='label Beta', Charlie=dict_charlie, Delta=dict_delta)
        expected_result = dict(Alpha=dict_alpha)
        print(expected_result)
        self.maxDiff = None
        self.assertDictEqual(expected_result, result)

    # def test_conflict_in_attribute_name(self):
        # read XML resource file
        # pass xml element to encoder
        # assert exception is thrown

    # def test_encode_clinvar_record(self):
        # read XML containing clinvar record / records
        # pass xml element to encoder
        # assert key fields are exported