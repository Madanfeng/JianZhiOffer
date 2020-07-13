"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例 1：
    输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
    输出：[1,2,3,6,9,8,7,4,5]
示例 2：
    输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    输出：[1,2,3,4,8,12,11,10,9,5,6,7]

限制：
    0 <= matrix.length <= 100
    0 <= matrix[i].length <= 100
"""


def spiralOrder(matrix):
    """

    :param matrix: List[List[int]]
    :return: List[int]
    """
    if matrix == []:
        return []
    res = []
    m = len(matrix)
    n = len(matrix[0])
    start = 0
    while m > start*2 and n > start*2:
        endm = m - 1 - start
        endn = n - 1 - start

        for i in range(start, endn+1):
            res.append(matrix[start][i])
        if endm > start:
            for i in range(start+1, endm+1):
                res.append(matrix[i][endn])
        if start < endn and start < endm:
            for i in range(endn-1, start-1, -1):
                res.append(matrix[endm][i])
        if start < endn and start < endm - 1:
            for i in range(endm-1, start, -1):
                res.append(matrix[i][start])

        start += 1
    return res


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder([[]]))
