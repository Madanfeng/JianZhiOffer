"""
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：
    输入：A = [1,2,3], B = [3,1]
    输出：false
示例 2：
    输入：A = [3,4,5,1,2], B = [4,1]
    输出：true
限制：
    0 <= 节点个数 <= 10000
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSubStructure(A, B):
    """
    根据前序遍历迭代
    :param A: TreeNode
    :param B: TreeNode
    :return: bool
    """
    def isMatch(a, b):
        s1, s2 = [a, ], [b, ]
        while s1 and s2:
            root1 = s1.pop()
            root2 = s2.pop()
            if root1 is not None and root2 is not None:
                if root1.val != root2.val:
                    return False
                if root1.right is not None and root2.right is not None:
                    s1.append(root1.right)
                    s2.append(root2.right)
                elif root2.right is not None:
                    s2.append(root2.right)
                if root1.left is not None and root2.left is not None:
                    s1.append(root1.left)
                    s2.append(root2.left)
                elif root2.left is not None:
                    s2.append(root2.left)
        if s2 == []:
            return True
        return False

    if A is None and B is None:
        return True
    elif A is not None and B is None:
        return False
    elif A is None and B is not None:
        return False
    stack = [A, ]
    while stack:
        root = stack.pop()
        if root is not None:
            if root.val == B.val:
                if isMatch(root, B):
                    return True
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)

    return False


def isSubStructure_2(A, B):
    """
    递归
    :param A: TreeNode
    :param B: TreeNode
    :return: bool
    """
    def dfs(A, B):
        if not B:
            return True
        if not A or A.val != B.val:
            return False
        return dfs(A.left, B.left) and dfs(A.right, B.right)

    if not A or not B:
        return False
    return dfs(A, B) or isSubStructure_2(A.left, B) or isSubStructure_2(A.right, B)


a1 = TreeNode(1)
a2 = TreeNode(0)
a3 = TreeNode(1)
a4 = TreeNode(-4)
a5 = TreeNode(-3)
a6 = TreeNode(6)
a7 = TreeNode(7)

a1.left = a2
a1.right = a3
a2.left = a4
a2.right = a5
# a3.left = a6
# a3.right = a7


b1 = TreeNode(1)
b2 = TreeNode(-4)
b3 = TreeNode(3)

b1.left = b2
# b1.right = b3

print(isSubStructure_2(a1, b1))
