#encoding=utf8

class Node:
	"""s Nstring for Node"""
	def __init__(self,x):
		
		self.val = x
		self.next = None

def getNodeLength(listNode):
	"""
	获取链表长度
	"""
	lenNode = 0
	if listNode==None:
		return lenNode
	head = listNode.next
	while head:
		head = head.next
		lenNode += 1
	return lenNode

def getCommonNode(l1,l2):
	"""
	求两个链表的公共节点，说明两个链表的最后部分相同，即最后部分等长。
	故先上长链表先走两个链表的差值.
	"""
	len1 = getNodeLength(l1)
	len2 = getNodeLength(l2)

	if len1 > len2:

		for _ in range(len1-len2):
			l1 = l1.next

	else:
		for _ in range(len2-len1):
			l2 = l2.next
	while l1 and l2:

		if l1 == l2:
			return l1
		else:
			l1 = l1.next
			l2 = l2.next

	return None
