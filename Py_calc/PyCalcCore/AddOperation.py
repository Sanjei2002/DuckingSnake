from PyCalcCore.ArithmeticBase import ArtihmeticBase
from Util.TypeUtil import EnsureInt


class AdditionOperation(ArtihmeticBase):

    def PerFormArithmetic(self, num1: int, num2: int) -> int:
        EnsureInt(num1)
        EnsureInt(num2)
        return num1 + num2

    def MetaInfo(self) -> str:
        return "Addition"
