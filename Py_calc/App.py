import PyCalcCore
import PyCalcCore.AddOperation
import PyCalcCore.ArithmeticBase
import PyCalcCore.SubtractionOperation
from typing import List
from Util import TypeUtil
from Util import GetHomePage


class App:

    def __init__(self):
        self.__operation = list()
        self.__operation.append(
            PyCalcCore.SubtractionOperation.SubtractionOperation())
        self.__operation.append(PyCalcCore.AddOperation.AdditionOperation())

    def Run(self):

        token = True
        App.SaveAHtmlPage()
        while (token):
            operation = self.PreferedOperation(operations=self.__operation)
            val1 = input("Enter number 1 :")
            val1 = TypeUtil.EnsureInt(val1)
            val2 = input("Enter number 2 :")
            val2 = TypeUtil.EnsureInt(val2)
            print(
                f"{operation.MetaInfo()} value is {operation.PerFormArithmetic(num1=val1, num2=val2)}")

    def PreferedOperation(cls, operations: list[PyCalcCore.ArithmeticBase.ArtihmeticBase]) -> PyCalcCore.ArithmeticBase.ArtihmeticBase:

        for i, operation in enumerate(operations):
            print(f"{i + 1} . {operation.MetaInfo()}")

        val = input("Type index of Opeartion :")
        val = TypeUtil.EnsureInt(value=val)
        return operations[val]

    def SaveAHtmlPage():
        page = GetHomePage.GetHomePage().GetHomePage()

        with open("Home.html", "wb") as file:
            file.write(page)
