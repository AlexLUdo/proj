import math

def test_filter():
    assert list(filter(lambda x: x >= 8, [1, 5, 15, 10, 20, 8])) == [15, 10, 20, 8]

def test_map():
    assert list(map(int, ['1', '2', '3', '4', '5'])) == [1, 2, 3, 4, 5]

def test_sorted():
    assert sorted([5, 2, 6, 7, 1, 1, 5]) == [1, 1, 2, 5, 5, 6, 7]

def test_pi():
    assert round(math.pi, 2) == 3.14

def test_sqrt():
    assert math.sqrt(9) == 9 ** 0.5

def test_pow():
    assert math.pow(4, 5) == 4 ** 5

def test_hypot():
    assert math.hypot(7, 8) == math.sqrt(8*8 + 7*7)
