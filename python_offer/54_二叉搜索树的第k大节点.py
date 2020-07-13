"""
给定一棵二叉搜索树，请找出其中第k大的节点。

示例 1:
    输入: root = [3,1,4,null,2], k = 1
       3
      / \
     1   4
      \
       2
    输出: 4
示例 2:
    输入: root = [5,3,6,2,4,null,null,1], k = 3
           5
          / \
         3   6
        / \
       2   4
      /
     1
    输出: 4
 
限制：
    1 ≤ k ≤ 二叉搜索树元素个数
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def kthLargest(root, k):
    """
    中序遍历
    :param root: TreeNode
    :param k: int
    :return: int
    """
    stack = []
    nums = []
    n = 0
    p = root
    while stack or p:
        if p:
            stack.append(p)
            p = p.left
        else:
            p = stack.pop(-1)
            nums.append(p.val)
            n += 1
            p = p.right
    return nums[n - k]

