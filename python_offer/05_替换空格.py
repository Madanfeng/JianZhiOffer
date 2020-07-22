"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
示例 1：
    输入：s = "We are happy."
    输出："We%20are%20happy."
限制：
    0 <= s 的长度 <= 10000
"""


def replaceSpace(s):
    """
    创建另一个新的字符串
    :param s: str
    :return: str
    """
    res = ""
    for i in s:
        if i == " ":
            res += "%20"
        else:
            res += i
    return res


def replaceSpace_2(s):
    """

    :param s: str
    :return: str
    """
    return s.replace(" ", "%20")


def replaceSpace_(s):
    # 二刷
    # 思路： 依次遍历
    res = ""
    for i in s:
        if i == " ":
            res += "%20"
        else:
            res += i
    return s

    # 思路二， python内置replace库
    # return s.replace(" ", "%20")



s = "We are happy."
print(replaceSpace(s))
