# locals()
# 以字典类型返回当前位置的全部局部变量
def learn_locals():
    a = True
    b = 0
    c = 0.1
    d = [1, 2]
    e = 'a'
    f = "abcdefg"
    g = (3, 4)
    h = {'key': 'value'}
    i = type(c)
    j = type(e)
    return locals()

def is_in():
    return 0


if __name__ == '__main__':
    # 测试 locals()
    print(learn_locals())
