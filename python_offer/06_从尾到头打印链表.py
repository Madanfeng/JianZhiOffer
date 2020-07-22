"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
示例 1：
    输入：head = [1,3,2]
    输出：[2,3,1]
限制：
    0 <= 链表长度 <= 10000
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reversePrint(head):
    """
    借助栈
    :param head: ListNode
    :return: List[int]
    """
    res = []
    p = head
    while p:
        res.append(p.val)
        p = p.next
    return res[::-1]


def reversePrint_2(head):
    """
    递归
    :param head: ListNode
    :return: List[int]
    """
    if head:
        if head.val:
            reversePrint_2(head.next)
        print(head.val)


def reversePrint_(head):
    # 二刷
    # 思路：从头到尾遍历，逆序输出
    p = head
    res = []
    while p:
        res.append(p.val)
        p = p.next
    return res[::-1]
