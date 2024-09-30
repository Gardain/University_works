import json
import xml.etree.ElementTree as ET
import Pet_classes


# Класс для сериализации и десериализации данных в форматах JSON и XML
class PetSerializer:
    @staticmethod
    def to_json(pet):
        return json.dumps({"type": pet.__class__.__name__, "name": pet.name, "age": pet.age})

    @staticmethod
    def to_xml(pet):
        pet_element = ET.Element(pet.__class__.__name__)
        name_element = ET.SubElement(pet_element, "name")
        name_element.text = pet.name
        age_element = ET.SubElement(pet_element, "age")
        age_element.text = str(pet.age)
        return ET.tostring(pet_element, encoding='unicode')

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        pet_type = data['type']
        name = data['name']
        age = data['age']
        return PetSerializer._create_pet(pet_type, name, age)

    @staticmethod
    def from_xml(xml_str):
        root = ET.fromstring(xml_str)
        pet_type = root.tag
        name = root.find('name').text
        age = int(root.find('age').text)
        return PetSerializer._create_pet(pet_type, name, age)

    @staticmethod
    def _create_pet(pet_type, name, age):
        pets = {
            'Dog': Pet_classes.Dog,
            'Cat': Pet_classes.Cat,
            'Parrot': Pet_classes.Parrot,
            'Rabbit': Pet_classes.Rabbit,
            'Fish': Pet_classes.Fish,
            'Hamster': Pet_classes.Hamster,
            'Turtle': Pet_classes.Turtle,
            'Snake': Pet_classes.Snake,
            'Horse': Pet_classes.Horse
        }
        return pets.get(pet_type, Pet_classes.Pet)(name, age)
