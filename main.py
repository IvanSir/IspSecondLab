from Serializer import Serializer
import inspect

first_global = 3.14
second_global = 16
multiplier = 3


class Figure:
    name = "circle"

    def __init__(self, name):
        self.name = name
        self.radius = 5
        self.samples = ["prosto", "test", 1, 2, "rabotaet"]

    def square(self):
        return first_global * self.radius ** 2


def summing(a, b):
    res = a + b + second_global
    answer = f"Summing is {res}"
    return answer


def inc_sort(mas):
    for i in range(len(mas)):
        mas[i] += 1
    mas.sort()
    return mas


def calculate(rad):
    print("Now Harder")
    circ = Figure("little circle")
    circ.radius = rad
    squar = circ.square()
    differ = second_global

    def square_diff(square, difference):
        return square - difference

    difs = triple(square_diff(squar, differ))
    return summing(difs, circ.radius)


triple = lambda x: x * multiplier

circle = Figure("circle")
circle.radius = 12

json_seria = Serializer.create_serializer("JSON")
pickle_seria = Serializer.create_serializer("PICKLE")
toml_seria = Serializer.create_serializer("TOML")
yaml_seria = Serializer.create_serializer("YAML")
