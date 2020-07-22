from typing import List

import pytest

# session 是整个项目只执行一次，module是每个py文件执行一次
# autouse 是每个测试用例不写login，也会自动调用login这个方法
import yaml


@pytest.fixture(scope='class', autouse=False, params=["user1", "user2", "user3"])
def login(request):
    print("登录方法")
    print(request.param)
    yield ["username", "password"]
    print("teardown")


@pytest.fixture()
def calc():
    print("计算开始")
    yield
    print("计算结束")


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

        if 'sub' in item.nodeid:
            item.add_marker(pytest.mark.sub)

        if 'multi' in item.nodeid:
            item.add_marker(pytest.mark.multi)


def pytest_addoption(parser):
    mygroup = parser.getgroup("Hogwarts")
    mygroup.addoption("--env", default="test", dest="env", help="set your run env")


# 处理命令行传来的参数，设置为fixture，将test环境或者env环境分别处理，获取想要的环境下的测试数据

@pytest.fixture(scope="session")
def cmdoption(request):
    myenv = request.config.getoption("--env", default="test")

    if myenv == "test":
        datapath = "../datas/test/data.yml"

    if myenv == "dev":
        datapath = "../datas/dev/data.yml"

    with open(datapath) as f:
        datas = yaml.safe_load(f)

    return myenv, datas


# 通过metafunc方法获取到所有fixture中的名称，如果发现fixture中有一个参数是param，就可以通过param实现动态参数化的功能
def pytest_generate_tests(metafunc: "Metafunc") -> None:
    if "param" in metafunc.fixturenames:
        metafunc.parametrize("param",
                             metafunc.module.datas,
                             ids=metafunc.module.myids,
                             scope='function')
