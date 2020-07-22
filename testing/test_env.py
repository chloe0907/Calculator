# 测试用例通过穿日fixture方法，获取测试数据/开发数据
def test_case(cmdoption):
    print("测试环境验证")
    env, datas = cmdoption
    print(f"环境{env}， 数据{datas}")
    ip = datas['env']['ip']
    port = datas['env']['port']
    url = "http://" + ip + ':' + str(port)
    print(url)
