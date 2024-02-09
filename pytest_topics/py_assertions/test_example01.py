def test_inequality():
    assert 5 > 4
    assert 3 < 4
    assert 4 != 3


def test_return_passed():
    assert 1


def test_return_failed():
    assert 0


def test_true():
    assert True


def test_false():
    assert False

def test_string():
    assert "abc" == 'abc'

def test_divmod_passed():
    assert 1 in divmod(9,5)

def test_divmod_failed():
    assert 9 in divmod(9, 5)