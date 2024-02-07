
def test_arithmetic_operations():
    print("This is a test.")
    assert 100 + 1000 == 1100
    assert 100 - 1000 == -900
    assert 100 * 1000 == 100000
    assert 100 / 1000 == 0.1


def test_division():
    assert 100 / 1000 == 0.2, "This will not pass the test."


def test_integer_truncating_division():
    assert 110 // 1000 == 0
    assert 999 // 1000 == 0