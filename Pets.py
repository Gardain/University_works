# Родительский класс Pet
class Pet:
    def __init__(self, name, age) -> None:
        self._name = name
        self._age = age

    def make_sound(self) -> None:
        print(f"{self._name} издаёт звук.")

    def info(self) -> None:
        print(f"Имя: {self._name}, Возраст: {self._age} лет")

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value) -> None:
        if not isinstance(value, str):
            raise ValueError("Имя должно быть строкой!")
        self._name = value

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value) -> None:
        if not isinstance(value, int):
            raise ValueError("")
        self._age = value


# Наследники класса Pet
class Dog(Pet):
    def make_sound(self) -> None:
        print(f"{self._name} гавкает.")


class Cat(Pet):
    def make_sound(self) -> None:
        print(f"{self._name} мяукает.")


class Parrot(Pet):
    def make_sound(self) -> None:
        print(f"{self._name} говорит: Привет!")


class Rabbit(Pet):
    def make_sound(self) -> None:
        print(f"{self._name} шуршит.")


class Fish(Pet):
    def make_sound(self) -> None:
        print(f"{self._name} молчит.")


class Hamster(Pet):
    def make_sound(self) -> None:
        print(f"{self._name} пищит.")


class Turtle(Pet):
    def make_sound(self) -> None:
        print(f"{self._name} медленно двигается без звуков.")


class Snake(Pet):
    def make_sound(self) -> None:
        print(f"{self._name} шипит.")


class Horse(Pet):
    def make_sound(self) -> None:
        print(f"{self._name} ржёт.")
