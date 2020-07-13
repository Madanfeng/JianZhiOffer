"""
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。
 
示例:
    给定如下二叉树，以及目标和 sum = 22，

                  5
                 / \
                4   8
               /   / \
              11  13  4
             /  \    / \
            7    2  5   1
    返回:
    [
       [5,4,11,2],
       [5,8,4,5]
    ]
 
提示：
    节点总数 <= 10000
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def pathSum(root, sum):
    """

    :param root: TreeNode
    :param sum: int
    :return: List[List[int]]
    """
    def dfs(root, n, temp):
        temp = temp + [root.val]
        if root.val == n and not root.left and not root.right:
            res.append(temp)
        if root.left:
            dfs(root.left, n-root.val, temp)
        if root.right:
            dfs(root.right, n-root.val, temp)
        return None

    if root is None:
        return []
    res = []
    dfs(root, sum, [])
    return res
