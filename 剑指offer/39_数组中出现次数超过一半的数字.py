"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
 
示例 1:
    输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
    输出: 2
限制：
    1 <= 数组长度 <= 50000
"""


def majorityElement(nums):
    """

    :param nums: List[int]
    :return: int
    """
    if nums == []:
        return None
    vote = 0
    for num in nums:
        if vote == 0:
            x = num
            vote += 1
        else:
            vote -= 1
    return x


print(majorityElement([1]))
