"""
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:
    s = "abaccdeff"
    返回 "b"

    s = ""
    返回 " "
 
限制：
    0 <= s 的长度 <= 50000
"""


def firstUniqChar(s):
    """

    :param s: str
    :return: str
    """

    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in s:
        if d[i] == 1:
            return i
    return " "


print(firstUniqChar("abaccdeff"))
