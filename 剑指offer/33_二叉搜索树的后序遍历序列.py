"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。
如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：
    输入: [1,6,3,2,5]
    输出: false
示例 2：
    输入: [1,3,2,6,5]
    输出: true

提示：
    数组长度 <= 1000
"""


def verifyPostorder(postorder):
    """
    二叉树的后续遍历中，最后一个元素是树的根节点
    根据根节点可以将剩余的后续遍历分成两个部分
    前一部分所有元素都小于根节点
    后一部分所有元素都大于根节点
    递归判断前后两部分
    当后一部分中有出现小于根节点的情况 返回 False

    :param postorder: List[int]
    :return: bool
    """
    if postorder == []:
        return True
    if len(postorder) == 1:
        return True
    root = postorder[-1]
    i = 0
    while postorder[i] < root:
        i += 1
    for j in range(i, len(postorder)-1):
        if postorder[j] < root:
            return False
    return verifyPostorder(postorder[0:i]) and verifyPostorder(postorder[i:len(postorder)-1])


print(verifyPostorder([1,6,3,2,5]))
