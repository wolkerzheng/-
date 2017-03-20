#encoding=utf8

# Definition for singly-linked list.

"""
1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
双指针一个记录位置一个移动
tip:头指针元素的删除,返回

"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode

        """
        if head == None:
            return head

        p = head
        while p.next:

            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next

        if head.val == val:
            return head.next
        return head

    def removeElements2(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode

        """
        fakehead = ListNode(0)
        fakehead.next = head
        p = fakehead

        while p.next!=None:

            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next

        return fakehead.next