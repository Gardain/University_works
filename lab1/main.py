from serialization.interface.ISerializer import ISerializer
from Pets import Pet
from serialization.PetFactory import PetFactory
from serialization.Storage import Storage
from serialization.serializers.JsonSerializer import JsonSerializer
from serialization.serializers.XmlSerializer import XmlSerializer
from exceptions import InvalidPetTypeException, InvalidFileTypeException


def create_serializer(file_type) -> ISerializer:
    file_types = {
        'json': JsonSerializer(),
        'xml': XmlSerializer()
    }

    if file_type not in file_types:
        raise InvalidFileTypeException(file_type)
    return file_types[file_type]


def create_pet() -> Pet:
    try:
        pet_type = input("Введите тип питомца (Dog, Cat, Parrot, etc.): ")
        name = input("Введите имя питомца: ")
        age = int(input("Введите возраст питомца: "))
        return PetFactory.create_pet(pet_type, name, age)
    except ValueError:
        print("Ошибка: возраст должен быть числом.")
    except InvalidPetTypeException as e:
        print(e)


if __name__ == "__main__":
    pets = []
    storage = None

    while True:
        print("\n1. Создать нового питомца")
        print("2. Показать всех питомцев")
        print("3. Издать голос питомцу")
        print("4. Сохранить питомцев в файл")
        print("5. Загрузить питомцев из файла")
        print("6. Выйти")

        choice = input("\nВыберите действие: ")

        match choice:
            case "1":
                pet = create_pet()
                if pet:
                    pets.append(pet)
                    print(f"Питомец {pet.name} добавлен.")

            case "2":
                if not pets:
                    print("\nПитомцы отсутствуют.")
                    continue
                for pet in pets:
                    pet.info()

            case "3":
                if not pets:
                    print("\nСписок питомцев пуст.")
                    continue
                for idx, pet in enumerate(pets, start=1):
                    print(f"{idx}. {pet.name} ({pet.__class__.__name__})")
                selected_idx = int(input("Введите номер питомца: ")) - 1
                pets[selected_idx].make_sound()

            case "4":
                file_format = input("Сохранить как (json/xml)? ").lower()
                try:
                    storage = Storage(create_serializer(file_format))
                    storage.save_to_file(f"DB/pets.{file_format}", pets)
                except InvalidFileTypeException as e:
                    print(e)

            case "5":
                file_format = input("Загрузить из (json/xml)? ").lower()
                try:
                    storage = Storage(create_serializer(file_format))
                    pets = storage.load_from_file(f"DB/pets.{file_format}")
                except InvalidFileTypeException as e:
                    print(e)

            case "6":
                print("Выход из программы.")
                break