
# defined Human class.
import math


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"


humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = []
for human in humans:
    if human.name[0].lower() == 'd':
        a.append(human.name)
print(a)

# a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = []
for human in humans:
    if human.name[-1].lower() == 'e':
        b.append(human.name)
print(b)

# a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = []
for human in humans:
    if 'c' <= human.name[0].lower() <= 'g':
        c.append(human.name)
print(c)

# a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [human.age + 10 for human in humans]

print(d)

#  a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [(f'{human.name}-{human.age}') for human in humans]
print(e)

# a list comprehension that creates a list of tuples containing name and

print("Names and ages between 27 and 32:")
f = [(human.name, human.age) for human in humans if 27 <= human.age <= 32]
print(f)

# a list comprehension that creates a list of new Humans like the old

print("All names capitalized:")
g = [Human(human.name.upper(), human.age + 5) for human in humans]
print(g)

# a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
h = [human.age**.5 for human in humans]
print(h)
