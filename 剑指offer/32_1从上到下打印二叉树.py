"""
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

例如:
    给定二叉树: [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7
    返回：
    [3,9,20,15,7]
 
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
    :return: List[int]
    """
    if root is None:
        return []
    res = []
    q = [root, ]
    while q:
        temp = []
        while q:
            p = q.pop(0)
            res.append(p.val)
            if p.left:
                temp.append(p.left)
            if p.right:
                temp.append(p.right)
        q = temp
    return res


print(levelOrder([]))
