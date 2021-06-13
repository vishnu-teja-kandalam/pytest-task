import pytest
from basicmath.util import add_num, sub_num, mul_num, div_num


class TestClass:
    def test_function_add(self):
        assert add_num(10,20) == 30

    def test_function_sub(self):
        assert sub_num(20,10) == 10

    def test_function_mul(self):
        assert mul_num(2,2)==4

    def test_function_div(self):
        with pytest.raises(ZeroDivisionError):
            div_num(5,0)

