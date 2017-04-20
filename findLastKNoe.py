#encoding=utf8

class ListNode(object):

    def __init__(self,x):
        self.val = x
        self.next = None


class Solution():

    def findLastKNode(self,head,k):
        p = head
        for i in range(k-1):
            if not p:
                p = p.next
            else:
                return None

        while p !=None:
            p = p.next
            head = head.next

        return head