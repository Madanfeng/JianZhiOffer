"""
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:
    输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
    输出: [3,3,5,5,6,7]
    解释:

      滑动窗口的位置                最大值
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7
 
提示：
    你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。
"""
import collections


def maxSlidingWindow(nums, k):
    """
    暴力法
    :param nums: List[int]
    :param k: int
    :return: List[int]
    """
    if nums == []:
        return []
    res = []
    for i in range(len(nums)-k+1):
        res.append(max(nums[i:i+k]))
    return res


def maxSlidingWindow_2(nums, k):
    """

    :param nums: List[int]
    :param k: int
    :return: List[int]
    """
    if not nums or k == 0: return []
    deque = collections.deque()
    for i in range(k):  # 未形成窗口
        while deque and deque[-1] < nums[i]: deque.pop()
        deque.append(nums[i])
    res = [deque[0]]
    for i in range(k, len(nums)):  # 形成窗口后
        if deque[0] == nums[i - k]: deque.popleft()
        while deque and deque[-1] < nums[i]: deque.pop()
        deque.append(nums[i])
        res.append(deque[0])
    return res


print(maxSlidingWindow_2([1,3,-1,-3,-2,5,3,6,7], 3))
