"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组，求出这个数组中的逆序对的总数。

示例 1:
    输入: [7,5,6,4]
    输出: 5

限制：
    0 <= 数组长度 <= 50000
"""


def reversePairs(nums):
    """
    暴力
    :param nums: List[int]
    :return: int
    """
    res = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                res += 1
    return res


def reversePairs_2(nums):
    """
    归并排序

    :param nums: List[int]
    :return: int
    """
    def mergeSort(nums, tmp, l, r):
        if l >= r:
            return 0

        mid = (l + r) // 2
        inv_count = mergeSort(nums, tmp, l, mid) + mergeSort(nums, tmp, mid + 1, r)
        i, j, pos = l, mid + 1, l
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                i += 1
                inv_count += (j - (mid + 1))
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1
        for k in range(i, mid + 1):
            tmp[pos] = nums[k]
            inv_count += (j - (mid + 1))
            pos += 1
        for k in range(j, r + 1):
            tmp[pos] = nums[k]
            pos += 1
        nums[l:r + 1] = tmp[l:r + 1]
        return inv_count

    n = len(nums)
    temp = [0] * n
    return mergeSort(nums, temp, 0, n-1)


print(reversePairs_2([7,5,6,4]))
