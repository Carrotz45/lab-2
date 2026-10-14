import math
from model import *



vec_xy = [(1,1), (1,2)]

def assert_equal(object, attr, result, *input):
    print(result)
    print(f"trying method: {attr}, with input: {input} on object: {object}")
    method = getattr(object, attr)

    if str(input) != "()":
        compare = method(input[0])
    else:
        compare = method()

    if compare == result:
        print("pass")
    else:
        print(f"got: {compare}, expected: {result}")
        print("fail")


for x, y in vec_xy:
    init_vec = Vec(x, y)
    assert_equal(init_vec, '__repr__', f"({x}, {y})")
    assert_equal(init_vec, '__rmul__', ((x*4), (y*4)), 4)


