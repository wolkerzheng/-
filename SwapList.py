#encoding=utf8

"""
链表成对交换
before swap:1->2->3->4
after swap:2->1->4->3
"""


class ListNode:

    def __init__(self,x):

        self.val = x
        self.next = None


def swapNode(ListNode):
    """
    :param ListNode:
    :return:
    """
    if ListNode and ListNode.next:
        tmp = ListNode.next
        ListNode.next = swapNode(tmp.next)
        tmp.next = ListNode
        return tmp
    return ListNode
    # pass

def swapNode1(ListNode):
    """
    wrong
    如何设置一个头指针.使其在交换的时候没有发生变化
    :param ListNode:
    :return:
    """
    head = ListNode
    newNode = ListNode(0)
    newNode.next = head

    while head!=None and head.next!=None:
        tmpNode = head.next
        head.next = tmpNode.next
        tmpNode.next = head
        head = head.next
    return  newNode.next

class Solution(object):
    def swapPairs(self, head):
        """

        :param self:
        :param head:
        :return:
        """
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next


