"""
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

示例 1：
    输入：target = 9
    输出：[[2,3,4],[4,5]]
示例 2：
    输入：target = 15
    输出：[[1,2,3,4,5],[4,5,6],[7,8]]
 
限制：
    1 <= target <= 10^5
"""


def findContinuousSequence(target):
    """

    :param target: int
    :return: List[List[int]]
    """
    res = []
    small = 1
    big = 2
    s = small + big
    while small <= (target+1)//2:
        if s < target:
            big += 1
            s += big
        elif s > target:
            s -= small
            small += 1
        else:
            res.append([i for i in range(small, big+1)])
            s -= small
            small += 1
    return res


print(findContinuousSequence(16))
