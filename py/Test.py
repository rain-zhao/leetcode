def f1():

    n = 1

    def f2():

        n = n + 1

        return n

    return f2


res = f1()

print(res())   # 2
