"""
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

示例 1:
    输入: "abcabcbb"
    输出: 3
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
    输入: "bbbbb"
    输出: 1
    解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:
    输入: "pwwkew"
    输出: 3
    解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
         请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
提示：
    s.length <= 40000
"""


def lengthOfLongestSubstring(s):
    """

    :param s: str
    :return: int
    """
    if s is None:
        return 0
    left, right = 0, 0
    res = 0
    temp = 0
    while right < len(s):
        if s[right] not in s[left:right]:
            right += 1
            temp += 1
            res = max(res, temp)
        else:
            i = left
            while s[i] != s[right]:
                i += 1
            left = i + 1
            temp = right - left
    return res


print(lengthOfLongestSubstring(""))

