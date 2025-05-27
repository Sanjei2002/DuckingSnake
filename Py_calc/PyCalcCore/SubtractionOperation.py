from PyCalcCore.ArithmeticBase import ArtihmeticBase
from Util import TypeUtil


class SubtractionOperation(ArtihmeticBase):

    def PerFormArithmetic(self, num1: int, num2: int) -> int:
        TypeUtil.EnsureInt(num1)
        TypeUtil.EnsureInt(num2)
        return num1 - num2

    def MetaInfo(self) -> str:
        return "Substraction"
