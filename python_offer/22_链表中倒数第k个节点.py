"""
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

示例：
    给定一个链表: 1->2->3->4->5, 和 k = 2.
    返回链表 4->5.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getKthFromEnd(head, k):
    """
    需要2次遍历链表
    :param head: ListNode
    :param k: int
    :return: ListNode
    """
    num = 0
    p = head
    while p:
        num += 1
        p = p.next
    p = head
    for i in range(num-k):
        p = p.next
    return p


def getKthFromEnd_2(head, k):
    """
    只需遍历一次链表
    注意异常输入
    :param head: ListNode
    :param k: int
    :return: ListNode
    """
    # 当head为空或者返回倒数第0个时，都返回None
    if head == None or k == 0:
        return None
    p, q = head, head
    for _ in range(k-1):
        if p.next:
            p = p.next
        else:
            # k超出链表原有长度了
            return None
    while p.next:
        p = p.next
        q = q.next
    return q
