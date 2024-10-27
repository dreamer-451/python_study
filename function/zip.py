# zip()
# 参数为可迭代对象（list，str，dict，tuple等)，数量为一个或多个
# 将参数中的对应元素打包为元组，以列表类型返回打包的元组，即压缩
# 若使用 * 操作符操作参数，则将列表中各元组作为参数进行zip，即解压缩
# 注意：
# 【1】python3 中 zip() 返回一个对象，如需访问其中内容，需自行进行 list() 转换
# 【2】参数为多个时，若多个参数包含的元素个数不同，返回的列表长度与最短对象相同
# 【3】zip(*) 解压缩，也是调用 zip()，返回的同样是元组序列组成的列表对象
# 【4】用 zip(*) 解压缩时，若将返回的结果赋予与结果的子序列数量相同的结果列表，则各结果列表分别存储一个子序列，且返回内容无需转换，字符串、字典等除外

import sys


def print_help():
    print("zip()")
    print("参数为可迭代对象（list，str，dict，tuple等)，数量为一个或多个")
    print("将参数中的对应元素打包为元组，以列表类型返回打包的元组，即压缩")
    print("若使用 * 操作符操作参数，则将列表中各元组作为参数进行zip，即解压缩")
    print("注意：")
    print("【1】python3 中 zip() 返回一个对象，如需访问其中内容，需自行进行 list() 转换")
    print("【2】参数为多个时，若多个参数包含的元素个数不同，返回的列表长度与最短对象相同")
    print("【3】zip(*) 解压缩，也是调用 zip()，返回的同样是元组序列组成的列表对象")
    print("【4】用 zip(*) 解压缩时，若将返回的结果赋予与结果的子序列数量相同的结果列表，则各结果列表分别存储一个子序列，且返回内容无需转换，字符串、字典等除外\n")

def learn_zip():
    print("压缩zip()")

    # 长度相等列表作为参数
    a = [0, 1, 2]
    b = [3, 4, 5]
    zip_ab = zip(a, b)
    zipped_ab = list(zip_ab)
    print(f"长度相等列表zip\n列表参数1：{a}\n列表参数2：{b}\nzip()返回：{zip_ab}\nzip()结果：{zipped_ab}\n")

    # 长度相等元组作为参数
    c = (0, 1, 2)
    d = (3, 4, 5)
    zip_cd = zip(c, d)
    zipped_cd = list(zip_cd)
    print(f"长度相等元组zip\n元组参数1：{c}\n元组参数2：{d}\nzip()返回：{zip_cd}\nzip()结果：{zipped_cd}\n")

    # 长度相等字符串作为参数
    e = "abc"
    f = "def"
    zip_ef = zip(e, f)
    zipped_ef = list(zip_ef)
    print(f"长度相等字符串zip\n字符串参数1：{e}\n字符串参数2：{f}\nzip()返回：{zip_ef}\nzip()结果：{zipped_ef}\n")

    # 长度相等字典作为参数
    g = {'a': 0, 'b': 1, 'c': 2}
    h = {'d': 3, 'e': 4, 'f': 5}
    zip_gh = zip(g, h)
    zipped_gh = list(zip_gh)
    print(f"长度相等字典zip\n字典参数1：{g}\n字典参数2：{h}\nzip()返回：{zip_gh}\nzip()结果：{zipped_gh}\n")

    # 长度不等列表作为参数
    i = [6, 7, 8, 9]
    zip_ai = zip(a, i)
    zipped_ai = list(zip_ai)
    print(f"长度不等列表zip\n列表参数1：{a}\n列表参数2：{i}\nzip()返回：{zip_ai}\nzip()结果：{zipped_ai}\n")

    # 长度不等元组作为参数
    j = (6, 7, 8, 9)
    zip_cj = zip(c, j)
    zipped_cj = list(zip_cj)
    print(f"长度不等元组zip\n元组参数1：{c}\n元组参数2：{j}\nzip()返回：{zip_cj}\nzip()结果：{zipped_cj}\n")

    # 长度不等字符串作为参数
    k = "ghij"
    zip_ek = zip(e, k)
    zipped_ek = list(zip_ek)
    print(f"长度相等字符串zip\n字符串参数1：{e}\n字符串参数2：{k}\nzip()返回：{zip_ek}\nzip()结果：{zipped_ek}\n")

    # 长度不等字典作为参数
    l = {'g': 6, 'h': 7, 'i': 8, 'j': 9}
    zip_gl = zip(g, l)
    zipped_gl = list(zip_gl)
    print(f"长度不等字典zip\n字典参数1：{g}\n字典参数2：{l}\nzip()返回：{zip_gl}\nzip()结果：{zipped_gl}\n")

    # 长度相等类型不同参数
    print("长度相等类型不同zip")

    zip_ij = zip(i, j)
    zipped_ij = list(zip_ij)
    print(f"列表参数：{i}\n元组参数：{j}\nzip()返回：{zip_ij}\nzip()结果：{zipped_ij}")

    zip_ik = zip(i, k)
    zipped_ik = list(zip_ik)
    print(f"列表参数：{i}\n字符串参数：{k}\nzip()返回：{zip_ik}\nzip()结果：{zipped_ik}")

    zip_il = zip(i, l)
    zipped_il = list(zip_il)
    print(f"列表参数：{i}\n字典参数：{l}\nzip()返回：{zip_il}\nzip()结果：{zipped_il}")

    zip_jk = zip(j, k)
    zipped_jk = list(zip_jk)
    print(f"元组参数：{j}\n字符串参数：{k}\nzip()返回：{zip_jk}\nzip()结果：{zipped_jk}")

    zip_jl = zip(j, l)
    zipped_jl = list(zip_jl)
    print(f"元组参数：{j}\n字典参数：{l}\nzip()返回：{zip_jl}\nzip()结果：{zipped_jl}")

    zip_kl = zip(k, l)
    zipped_kl = list(zip_kl)
    print(f"字符串参数：{k}\n字典参数：{l}\nzip()返回：{zip_kl}\nzip()结果：{zipped_kl}")

    # 长度不等类型不同参数
    print("\n长度不等类型不同zip")

    zip_aj = zip(a, j)
    zipped_aj = list(zip_aj)
    print(f"列表参数：{a}\n元组参数：{j}\nzip()返回：{zip_aj}\nzip()结果：{zipped_aj}")

    zip_ak = zip(a, k)
    zipped_ak = list(zip_ak)
    print(f"列表参数：{a}\n字符串参数：{k}\nzip()返回：{zip_ak}\nzip()结果：{zipped_ak}")

    zip_al = zip(a, l)
    zipped_al = list(zip_al)
    print(f"列表参数：{a}\n字典参数：{l}\nzip()返回：{zip_al}\nzip()结果：{zipped_al}")

    zip_ck = zip(c, k)
    zipped_ck = list(zip_ck)
    print(f"元组参数：{c}\n字符串参数：{k}\nzip()返回：{zip_ck}\nzip()结果：{zipped_ck}")

    zip_cl = zip(c, l)
    zipped_cl = list(zip_cl)
    print(f"元组参数：{c}\n字典参数：{l}\nzip()返回：{zip_cl}\nzip()结果：{zipped_cl}")

    zip_el = zip(e, l)
    zipped_el = list(zip_el)
    print(f"字符串参数：{e}\n字典参数：{l}\nzip()返回：{zip_el}\nzip()结果：{zipped_el}")


