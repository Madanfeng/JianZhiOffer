"""
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

示例 1:
    输入:
    [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    输出: 12
    解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
 
提示：
    0 < grid.length <= 200
    0 < grid[0].length <= 200
"""


def maxValue(grid):
    """

    :param grid: List[List[int]]
    :return: int
    """
    if grid == [] or grid == [[]]:
        return 0
    res = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if i == 0 and j == 0:
                res[i][j] = grid[i][j]
            elif i == 0 and j != 0:
                res[i][j] = grid[i][j] + res[i][j-1]
            elif i != 0 and j == 0:
                res[i][j] = grid[i][j] + res[i-1][j]
            else:
                res[i][j] = max(res[i-1][j], res[i][j-1]) + grid[i][j]
    return res[-1][-1]


print(maxValue([[]]))
