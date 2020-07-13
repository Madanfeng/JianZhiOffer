"""
找出数组中重复的数字。
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
请找出数组中任意一个重复的数字。
示例 1：
    输入：
    [2, 3, 1, 0, 2, 5, 3]
    输出：2 或 3
限制：
    2 <= n <= 100000
"""


def findRepeatNumber(nums):
    """
    最直接的想法，通过构造字典，字典的key为nums中的值，value为key值在nums出现的次数
    遍历nums时，第一次出现value == 2的时候，返回该key
    完成整个遍历都没有出现value == 2时，返回-1，代表nums没有重复的数值
    :param nums: List[int]
    :return: int
    """
    temp = {}
    for i in nums:
        if i in temp:
            return i
        else:
            temp[i] = 1
    else:
        return None


def findRepeatNumber_2(nums):
    """如果没有重复的数字，则将排序好后数组的每个序号正好对应其数值。"""
    for i in range(len(nums)):
        while nums[i] != i:
            if nums[nums[i]] == nums[i]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]


a = [2,3,1,0,2,5,3]
print(findRepeatNumber_2(a))
