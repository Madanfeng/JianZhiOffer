"""
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

示例 1:
    输入: [1,2,3,4,5]
    输出: True
示例 2:
    输入: [0,0,1,2,5]
    输出: True
 
限制：
    数组长度为 5 
    数组的数取值为 [0, 13] .
"""


def isStraight(nums):
    """

    :param nums: List[int]
    :return: bool
    """
    nums.sort()
    tag = 0
    if nums[0] == 0:
        tag += 1
    for i in range(1, 5):
        if nums[i] == 0:
            tag += 1
            continue
        if nums[i-1] == nums[i]:
            return False
        if nums[i-1] != 0 and nums[i-1] + 1 == nums[i]:
            continue
        if nums[i-1] != 0 and nums[i-1] + 1 != nums[i]:
            tag -= (nums[i] - nums[i-1] - 1)
            if tag < 0:
                return False

    return True


print(isStraight([0,0,1,2,5]))
