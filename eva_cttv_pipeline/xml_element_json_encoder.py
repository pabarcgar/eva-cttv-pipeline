from json import JSONEncoder


class XMLElementEncoder(JSONEncoder):
    def default(self, element):
        output = dict()
        output[element.tag] = self.xml_element_to_json(element)
        return output

    def xml_element_to_json(self, element):
        attributes = element.attrib
        if len(element.getchildren()) == 0 and len(attributes) == 0:
            return element.text
        else:
            output = dict()
            for child in element:
                if not child.tag in output:
                    output[child.tag] = self.xml_element_to_json(child)
                else:
                    if isinstance(output[child.tag], list):
                        output[child.tag].append(self.xml_element_to_json(child))
                    else:
                        new_list = [output[child.tag], self.xml_element_to_json(child)]
                        output[child.tag] = new_list
            for key in element.attrib:
                if key in output:
                    raise Exception('Attribute name duplicated: ' + key)
                output[key] = element.attrib[key]

            return output
