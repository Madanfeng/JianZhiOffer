"""
输入一棵二叉树的根节点，求该树的深度。
从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：
    给定二叉树 [3,9,20,null,null,15,7]，

        3
       / \
      9  20
        /  \
       15   7
    返回它的最大深度 3 。

提示：
    节点总数 <= 10000
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxDepth(root):
    """

    :param root: TreeNode
    :return: int
    """
    if root is None:
        return 0
    depth = 0
    q = [root, ]
    while q:
        depth += 1
        temp = []
        while q:
            p = q.pop()
            if p.left:
                temp.append(p.left)
            if p.right:
                temp.append(p.right)
        q = temp

    return depth

