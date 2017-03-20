#encoding=utf8

#合并两个有序的链表

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    """

    :param l1:
    :param l2:
    :return:
    """
    head = ListNode(-1)
    cur = head
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    if l1!=None:
        cur.next = l1
    else:
        cur.next = l2
    return head.next

#尾递归
def _recursion_merge_sort2(l1, l2, tmp):
    """
    递归要注意边界条件
    :param l1:
    :param l2:
    :param tmp:
    :return:
    """

    if len(l1) == 0 or len(l2) == 0:
        tmp.extend(l1)
        tmp.extend(l2)
        return tmp
    else:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
        return _recursion_merge_sort2(l1, l2, tmp)

def recursion_merge_sort2(l1, l2):
    return _recursion_merge_sort2(l1, l2, [])