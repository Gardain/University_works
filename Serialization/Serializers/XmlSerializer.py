import xml.etree.ElementTree as ET

from Serialization.Interface.ISerializer import ISerializer
from Serialization.PetFactory import PetFactory


# Сериализация в XML
class XmlSerializer(ISerializer):
    def to_format(self, pets):
        root = ET.Element("Pets")
        for pet in pets:
            pet_element = ET.Element(pet.__class__.__name__)
            name_element = ET.SubElement(pet_element, "name")
            name_element.text = pet.name
            age_element = ET.SubElement(pet_element, "age")
            age_element.text = str(pet.age)
            root.append(pet_element)
        return ET.tostring(root, encoding='unicode')

    def from_format(self, data):
        root = ET.fromstring(data)
        pets = []
        for pet_element in root:
            pet_type = pet_element.tag
            name = pet_element.find('name').text
            age = int(pet_element.find('age').text)
            pets.append(PetFactory.create_pet(pet_type, name, age))
        return pets
