"""
输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)。

示例1:
    输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
    输出: 6
    解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
 
提示：
    1 <= arr.length <= 10^5
    -100 <= arr[i] <= 100
"""


def maxSubArray(nums):
    """
    转移方程： 若 dp[i-1] ≤ 0 ，说明 dp[i-1] 对 dp[i] 产生负贡献，即 dp[i-1] + nums[i] 还不如 nums[i] 本身大。

    当 dp[i−1] > 0 时：执行 dp[i] = dp[i−1] + nums[i] ；
    当 dp[i−1] ≤ 0 时：执行 dp[i] = nums[i] ；

    :param nums: List[int]
    :return: int
    """
    for i in range(1, len(nums)):
        nums[i] += max(nums[i - 1], 0)
    return max(nums)

    """ 
    pre, ret = nums[0], nums[0]
    for i in range(1, len(nums)):
        pre = pre + nums[i] if pre > 0 else nums[i]
        ret = pre if pre > ret else ret
    return ret
    """



print(maxSubArray([8,-19,5,-4,20]))
