test = zip([1, 2], [3, 4])
print(list(test))

# =======================================

from typing import List
Vector = List[float]

def add(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)
    return [v_i + w_i for v_i, w_i in zip(v, w)]

test = add([1, 2, 3], [4, 5, 6])
print(test)

# =======================================

def subtract(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)
    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]