"""
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

示例:
    输入: 1->2->3->4->5->NULL
    输出: 5->4->3->2->1->NULL

限制：
    0 <= 节点个数 <= 5000
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head):
    """

    :param head: ListNode
    :return: ListNode
    """
    if head == None:
        return None
    p = head
    pre = head.next
    p.next = None
    while pre:
        head = pre
        pre = head.next
        head.next = p
        p = head
    return head

