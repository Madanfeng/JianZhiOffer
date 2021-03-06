"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。
如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。
例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。
[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]
但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。
示例 1：
    输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    输出：true
示例 2：
    输入：board = [["a","b"],["c","d"]], word = "abcd"
    输出：false
提示：
    1 <= board.length <= 200
    1 <= board[i].length <= 200
"""


def exist(board, word):
    """
    递归参数：
        当前元素在矩阵 board 中的行列索引 i 和 j ，当前目标字符在 word 中的索引 k 。
    终止条件：
        返回 falsefalse ： ①行或列索引越界 或 ②当前矩阵元素与目标字符不同 或 ③当前矩阵元素已访问过 （③可合并至②）。
        返回 truetrue ： 字符串 word 已全部匹配，即 k = len(word) - 1 。
    递推工作：
        标记当前矩阵元素： 将 board[i][j] 值暂存于变量 tmp ，并修改为字符 '/' ，代表此元素已访问过，防止之后搜索时重复访问。
        搜索下一单元格： 朝当前元素的 上、下、左、右 四个方向开启下层递归，使用 或 连接 （代表只需一条可行路径） ，并记录结果至 res 。
        还原当前矩阵元素： 将 tmp 暂存值还原至 board[i][j] 元素。
    回溯返回值：
        返回 res ，代表是否搜索到目标字符串。
    :param board: List[List[str]]
    :param word: str
    :return: bool
    """
    def dfs(i, j, k):
        if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True
        tmp, board[i][j] = board[i][j], '/'
        res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
        board[i][j] = tmp
        return res

    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, 0):
                return True
    return False


b = [["a","b","c","e"],
     ["s","f","c","s"],
     ["a","d","e","e"]]
w = "bfcc"
print(exist(b, w))
