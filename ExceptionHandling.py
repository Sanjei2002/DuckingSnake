

try:
    value = int(input("enter a number"))
# in C# multiple exception handling occurs in mutiple catch , here it can be multipl catch block or one catch block
except (ValueError, ZeroDivisionError) as ex:
    print(ex)
else:  # like for-else bock else will be executed if no exception is thrown
    print("Exception not thrown")
finally:
    print("Finally Block")
# finally block

# in C# dispobale can be used in Using block likewise in Python with block
# like multipe catch block multiple disposable can be used
with open("ExceptionHandling.py") as file, open("anotherFile.txt") as anotherFile:
    print("File OPened")

if value == 5:
    raise ValueError("Error")
