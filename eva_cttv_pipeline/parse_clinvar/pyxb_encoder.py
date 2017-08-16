from json import JSONEncoder
from clinvar import AttributeType
from clinvar import MethodType
import pyxb.binding.datatypes


class PyxbEncoder(JSONEncoder):

    def default(self, element):
        output = dict()
        output = self.parse_pyxb_element(element, output)
        return output

    def parse_pyxb_element(self, element, output):
        if isinstance(element, AttributeType):
            tipo = 'attr'
        elif isinstance(element, MethodType):
            tipo = 'method'
        elif isinstance(element, pyxb.binding.basis.STD_union):
            tipo = 'stdUnion'
        elif isinstance(element, pyxb.binding.basis.complexTypeDefinition):
            #  attributes
            for key, attribute in element._AttributeMap.items():
                output[attribute.name().localName()] = str(attribute.value(element))
            #  children
            for key, child in element._ElementMap.items():
                output[key.localName()] = self.parse_pyxb_element(child.elementBinding().typeDefinition(), output)
                # print (child)
                # print (child)
            # for att in element._AttributeMap:
            #     attrib = element._AttributeMap[att]
            #     print(att.localName() + ':' + att.getAttribute(element._AttributeMap))
            # for child_name in element._ElementMap:
            #     child = element._ElementMap[child_name]
            #     output[child_name.localName()] = self.parse_pyxb_element(child, output)
            tipo = 'complex'
        elif isinstance(element, pyxb.binding.basis.enumeration_mixin):
            tipo = 'enumeration'
        elif isinstance(element, pyxb.binding.datatypes.string):
            return element.__str__
        else:
            tipo = type(element)

        return output