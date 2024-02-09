class TestExample():
    def test_int_type(self):
        assert type(22) == int


    def test_float_type(self):
        assert type(22.22) == int


    def test_string_type(self):
        assert str.lower('PYTHON') == 'python'
#        assert str.lower('PYTHON') == 'Python'
        assert str.capitalize('python') == 'Python'