from json import JSONEncoder


class XMLElementEncoder(JSONEncoder):

    def default(self, element):
        output = dict()
        output[element.tag] = self.xml_element_to_dictionary(element)
        return output

    def xml_element_to_dictionary(self, element):
        attributes = element.attrib

        if len(element.getchildren()) == 0 and len(attributes) == 0:
            # base case: simple element with text and no attributes or children
            #  TODO: if a element has text and attribute(s), would the text be lost?
            return element.text
        else:
            output = dict()
            for child in element:
                output = self.__add_child_to_output(child, output)
            for key in attributes:
                if key in output:
                    raise Exception('Attribute name duplicated: ' + key)
                output[key] = attributes[key]

            return output

    def __add_child_to_output(self, child, output):
        # recursive call to xml_element_to_dictionary to transform the child
        child_dictionary = self.xml_element_to_dictionary(child)

        child_name = child.tag
        if child_name not in output:
            output[child_name] = child_dictionary
        else:
            # like there are several children with the same element name, we encapsulate them in a list
            if isinstance(output[child_name], list):
                output[child_name].append(child_dictionary)
            else:
                children_list = [output[child_name], child_dictionary]
                output[child_name] = children_list

        return output
