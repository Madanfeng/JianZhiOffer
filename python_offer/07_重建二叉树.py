"""
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如，给出
    前序遍历 preorder = [3,9,20,15,7]
    中序遍历 inorder = [9,3,15,20,7]
    返回如下的二叉树：
        3
       / \
      9  20
        /  \
       15   7
限制：
    0 <= 节点个数 <= 5000
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(preorder, inorder):
    """

    :param preorder: List[int]
    :param inorder: List[int]
    :return: TreeNode
    """
    def recur(pre_root, inl, inr):
        if inl > inr:
            return
        root = TreeNode(preorder[pre_root])
        k = dic[preorder[pre_root]]
        root.left = recur(pre_root+1, inl, k-1)
        root.right = recur(k-inl+pre_root+1, k+1, inr)
        return root

    dic = {}
    for i in range(len(inorder)):
        dic[inorder[i]] = i
    return recur(0, 0, len(inorder)-1)


def buildTree_(preorder, inorder):
    # 二刷
    pass

# e1 = TreeNode(1)
# e2 = TreeNode(2)
# e3 = TreeNode(3)
# e4 = TreeNode(4)
# e5 = TreeNode(5)
# e6 = TreeNode(6)
# e7 = TreeNode(7)
#
# e1.left = e2
# e1.right = e3
# e2.left = e4
# e2.right = e5
# e3.left = e6
# e3.right = e7

buildTree([1,2,4,5,3,6,7],[4,2,5,1,6,3,7])
