def fun():
    for i in range(3):
        print(f"i = {i}")
        # yield  相当于return，暂停并且记住上一次的执行位置
        yield
        print("end")


f = fun()
next(f)
next(f)
next(f)
