"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。
要求不能创建任何新的节点，只能调整树中节点指针的指向。

为了让您更好地理解问题，以下面的二叉搜索树为例：
    4
   / \
  2   5
 / \
1   3
 
我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。
对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。
 https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof

特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。
还需要返回链表中的第一个节点的指针。
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def treeToDoublyList(root):
    """

    :param root: 'Node'
    :return: 'Node'
    """
    stack = []
    res = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.append(root)
        root = root.right

    for i in range(len(res)):
        res[i].right = res[(i+1) % len(res)]
        res[i].left = res[i-1]
    head = res[0]
    return head


e1 = Node(4)
e2 = Node(2)
e3 = Node(5)
e4 = Node(1)
e5 = Node(3)
e6 = Node(6)
e7 = Node(7)

e1.left = e2
e1.right = e3
e2.left = e4
e2.right = e5
# e3.left = e6
# e3.right = e7
print(treeToDoublyList(e1))
