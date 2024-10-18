import json
from Serialization.Interface.ISerializer import ISerializer
from Serialization.PetFactory import PetFactory


class JsonSerializer(ISerializer):
    def to_format(self, pets):
        pets_data = [{"type": pet.__class__.__name__, "name": pet.name, "age": pet.age} for pet in pets]
        return json.dumps(pets_data, ensure_ascii=False)

    def from_format(self, data):
        pets_data = json.loads(data)
        return [PetFactory.create_pet(pet_data['type'], pet_data['name'], pet_data['age']) for pet_data in pets_data]
