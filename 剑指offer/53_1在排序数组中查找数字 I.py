"""
统计一个数字在排序数组中出现的次数。

示例 1:
    输入: nums = [5,7,7,8,8,10], target = 8
    输出: 2
示例 2:
    输入: nums = [5,7,7,8,8,10], target = 6
    输出: 0
 
限制：m
    0 <= 数组长度 <= 50000
"""


def search(nums, target):
    """

    :param nums: List[int]
    :param target: int
    :return: int
    """
    if nums == []:
        return 0
    n = len(nums)
    left, right = 0, n-1
    while left != right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    if nums[left] != target:
        return 0
    res = 1
    i, j = left - 1, left + 1
    while i >= 0 and j < n:
        if nums[i] != target and nums[j] != target:
            return res
        if nums[i] == target:
            res += 1
            i -= 1
        if nums[j] == target:
            res += 1
            j += 1
    while i >= 0 and nums[i] == target:
        res += 1
        i -= 1
    while j < n and nums[j] == target:
        res += 1
        j += 1

    return res


def search_2(nums, target):
    """
    二分查找分别查找第一个和最后一个target
    :param nums: List[int]
    :param target: int
    :return: int
    """
    n = len(nums)
    left, right = 0, n-1
    while left != right:
        mid = left + (right - left) // 2
        if nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] == target:
            if mid == 0:
                left, right = 0, 0
                break
            if nums[mid - 1] == target:
                right = mid - 1
            else:
                left, right = mid, mid
    if nums[left] != target:
        return 0
    start = left

    left, right = 0, n - 1
    while left != right:
        mid = left + (right - left) // 2
        if nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] == target:
            if mid == n-1:
                left, right = n-1, n-1
                break
            if nums[mid + 1] == target:
                left = mid + 1
            else:
                left, right = mid, mid
    end = left
    return end - start + 1


print(search_2([2,2], 2))
