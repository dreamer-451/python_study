from itertools import permutations


# permutations()
# 返回序列的全排列
def learn_permutations():
    seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    result1 = permutations(seq, 2)
    result1 = list(result1)
    print(result1)
    result2 = permutations(seq, 3)
    result2 = list(result2)
    print(result2)
    result3 = permutations(seq, 5)
    result3 = list(result3)
    print(result3)


if __name__ == '__main__':
    # 测试 permutations()
    learn_permutations()
