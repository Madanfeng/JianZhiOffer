"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：
    输入：nums = [1,2,3,4]
    输出：[1,3,2,4]
    注：[3,1,2,4] 也是正确的答案之一。
 
提示：
    1 <= nums.length <= 50000
    1 <= nums[i] <= 10000
"""


def exchange(nums):
    """

    :param nums: List[int]
    :return: List[int]
    """
    def isodd(num):
        if num % 2 == 0:
            return False
        else:
            return True

    i, j = 0, len(nums)-1
    while i <= j:
        if not isodd(nums[i]):
            if isodd(nums[j]):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            else:
                j -= 1
        else:
            i += 1
    return nums


print(exchange([1,2,3,4]))
