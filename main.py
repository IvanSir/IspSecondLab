import inspect
from types import CodeType, FunctionType
from Serializer import Serializer
import builtins

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
    print("This is sum")
    return a + b - second_global


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

dumped_obj = json_seria.dumps(circle)
loaded_obj = json_seria.loads(dumped_obj)

# print(loaded_obj.square(loaded_obj))
# print(loaded_obj.radius)

dumped_func = json_seria.dumps(summing)
loaded_func = json_seria.loads(dumped_func)
# print(loaded_func(11, 10))

dumped_lambda = json_seria.dumps(triple)
loaded_lambda = json_seria.loads(dumped_lambda)
# print(loaded_lambda(6))

dumped_class = json_seria.dumps(Figure)
loaded_class = json_seria.loads(dumped_class)
# for i in inspect.getmembers(Figure):
#     print(i)
# print()
#
# for i in inspect.getmembers(Figure):
#     print(i)
# print()

# print(dumped_class)
# print(loaded_class)
# awe = loaded_class("qwerty")
# awe = loaded_class("auf")
# print(awe)

# print(getattr(loaded_class,"__init__"))
# print(getattr(Figure,"__init__"))


dumped_hard = json_seria.dumps(calculate)
loaded_hard = json_seria.loads(dumped_hard)
# print(loaded_hard(3))


pickle_seria = Serializer.create_serializer("PICKLE")
toml_seria = Serializer.create_serializer("TOML")
yaml_seria = Serializer.create_serializer("YAML")

# hm = yaml_seria.dumps(Figure)
# print(hm)
# opada = yaml_seria.loads(hm)
# print(opada)
# print()
# qwert = opada("kukuwka")
# qwert.radius = 2
# yaml_seria.dumps(qwert)
# obbj = yaml_seria.loads(yaml_seria.dumps(calculate))
#
# print(obbj(2))


dfunc_toml = toml_seria.dumps(loaded_func)
lfunc_toml = toml_seria.loads(dfunc_toml)
# print(lfunc_toml(1, 5))

dobj_toml = toml_seria.dumps(circle)
lobj_toml = toml_seria.loads(dobj_toml)

dclass_toml = toml_seria.dumps(Figure)
lclass_toml = toml_seria.loads(dclass_toml)

dhard_toml = toml_seria.dumps(calculate)
lhard_toml = toml_seria.loads(dhard_toml)








