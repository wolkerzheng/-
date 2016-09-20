#encoding=utf-8
"""
开始自学python，看着廖的文档挺无聊，不如多动手变成
学着多用python进行开发。于是就想起用leetcode来进行相关python练习
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def isHappy(n):
        """
        :type num: int
        :rtype: bool
        """
        his = []
        while n != 1 and n not in his:
            his.append(n)
            sum = 0
            while n>0:
                a = n % 10
                sum += a**2
                n = n /10
            n = sum
        return True if n==1 else False    


def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l1 = len(digits)
        c = 1
        for i in range(0,l1)[::-1]:
        	digits[i] = digits[i]+c
        	c = digits[i] / 10
        	digits[i] = digits[i] % 10
        if c == 1:
            digits.insert(0,c)
        return digits


def insertSort(nums):
    """
    num:list[int]
    """
    #lambda x:x[1]返回list的第二个数据
    # nums.sort(key=lambda x:x[1] ,reverse=True)
    # return nums
    # return sorted(nums)
    l = len(nums)
    for i in xrange(1,l):
        while i < l :
            pass

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    :使用下标记住最小值所在的位置，判断新的元素是否比前面最小值小，然后使用该
     下标，之后每次进行maxP最大收益比较
    """
    maxP = 0
    startIndex = 0
    for i in xrange(len(prices)):
            # pass
        if prices[i] < prices[startIndex]:
            startIndex = i
        maxP = max(maxP,prices[i]-prices[startIndex])
        
    return maxP


def bubblesort(nums):
    """
    冒泡排序
    """
    for i in range(len(nums)):
        for j in range(1,len(nums)):
            if nums[j-1] > nums[j]:
                nums[j-1],nums[j] = nums[j],nums[j-1]
    return nums

def climbStairs(n):
    """
    n：int
    return : int 

    动态规划：在第i层楼梯，只能由在第i-1或者i-2层爬上来的
    故： d[i] = d[i-1] +d[i-2]
    """
    d = {}
    d[0] = 1
    d[1] = 1
    if n<=0:
        return 0
    if n==1:
        return 1
    for i in xrange(2,n+1):
        d[i] = d[i-1]+d[i-2]
    return d[n] 

def singelNums(nums):
    """
    nums:List[int]
    找出只出现一次的数，将数组中的所有数字进行异或处理，两两相同的数字则会为0，而
    唯一不同的一个数在异或处理后则出现：eg[1,2,5,2,4,1,4] 异或后为5
    """
    if len(nums) <=0 :
        return 
    a = nums[0]
    for i in xrange(1,len(nums)):
        a = a^nums[i]
    return a 

def isUglyNum(nums):
    """
    """
    while nums >0:
        if nums == 1:
            return True
        elif nums %2 == 0:
            nums/=2
        elif nums%3==0:
            nums/=3
        elif nums%5==0:
            nums/=5
        else:
            return False
    return False

def isPowerOfFour(num):
    """
    :type num: int
    :rtype: bool
    """
    if num <=0:
        return False
    if num&(num-1) == 0:
        if num &(0xAAAAAAAA) == 0:
            return True
        pass
    return False


def virahankal(n):
    if n==0:
        return [""]
    elif n==1:
        return ["S"]
    else:
        s = ["S" + prosody for prosody in virahankal(n-1)]
        l = ["L" + prosody for prosody in virahankal(n-2)]
        return s+l

def aasdf():
    pass
    with open("12.txt") as t:
        t.read()

def mergeTwoLists(l1,l2):
    """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
    # if l1 is None:
    #     return l2
    # elif l2 is None:
    #     return l1
    # else:
    #     if l1.val < l2.val:
    #         head = l1
    #         head.next = mergeTwoLists(l1.next,l2)
    #     else:
    #         head = l1
    #         head.next = mergeTwoLists(l1,l2.next)
    #     return head
    if(l1 != None) or(l2 != None):
        if l1 == None or (l2 !=None and l1.val >= l2.val):
            tmp = l2
            tmp.next = mergeTwoLists(l1,l2.next)
        else:
            tmp = l1
            tmp.next = mergeTwoLists(l1.next,l2)
        return tmp
    else:
        return None

def swapPairs(self, head):
    """
    :type head: ListNode
    :rtype: ListNode

    """
        
    pass


def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    最大不相邻数组和问题。存储
    """
    # f, s = 0, 0
    # for n in nums:
    #     f, s = s, max(f + n, s)
    # return s
    if len(nums)<=0:
        return 0
    if len(nums)<=2:
        return max(nums)
    nums[1] = max(nums[0],nums[1])
    for i in xrange(2,len(nums)):
         nums[i] = (max(nums[i-2]+nums[i],nums[i-1]))

    return nums[-1]


# while True:
# 	a = (raw_input())
# 	a = [int(w) for w in a.split(" ")]
# print insertSort(a)
# a = [[1,3],[3,4],[2,2],[1,10],[5,7]]
# print a
if __name__ == '__main__':

    while True:
        a = (raw_input())
        a = [int(w) for w in a.split(",")]
        print rob(a)
        # a =  int(raw_input())
        # print isPowerOfFour(a)