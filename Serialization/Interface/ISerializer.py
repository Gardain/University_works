from abc import ABC, abstractmethod

# Интерфейс для сериализации
class ISerializer(ABC):
    @abstractmethod
    def to_format(self, pets):
        pass

    @abstractmethod
    def from_format(self, data):
        pass
