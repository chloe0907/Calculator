import pytest


class TestSearch:

    def test_search1(self, login):
        print("search1")

    def test_search2(self, login):
        print("search2")

    @pytest.fixture()
    def fun(self):
        print("这是另外一个fixture")

    # 参数化结合 fixture使用
    # 情况1：传入值 和 数据
    # 情况2：传入一个fixture方法，将数据传入fixture方法中，fixture方法使用request参数来接受这组数据，在方法体重使用 request.param 来使用这个数据

    @pytest.mark.parametrize('login', [
        ('username', 'password'),
        ('username1', 'password1')
    ], indirect=True)
    @pytest.mark.parametrize('a, b', [
        (1, 2),
        (3, 4)
    ])
    def test_search3(self, login, fun, a, b):
        print("search3")

    @pytest.mark.parametrize('a', [1, 2, 3])
    @pytest.mark.parametrize('b', [4, 5, 6])
    def test_data(self, a, b):
        print(a, b)

    def test_assume(self):
        pytest.assume(2 == 2)
        pytest.assume(2 == 2)
        pytest.assume(3 == 3)
