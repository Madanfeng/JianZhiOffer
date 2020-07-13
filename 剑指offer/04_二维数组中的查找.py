"""
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例:
    现有矩阵 matrix 如下：
    [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]
    给定 target = 5，返回 true。
    给定 target = 20，返回 false。

限制：
    0 <= n <= 1000
    0 <= m <= 1000
"""


def findNumberIn2DArray(matrix, target):
    """
    最直接的想法
    :param matrix: List[List[int]]
    :param target: int
    :return: bool
    """
    if not matrix:
        return False
    for i in range(len(matrix)):
        if matrix[i][0] > target:
            return False
        if matrix[i][-1] < target:
            continue
        # 二分法查找
        left = 0
        right = len(matrix[0]) - 1
        while left != right:
            mid = (left + right) // 2
            if matrix[i][mid] >= target:
                right = mid
            else:
                left = mid + 1
        if matrix[i][left] == target:
            return True
    return False


def findNumberIn2DArray_2(matrix, target):
    """
    从矩阵右上角开始遍历，如果正好等于target，返回True；如果该值小于target，则排除该行；如果该值大于target，则排除该列。
    :param matrix: List[List[int]]
    :param target: int
    :return: bool
    """
    if not matrix:
        return False
    i = 0
    j = len(matrix[0]) - 1
    while i < len(matrix) and j >= 0:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            i += 1
        else:
            j -= 1
    return False


m = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

print(findNumberIn2DArray_2(m, 33))
