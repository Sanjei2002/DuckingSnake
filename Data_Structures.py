# Lists

from sys import getsizeof
from array import array
from collections import deque
letters = ["a", "b"]

list_of_list = [[0, 1], [2, 3]]

list_of_hundred_zers = [0] * 10

# two list can be concatineted using siple plus
combined = letters + list_of_hundred_zers

# also list can be created using list method which taes iterable
even_numbers = list(range(2, 50, 2))
print(even_numbers)

string_list = list("Hellow World")
print(f"string is a iterable can be converted into list {string_list}")
print(f"Length of the list is found using len {len(string_list)}")

print(combined)

# Opeartio in list

# indexing is supported in lists

letters = ['a', 'b', 'c', 'd']

print(
    f"indexing is supported {letters[0]} , like substring list can be sliced {letters[0:4:2]} ,reverse a list using negative stepper {letters[::-1]}")

# unPacking list
numbers = [1, 2, 3, 4, 5, 6, 78, 9]

# legacy unpacking
first = numbers[0]
second = numbers[1]
third = numbers[2]

# unpacking is much simpler
# overlown items are assigned to nre list
first, second, third, *extralist = numbers

print(f"obects from the list are automaticaaly assigned to varibled  number of item on list and varible should be same , else we can use repack items")

# looping over list

numbers = list(range(100))

print(f"for can be used for enumrating the list , also enumurate method returs a object which supports indexing while traversing")

for index, num in enumerate(numbers, start=0):
    print(f"index {index} number is {num}")

# adding / removing items in a list
letters.append("letter")
letters.insert(0, "first letter")
print(letters)

# Rmove
letters.pop()  # default lastindex,remove only one item
letters.remove("b")  # looks for a value i the list and deletes the item
del letters[0:2]  # remove multipe items
print(letters)

letters.clear()  # removes everything

# finding object in a list

numbers.count(3)  # returns number of elements in the list
if 3 in numbers:
    print("3 is in the list")
    print(
        f"index of an elemnt can be fetch by indexof method {numbers.index(3)}")

# sroting list

num = [99, 43, 65, 32, 6565, 54]
# also have build in sort method
print(f"sort {num.sort()} sort in reverse {num.sort(reverse=True)} , also sort using build in Sorted method returns new sorted list = {sorted(num)}")

# to sort complex object a Func like method is passed to it

# lamda in pyton
# systanx is lamda parameter:exression
num.sort(key=lambda item: item)
print(num)

# Set
hasSet = set()


items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# Transform this list of tupple into list o numbers
prices = []
for item in items:
    prices.append(item[1])

print(prices)
for value in map(lambda item: item[1], items):
    print(value)

# filter Function
filtered = filter(lambda item: item[1] == 9, items)
print(list(filtered))


print("map and filter can be written in a single line using list comprehension")
# define list [expresiion for item in items ]
filtered2 = [item[1] for item in items if item[1] == 9]
print(filtered2)

# zip function
list1 = [10, 20, 30, 40]
list2 = [40, 50, 60]

print(list(zip("sanjei", "Pranav", list1, list2)))


# Stacks
print(f"stack no separate data structure in phyton list's appended and Pop is used here")
list_as_stack = ["a", "b", "c"]
list_as_stack.append("b")
list_as_stack.pop()
list_as_stack.append(76)
print(f"last index is fetched using -1")

# Queue
print(f"queue implementation in python is implemented using dequeue class from collections module")

fifo = deque([12, 54, 76, 235, 545])
fifo.popleft()  # first elemnt gets removed

# Tupples
# readonly list

# number seprated by comma is tupple
example3 = 4, 6, 2, 5  # its a tupple
print(type(example3))
example_tupple = (10, 20, 30, 40, 50) * 10
example_tupple = (10, 20, 30, 40, 50) + (12, 43, 243, 54, 65)
example_tupple[0: 4: 1]
print(example_tupple)

# swapping varibles

# legacy method
x = 10
y = 20

z = x
x = y
y = z

# python tupple unpackinng method
x, y = y, x  # tupple is unpacked into these varibles
print("x= ", x)
print("Y =", y)

# Arrays
# array collection is list with strictly typed

example_array = array("i", [32, 43, 54, 454, 2323])
# array is sued in case of lareg data set and perfromace optimization

# Sets

# Stores Unique items , and unorderes indexing cannot be used

numbers = [10, 20, 30, 10, 40]
unique_numbers_1 = set(numbers)
print("set can only have unique numebrs", unique_numbers_1)
unique_numbers_2 = {20, 30, 70, 90}

print(F"union between two set : |  {unique_numbers_1 | unique_numbers_2}")
print(
    F"Intersection between two set : &  {unique_numbers_1 & unique_numbers_2}")
print(
    F"differnce between two set : - subracts matching elements from set 2  {unique_numbers_1 - unique_numbers_2}")
print(
    F"symmetric diff  between two set : ^ unions them and remove mathing elements  {unique_numbers_1 ^ unique_numbers_2}")


# Dictionaries
# immutable types can only be used as key
example_dicationary = {"name1": 43434, "name4": 54242}
example_dic2 = dict()


point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
# checking if element is in dictionary collection
if "a" in point:
    print(point["a"])
print(point.get("a", 0))

# removing a element from dictionary
del point["x"]
print(point)
for key, value in point.items():
    print(key, value)

# dictioanry comprehension

even_numbers = [num * 2 for num in range(10)]
# set comprehension
set_comprehension = {num * 2 for num in range(10)}
# difference between set and dictory is key and vaue colon :

# dictionary comprehension
dic_comprehension = {num: num*2 for num in range(50)}

print(
    f"list comprehenion {even_numbers} set_comprehension {set_comprehension}   ditionary_Compre {dic_comprehension}")

# Generator expression
# there like enumrator in C# gives values only when needed
genenrator_obj = (num*2 for num in range(50))


print("generator object size=", getsizeof(genenrator_obj))


# unpacking Opaertor
# **
