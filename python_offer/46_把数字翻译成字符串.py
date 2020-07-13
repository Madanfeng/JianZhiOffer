"""
给定一个数字，我们按照如下规则把它翻译为字符串：
0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。
请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

示例 1:
    输入: 12258
    输出: 5
    解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
 
提示：
    0 <= num < 2**31
"""


def translateNum(num):
    """

    :param num: int
    :return: int
    """

    def getNum(start):
        if start == l or start == l - 1:
            return 1
        if start > l:
            return 0
        for i in range(start, l):
            if num_str[start] >= "3" or num_str[start] == "0":
                return getNum(start + 1)
            elif num_str[start] == "2" and num_str[start + 1] >= "6":
                return getNum(start + 1)
            else:
                return getNum(start + 1) + getNum(start + 2)

    num_str = str(num)
    l = len(num_str)
    res = getNum(0)
    return res


print(translateNum(121221123))
