def add(a, b):
    return a + b

def test_add():
    assert add(1, 1) == 2
    assert add(2, 3) == 5
    assert add(-1, 1) == 0