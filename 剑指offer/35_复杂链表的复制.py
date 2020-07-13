"""
请实现 copyRandomList 函数，复制一个复杂链表。
在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

示例 1：
    https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof
    输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
    输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
示例 2：
    https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof
    输入：head = [[1,1],[2,1]]
    输出：[[1,1],[2,1]]
示例 3：
    https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof
    输入：head = [[3,null],[3,0],[3,null]]
    输出：[[3,null],[3,0],[3,null]]
示例 4：
    https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof
    输入：head = []
    输出：[]
    解释：给定的链表为空（空指针），因此返回 null。
 
提示：
    -10000 <= Node.val <= 10000
    Node.random 为空（null）或指向链表中的节点。
    节点数目不超过 1000 。
"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head):
    """

    :param head: 'Node'
    :return: 'Node'
    """
    if head is None:
        return None
    res_head = Node(head.val, None, None)
    p = head.next
    q = res_head
    d = {head:0}
    res_list = [q]
    i = 1
    while p:
        d[p] = i
        i += 1
        q.next = Node(p.val, None, None)
        p = p.next
        q = q.next
        res_list.append(q)
    p = head
    q = res_head
    while p:
        if p.random:
            q.random = res_list[d[p.random]]
        else:
            q.random = None
        q = q.next
        p = p.next
    return res_head


def copyRandomList_2(head):
    """

    :param head: 'Node'
    :return: 'Node'
    """
    def recur(head):
        if not head:
            return None
        if head in dic:
            return dic[head]
        one = Node(head.val, None, None)
        dic[head] = one
        one.next = recur(head.next)
        one.random = recur(head.random)
        return one

    # 键为老节点对象；值为新节点对象
    dic = {}
    return recur(head)
