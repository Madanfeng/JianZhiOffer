"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  
示例 1：
    输入：[3,4,5,1,2]
    输出：1
示例 2：
    输入：[2,2,2,0,1]
    输出：0
注意：本题与主站 154 题相同：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/
"""


def minArray(numbers):
    """
    两个指针，头尾同时开始判断，比顺序查找快
    :param numbers: List[int]
    :return: int
    """
    i = 0
    j = len(numbers) - 1
    if j == 0:
        return numbers[0]
    while i < j - 1:
        if numbers[i+1] < numbers[i]:
            return numbers[i+1]
        if numbers[j] < numbers[j-1]:
            return numbers[j]
        i += 1
        j -= 1
    if numbers[i] <= numbers[j]:
        return numbers[0]
    return numbers[j]


def minArray_2(numbers):
    """
    二分查找
    :param numbers: List[int]
    :return: int
    """
    left = 0
    right = len(numbers) - 1
    while left < right:
        mid = (left + right) // 2
        if numbers[mid] > numbers[right]:
            left = mid + 1
        elif numbers[mid] < numbers[left]:
            right = mid
        else:
            right -= 1
    return numbers[left]


n = [3,4,5]
print(minArray_2(n))
