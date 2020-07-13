"""
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

例如:
    给定二叉树: [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7
    返回其层次遍历结果：

    [
      [3],
      [9,20],
      [15,7]
    ]
 
提示：
    节点总数 <= 1000
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelOrder(root):
    """

    :param root: TreeNode
    :return: List[List[int]]
    """
    if root is None:
        return []
    res = []
    q = [root, ]
    while q:
        temp = []
        temp_res = []
        while q:
            p = q.pop(0)
            temp_res.append(p.val)
            if p.left:
                temp.append(p.left)
            if p.right:
                temp.append(p.right)
        res.append(temp_res)
        q = temp
    return res