def learn_zip_star():
    print("解压缩zip(*)")

    # 长度相等子序列的列表作为参数
    print("长度相等子列表zip*")
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"列表参数：{a}")
    for i in range(3):
        print(f"参数子序列{i + 1}：{a[i]}")
    zip_a = zip(*a)
    zipped_a = list(zip_a)
    print(f"zip(*)返回：{zip_a}\nzip(*)结果：{zipped_a}")
    a_1, a_2, a_3 = zip(*a)
    print(f"结果子序列1：{a_1}\n结果子序列2：{a_2}\n结果子序列3：{a_3}\n")

    # 长度相等子序列的元组作为参数
    print("长度相等子元组zip*")
    b = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    print(f"元组参数：{b}")
    for i in range(3):
        print(f"参数子序列{i + 1}：{b[i]}")
    zip_b = zip(*b)
    zipped_b = list(zip_b)
    print(f"zip(*)返回：{zip_b}\nzip(*)结果：{zipped_b}")
    b_1, b_2, b_3 = zip(*b)
    print(f"结果子序列1：{b_1}\n结果子序列2：{b_2}\n结果子序列3：{b_3}\n")

    # 长度相等子序列的字符串作为参数
    print("长度相等子字符串zip*")
    c = "abc"
    print(f"字符串参数：{c}")
    for i in range(3):
        print(f"参数子序列{i+1}：{c[i]}")
    zip_c = zip(*c)
    zipped_c = list(zip_c)
    print(f"zip(*)返回：{zip_c}\nzip(*)结果：{zipped_c}")
    c_1 = zip(*c)
    c_1 = list(c_1)
    print(f"结果子序列1：{c_1}\n")

    # 长度相等子序列的字典作为参数
    print("长度相等子字典zip*")
    d = {'a': 1, 'b': 2}
    print(f"字典参数：{d}")
    temp = list(d.items())
    for i in range(2):
        print(f"参数子序列{i + 1}：{temp[i]}")
    zip_d = zip(*d)
    zipped_d = list(zip_d)
    print(f"zip(*)返回：{zip_d}\nzip(*)结果：{zipped_d}")
    d_1 = zip(*d)
    d_1 = list(d_1)
    print(f"结果子序列1：{d_1}\n")


if __name__ == '__main__':
    sys.stdout = open('learn_zip.log', mode ='w', encoding ='UTF-8')
    print_help()
    learn_zip()
    learn_zip_star()
