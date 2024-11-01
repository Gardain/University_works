from lab1.Pets import Dog, Cat, Parrot, Rabbit, Fish, Hamster, Turtle, Snake, Horse
from lab1.exceptions import InvalidPetTypeException


# Фабрика для создания объектов питомцев
class PetFactory:
    pets = {
        'Dog': lambda name, age: Dog(name, age),
        'Cat': lambda name, age: Cat(name, age),
        'Parrot': lambda name, age: Parrot(name, age),
        'Rabbit': lambda name, age: Rabbit(name, age),
        'Fish': lambda name, age: Fish(name, age),
        'Hamster': lambda name, age: Hamster(name, age),
        'Turtle': lambda name, age: Turtle(name, age),
        'Snake': lambda name, age: Snake(name, age),
        'Horse': lambda name, age: Horse(name, age)
    }

    @staticmethod
    def create_pet(pet_type, name, age):
        if pet_type not in PetFactory.pets:
            raise InvalidPetTypeException(pet_type)
        return PetFactory.pets[pet_type](name, age)
