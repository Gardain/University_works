# Родительский класс Pet
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} издаёт звук.")

    def info(self):
        print(f"Имя: {self.name}, Возраст: {self.age} лет")


# Наследники класса Pet
class Dog(Pet):
    def make_sound(self):
        print(f"{self.name} гавкает.")


class Cat(Pet):
    def make_sound(self):
        print(f"{self.name} мяукает.")


class Parrot(Pet):
    def make_sound(self):
        print(f"{self.name} говорит: Привет!")


class Rabbit(Pet):
    def make_sound(self):
        print(f"{self.name} шуршит.")


class Fish(Pet):
    def make_sound(self):
        print(f"{self.name} молчит.")


class Hamster(Pet):
    def make_sound(self):
        print(f"{self.name} пищит.")


class Turtle(Pet):
    def make_sound(self):
        print(f"{self.name} медленно двигается без звуков.")


class Snake(Pet):
    def make_sound(self):
        print(f"{self.name} шипит.")


class Horse(Pet):
    def make_sound(self):
        print(f"{self.name} ржёт.")
