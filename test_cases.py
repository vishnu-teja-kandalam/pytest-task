from basicmath.util import add_num, sub_num, mul_num, div_num


class TestClass:
    ''' Class for testing four operations'''
    def test_function_add(self):
        '''method for addition'''
        assert add_num(10,20) == 30

    def test_function_sub(self):
        '''method for substraction'''
        assert sub_num(20,10) == 10

    def test_function_mul(self):
        '''method for multiplication'''
        assert mul_num(2,2)==4

    def test_function_div(self):
        '''method for division'''
        assert div_num(15,5)==3
