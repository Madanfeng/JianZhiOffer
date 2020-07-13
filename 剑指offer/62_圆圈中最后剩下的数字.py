"""
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，
则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

示例 1：

 输入: n = 5, m = 3
    输出: 3
示例 2：
    输入: n = 10, m = 17
    输出: 2

限制：
    1 <= n <= 10^5
    1 <= m <= 10^6
"""


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def lastRemaining(n, m):
    """
    运用循环链表
    超时
    :param n: int
    :param m: int
    :return: int
    """
    head = Node(0)
    p = head
    for i in range(1, n):
        temp = Node(i)
        p.next = temp
        p = p.next
    p.next = head
    while p.next != p:
        for i in range(m-1):
            p = p.next
        p.next = p.next.next

    return p.val


def lastRemaining_2(n, m):
    """

    :param n: int
    :param m: int
    :return: int
    """
