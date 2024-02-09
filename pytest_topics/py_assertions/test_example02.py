import pytest


def test_ex01():
    # Exception works for all exceptions, hence not useful
#    with pytest.raises(Exception):
    with pytest.raises(ZeroDivisionError):
        # Works for Exception or ZeroDivisionError
        assert (1 / 0)
        # Works for Exception or AssertionError
#        assert (3 < 3)


def test_ex02():
    with pytest.raises(Exception) as excep_info:
        assert (1, 2, 3) == (1, 2, 4)

#    print(excep_info)
    print(str(excep_info))


def func_raise_exception():
    raise ValueError("Exception raised")
#    raise ValueError("IndexError raised")


def test_ex03():
    with pytest.raises(Exception) as excep_info:
        func_raise_exception()

    print(str(excep_info))
    # .value is REQUIRED
    assert (str(excep_info.value)) == 'Exception raised'