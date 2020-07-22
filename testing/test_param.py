# datas = [(1,2,3), (0.1, 0.4, 0.5)]
# myids = ["整数", "浮点数"]
import yaml

with open("../datas/param.yml") as f:
    datasdict = yaml.safe_load(f)

    # myids datas要与conftest函数里面的metafunc.module.datas metafunc.module.myids中保持一致
    datas = datasdict.values()
    myids = datasdict.keys()


# param要与conftest里面处理的param保持一致
def test_param(param):
    print(param)
    print("动态生成测试用例")
