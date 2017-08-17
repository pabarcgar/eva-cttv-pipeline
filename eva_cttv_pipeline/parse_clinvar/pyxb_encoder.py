from json import JSONEncoder
from clinvar import AttributeType
from clinvar import MethodType
import pyxb.binding.datatypes
from pyxb.binding.basis import ElementContent
import inspect

class PyxbEncoder(JSONEncoder):

    def default(self, element):
        output = dict()
        output = self.parse_pyxb_element(element, output)
        return output

    def parse_pyxb_element(self, element, output):
        # try:
        # if isinstance(element, ElementContent):
        #     print('aqui')
        # if isinstance(element, AttributeType):
        #     print('attr')
        if self.is_class_or_subclass(element, pyxb.binding.datatypes.string):
            # print('sr')
            return element.__str__
        elif self.is_class_or_subclass(element, MethodType):
            print('method')
        # elif self.is_class_or_subclass(element, pyxb.binding.basis.STD_union):
        #     print('stdUnion')
        elif self.is_class_or_subclass(element, pyxb.binding.basis.complexTypeDefinition):
            #  attributes
            for key, attribute in element._AttributeMap.items():
                attribute_value = attribute.value(element)
                if attribute_value is not None:
                    output[attribute.name().localName()] = str(attribute_value)
            #  children
            for key, child in element._ElementMap.items():

                # output[key.localName()] = self.parse_pyxb_element(child.elementBinding().typeDefinition(), dict(), parent=element)
                output[key.localName()] = self.parse_pyxb_element(child, dict())
                # print (child)
                # print (child)
            # for att in element._AttributeMap:
            #     attrib = element._AttributeMap[att]
            #     print(att.localName() + ':' + att.getAttribute(element._AttributeMap))
            # for child_name in element._ElementMap:
            #     child = element._ElementMap[child_name]
            #     output[child_name.localName()] = self.parse_pyxb_element(child, output)
            tipo = 'complex'
        elif self.is_class_or_subclass(element.elementBinding().typeDefinition(), pyxb.binding.basis.complexTypeDefinition):
            type_definition = element.elementBinding().typeDefinition()
            for key, attribute in type_definition._AttributeMap.items():
                attribute_value = attribute.value(element)
                print( attribute_value)
        elif self.is_class_or_subclass(element, pyxb.binding.basis.enumeration_mixin):
            print('enumeration')
        else:
            print ('None')
            tipo = type(element)
        # except TypeError:
        #     print(type(element))

        return output

    def is_class_or_subclass(self, element, class_name):
        if isinstance(element, class_name):
            return True
        elif inspect.isclass(element) and issubclass(element, class_name):
            return True
        else:
            return False