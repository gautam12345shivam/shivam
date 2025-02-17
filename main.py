# a = 45
# A = "john"
# print(A , a)

# x = 34
# a = "john"
# y = int(78)
# r = float(89)
# print(x, a, y, r) 




# MyVariableName = "John"
# x = MyVariableName
# print(MyVariableName)

# unpack a collection

# fruits = ["apple","banana","mango"]
# x,y,z = fruits
# print(x)
# print(y)
# print(z)

# a = ("good")
# print(type(a))

# x, y, z = "one","two","three"
# print(x)
# print(y)
# # print(z)

# x = y = z = "good"
# print(x)
# print(y)
# print(z)

# fruits = {"apple","banana","mango"}
# x, y, z = fruits

# print(type(fruits))

# print(x,y,z)

# for i in range(5):
#     print(i)

# Create a bytearray with initial data
# data = bytearray(b"Hello")

# # Modify the bytearray
# data[0] = ord('h')  # Change the first letter to lowercase 'h'

# # Append new data to the bytearray
# data.append(ord('a'))  # Add an exclamation mark at the end

# # Print the modified bytearray
# # pata)  # Output: bytearray(b'hello!')


# print("Hey", 6, 7, sep="~", end="089\n")
# print("Herry")

# print("this is a simple language of progamming please do

# x = "Hello world"
# print(x[0:5])
# x = "Hello World"
 # print(x.replace("World", "python"))
x = 5.3
# c = 7
# z = x+c
# print(z)

# x = 567
# print(float(x))
def process_value(value):
    if isinstance(value, int):
        print(f"Processing an integer: {value * 2}")
    elif isinstance(value, str):
        print(f"Processing a string: {value.upper()}")
    else:
        print(f"Unsupported type: {type(value)}")

# process_value(5)       # Processing an integer: 10
# process_value("hello") # Processing a string: HELLO
# process_value(3.14)    # Unsupported type: <class 'float'>

class Animal:
    pass

class Dog(Animal):
    pass
class Fruit:
    pass
class Apple(Fruit):
    pass
# print(issubclass(Apple,Fruit))  # True,Apple is a subclass of Fruit
# print(issubclass(Dog, Animal))  # True, Dog is a subclass of Animal
# print(issubclass(Animal, Dog))  # False, Animal is not a subclass of Dog

x = 10
print(isinstance(x, int))  # True, since x is an integer

y = 3.14
print(isinstance(y, float))  # True, since y is a float

z = "Hello"
print(isinstance(z, str))  # True, since z is a string

# Check if a variable is an instance of a specific class or a subclass
class Animal:
    pass

class Dog(Animal):
    pass

a = Dog()
print(isinstance(a, Animal))  # True, because Dog is a subclass of Animal
