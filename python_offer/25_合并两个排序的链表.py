"""
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：
    输入：1->2->4, 1->3->4
    输出：1->1->2->3->4->4
限制：
    0 <= 链表长度 <= 1000
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):
    """

    :param l1: ListNode
    :param l2: ListNode
    :return: ListNode
    """
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    if l1.val > l2.val:
        l1, l2 = l2, l1
    head, pre = l1, l1
    l1 = l1.next
    while l1 and l2:
        while l1 and l1.val <= l2.val:
            pre = l1
            l1 = l1.next
        else:
            temp = l2
            l2 = l2.next
            pre.next = temp
            pre = temp
            pre.next = l1
    if l2:
        pre.next = l2
    return head
