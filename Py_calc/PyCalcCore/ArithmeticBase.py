from abc import ABC, abstractmethod


class ArtihmeticBase(ABC):

    @abstractmethod
    def PerFormArithmetic(self, num1: int, num2: int) -> int:
        pass

    @abstractmethod
    def MetaInfo(self) -> str:
        pass
