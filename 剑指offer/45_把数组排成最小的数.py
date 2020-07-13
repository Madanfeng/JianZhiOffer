"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

示例 1:
    输入: [10,2]
    输出: "102"
示例 2:
    输入: [3,30,34,5,9]
    输出: "3033459"

提示:
    0 < nums.length <= 100
说明:
    输出结果可能非常大，所以你需要返回一个字符串而不是整数
    拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0
"""


def minNumber(nums):
    """

    :param nums: List[int]
    :return: str
    """
    def fast_sort(l, r):
        if l >= r: return
        i, j = l, r
        while i < j:
            while strs[j] + strs[l] >= strs[l] + strs[j] and i < j: j -= 1
            while strs[i] + strs[l] <= strs[l] + strs[i] and i < j: i += 1
            strs[i], strs[j] = strs[j], strs[i]
        strs[i], strs[l] = strs[l], strs[i]
        fast_sort(l, i - 1)
        fast_sort(i + 1, r)

    strs = [str(num) for num in nums]
    fast_sort(0, len(strs) - 1)
    return ''.join(strs)


print(minNumber([1,2,10]))
