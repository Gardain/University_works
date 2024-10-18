class InvalidPetTypeException(Exception):
    def __init__(self, pet_type):
        super().__init__(f"Неверный тип питомца: {pet_type}. Допустимые типы: Dog, Cat, Parrot и др.")


class InvalidFileTypeException(Exception):
    def __init__(self, file_type):
        super().__init__(f"Неверный тип файла: {file_type}. Допустимые типы: json, xml.")
