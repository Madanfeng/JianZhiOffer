"""
不修改数组找出数组中重复的数字。
在一个长度为 n+1 的数组里的所有数字都在 1~n 的范围内，所以数字中至少有一个数字是重复的。
请找出数组中任意一个重复的数字，但不能修改输入的数组。
示例 1：
    输入：
    [2, 3, 5, 4, 3, 2, 6, 7]
    输出：2 或 3
限制：
    2 <= n <= 100000
"""


def findRepeatNumber(nums):
    """

    :param nums: List[int]
    :return: int
    """
    left = 1
    right = len(nums)
    while left != right:
        mid = (left + right) // 2
        n = 0
        for i in range(len(nums)):
            if nums[i] in range(left, mid+1):
                n += 1
            if n > (mid-left+1):
                right = mid
                break
        else:
            left = mid+1
    return right


a = [2, 3, 5, 4, 2, 1]
print(findRepeatNumber(a))
