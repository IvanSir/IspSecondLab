from Serializer import Serializer
# import sympy as sp
# from sympy.abc import x
# polynom = sp.poly(x ** 3 - 13.3667 * (x ** 2) + 39.8645 * x - 20.6282, x)
first_global = 3.14
second_global = 16
multiplier = 3

# prim_dict = {12: "hit", 10: ["hello", "there"], 11: True, "oh": 222}

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


# def sign_changes(_poly_range_, value):
#     counter = 0
#     size = len(_poly_range_)
#     current_sgn = _poly_range_[0](value) > 0
#     for i in range(size - 1):
#         new_sgn = _poly_range_[i + 1](value) > 0
#         if new_sgn != current_sgn:
#             counter += 1
#         current_sgn = new_sgn
#     return counter
#
#
# def sturm_theorem(poly, left, right):
#     sturm_sequence = [poly, sp.diff(poly)]
#     sequence_range = sp.degree(poly, gen=x)
#     for i in range(sequence_range - 1):
#         sturm_sequence.append(-sp.div(sturm_sequence[i], sturm_sequence[i + 1])[1])
#     return sign_changes(sturm_sequence, left) - sign_changes(sturm_sequence, right)



def calculate(rad):
    # print("Now Harder")
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
