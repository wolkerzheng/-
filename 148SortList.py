#encoding=utf8

# Definition for singly-linked list.
"""
Sort a linked list in O(n log n) time using constant space complexity.
分治思想：
先用双指针来将链表分为两个链表
再把两个相当于有序链表进行合并。
两个有序的链表合并，剑指offer中有

"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
        	return head

        prev = None
        slow = fast = head
        while fast and fast.next:
        	prev = slow
        	slow = slow.next
        	fast = fast.next.next
        
        prev.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return mergeList(l1,l2)

   	def mergeList(l1,l2):
   		"""
		sort two sorted list
   		"""
   		head = ListNode(0)
   		p = head
   		while l1 and l2:
   			if l1.val < l2.val
   				p.next = l1
   				l1 = l1.next
   			else:
   				p.next = l2
   				l2 = l2.next
   			p = p.next
   		if l1:
   			p.next = l1
   		if l2:
   			p.next = l2
   		return head.next



   
