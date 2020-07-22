import sys

import allure
import pytest

print(sys.path.append('D:\\PycharmProjects\\Calculator'))
from pythoncode.calc import Calculator
import yaml
import math


# def setup_module():
#     print("模块级别setup")
#
#
# def teardown_module():
#     print("模块级别teardown")
#
#
# def setup_function():
#     print("函数级别setup")
#
#
# def teardown_function():
#     print("函数级别teardown")
#
#
# def test_abc():
#     print("被测试函数")

@allure.feature("计算器")
class TestCalc:

    def setup_class(self):
        self.cal = Calculator()
        # print("类级别setup")

    # def teardown_class(self):
    #     print("类级别teardown")
    #
    # def setup(self):
    #     print("方法级别setup")
    #
    # def teardown(self):
    #     print("方法级别teardown")

    @allure.story("加法")
    @pytest.mark.flaky(reruns=5, reruns_delay=1)
    @pytest.mark.parametrize('a, b, result', yaml.safe_load(open("../datas/add.yaml")), ids=['整数', '浮点数', '负数', '大整数'])
    @pytest.mark.add
    def test_add(self, calc, a, b, result):
        # cal = Calculator()
        assert result == self.cal.add(a, b)

    with open("../datas/div.yaml") as f:
        # print(f)
        datas = yaml.safe_load(f)
        # print(datas)
        myids = datas.keys()
        mydata = datas.values()
        print(mydata)

    @allure.story("除法")
    @pytest.mark.parametrize('a, b, result', mydata, ids=myids)
    @pytest.mark.div
    def test_div(self, a, b, result):
        # cal = Calculator()

        assert result == self.cal.div(a, b)

    @allure.story("减法")
    @pytest.mark.parametrize('a, b, result', yaml.safe_load(open("../datas/sub.yaml")))
    def test_sub(self, a, b, result):
        # cal = Calculator()
        tmp = result - self.cal.sub(a, b)
        math.isclose(tmp, result)

    @allure.story("乘法")
    @pytest.mark.parametrize('a, b, result', yaml.safe_load(open("../datas/multi.yaml")))
    def test_multi(self, a, b, result):
        # cal = Calculator()
        assert result == self.cal.multi(a, b)
