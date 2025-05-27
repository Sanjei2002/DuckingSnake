# Variables

import math
student_count = 1000  # int
raing = 4.99  # float
is_even = False  # bool
some_string = "It is string Varable"  # string

# string in multiple line can be written using three doube quotes
multiple_line_string = """
string in
multiple lines
"""

# varible assignments

# 1

x, y = 10, 20

print("x values is ="+str(x))
print("Y value is =" + str(y))

# 2

z = w = 10  # channed assignment

print("Z value is "+str(z))
print("w value is "+str(w))


# Python Dynamically typed

print("Type is = "+str(type(student_count)))


# Type Annotation
# provide a way to specify the expected data types of variables, function parameters, and return values
age: int = 20
age = "eight"
print(age)

# mutble and Immutable types
number = 1  # intrepretor allocates some meory to store number 1

print("int , string , float are Immutbale ,  address of number varible "+str(id(number)))
number = number+1
print("address of number + 1 varible "+str(id(number)))

print("List are immutable changes takes place at same eory location")


# Strings

word = "Its a Long LEtter"

print("Length of the word using Len() functio len takes Object param : "+str(len(word)))
print("fetching char using indexer is allowed in python : "+str(word[8]))
print("using negative index in a Indexer willow not throw out of bounds instead cyclic postion is returned " +
      str(word[-1]))
print(
    "substring can fetched using two index in a same bracket [0 : 5 ]  = "+str(word[0:5]))


# Escape Sequence

message = "Pyton \" Programming"

print("escape charector is supported in Pyton , string also written with single squote ' "+message)


# String Formating

# append f to a string

exampleForating = f""" In Pyhton String foramting is done using appending {"f"} to the starting of the string , whereas in C# it is  {"$"}  """
print(exampleForating)


# String Methods
print(f"""String Strip is used to trim White spaces = {exampleForating.strip()} / .lower {exampleForating.lower()} / 
      in & not in Opeartor : checaks if the word(object) is in Collection  {"Pyton" in message}""")


# numbers

x = 10  # decimal
num2 = 0b1000  # bindary
num3 = 0x10  # Hexa Decimal
print(
    f"""bin method accepts a number and returns binary eqialent 10 : {bin(x)} to print Hexa decimal Hex method {hex(num2)}    |  {num2} """)

# complex number in pyhton i prespresnted in a + bi
complexNumber = 2 + 5j
print(f"Complex Number in pyton can be used {complexNumber}")


# Arithmatic operator

print(f"addition {10 + 10} Sub  {10-10} mul = {10 * 3} there are two divion operator / (retuns decimal value)and //(returns real number part only) / =  {10/3} // = {10//3} modulus returns remainder  {10 % 3}  exponenet left to the power of right {10 ** 10}  alos supports += operator | no incement or decrement operator")

# Python there in No Constant keywork like Pyton

PI = 3.14  # naming convention suggest us that PI cannot be modified
print(
    f"""round with give round to its nearest value {round(PI)} absoulte {abs(PI)}   , for extra math operation Math module should be imported""")


print(f"floor of 5.9 is {math.floor(5.9)}")


# Type Convertions in Python
print(f"Pyton is Dynamically typed but aos stringly typed , so implict type casting during opeartion is not supported for that we use int(),float(),bool(),str()")
number1 = input("Give me a Number : ")
number2 = 20
# number2 = number1 + number2 #causes Runtime error
print(f"number2 = int(number1) + number2 {int(number1) + number2}")

# falsy
# ""  , 0 , [] , None() , null


# COnditional Statements If
age = 25

if age >= 18:
    print("valid")
else:
    print("nah pdf file")
    pass
# empty blocks are not allowed so pass keyword is used to indentify epty block

  # logical Keyword
  # and
  # or
  # not

  # string.IsNullOrErtyOrWhiteSPace  can be replace with if not word.strip()  using truthy falsy concept here

print("python support chainned comparison operator")

if not 18 < age < 30:
    print('Chainned condition is usd here')
else:
    pass


# trenay operator in C# it is  ? :
message = "valid" if age > 18 else "pass"

print("ternary oeator in python is [value][if (condition) else] [value2]")

# forloop anf While

for char in message:
    print(char)

for x in ['a', 'b']:
    print(x)

print(
    f""" in c# we use for(int i=o;i<10;i++) but here iterable range object is used range(start, stop,range) {range(0, 10, 2)} """)

for number in range(0, 10, 1):
    print(number)


# For else

# names = ["AJohn", "Mary"]
# found=False
# for name in names:
#     if name.startswith("J"):
#         print("Found")
#         found = True
#         break
# if not found:
#     print("Not found")
print("In pyhton there is conceprt called For..rlse if a iterabel not breaks else bock will be executed")
names = ["AJohn", "Mary"]
for name in names:
    if name. startswith("J"):
        print("Found")
        break
else:
    print("Not found")


# while loop

print("while is same as C# while <bool> while:else also excutes if while completes without using break statement")

# Funtions


def funtion_name(number: int, by: int = 7) -> str:
    return number + by


print(funtion_name(number=5, by=7))

# args


def multiply(*arguments: int) -> int:
    returnvalue = 1
    for value in arguments:
        returnvalue *= value
    else:
        return returnvalue


print(f"arg eyword in python is replace using *  {multiply(34, 76, 325, 56)}")

# key value arguments


def save_user(** user):
    print(user["id"])


save_user(id=1, name="admin")

print("IN pUTHON THERE IS NO blOCK LEVEL SCOPES")


def fizz_buzz(number: int = 0) -> str:
    if (number % 3 == 0) and (number % 5 == 0):
        return "fizz_buzz"
    elif not number % 3:
        return "fizz"
    elif not number % 5:
        return "buzz"

    return number


print(
    f"fizzBuzz = 5 : {fizz_buzz(5)} | 10 : {fizz_buzz(10)} | 60 : {fizz_buzz(60)} | 52 : {fizz_buzz(52)}")
