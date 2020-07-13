"""
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
    1
   / \
  2   2
   \   \
   3    3

示例 1：
    输入：root = [1,2,2,3,4,4,3]
    输出：true
示例 2：
    输入：root = [1,2,2,null,3,null,3]
    输出：false
 
限制：
    0 <= 节点个数 <= 1000
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSymmetric(root):
    """

    :param root: TreeNode
    :return: bool
    """
    q = [root, ]
    while q:
        temp = []
        val = []
        while q:
            p = q.pop()
            if p != None:
                temp.append(p.left)
                temp.append(p.right)
                if p.left:
                    val.append(p.left.val)
                else:
                    val.append(None)
                if p.right:
                    val.append(p.right.val)
                else:
                    val.append(None)
        if val[::] != val[::-1]:
            return False
        q = temp
    return True


a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(2)
a4 = TreeNode(3)
a5 = TreeNode(3)
a6 = TreeNode(5)
a7 = TreeNode(3)

a1.left = a2
a1.right = a3
# a2.left = a4
a2.right = a5
# a3.left = a6
a3.right = a7

print(isSymmetric(a1))
