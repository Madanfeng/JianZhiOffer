"""
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。


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
      [20,9],
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
    tag = 0
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
        if tag == 0:
            res.append(temp_res)
            tag = 1
        else:
            res.append(temp_res[::-1])
            tag = 0
        q = temp
    return res
