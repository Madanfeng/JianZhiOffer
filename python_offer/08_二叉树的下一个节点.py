"""
给定一棵二叉树和其中的一个节点，如何找出中序遍历序列的下一个节点？
树中的节点除了有两个分别指向左、右子节点的指针，还有一个指向父节点的指针。

如图，二叉树的中序遍历序列是[d,b,h,e,i,a,f,c.g]
         a
       /  \
      b    c
     /\   /\
    d  e f  g
      /\
     h  i
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.father = None


def findnextNode(root, node):
    """
    迭代中序遍历
    :param root: TreeNode
    :param node: TreeNode
    :return: TreeNode
    """
    res = []
    stack = []
    curr = root
    tag = 0
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        if tag == 1:
            return curr.val
        if curr.val == node:
            tag = 1
        curr = curr.right


e1 = TreeNode(1)
e2 = TreeNode(2)
e3 = TreeNode(3)
e4 = TreeNode(4)
e5 = TreeNode(5)
e6 = TreeNode(6)
e7 = TreeNode(7)

e1.left = e2
e1.right = e3
e2.left = e4
e2.right = e5
e3.left = e6
e3.right = e7

print(findnextNode(e1, 5))
