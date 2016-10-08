#encoding=utf-8
"""
学python，看着廖的文档挺无聊，不如多动手编程
学着多用python进行开发。于是就想起用leetcode来进行相关python练习
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
    # if head is None:
    #         return head
    # p = head.next
    # while p is not None and p.next is not None:
    #     q = p.next
    #     p.next = q.next
    #     p = q
    #     p = p.next.next
    # return head
    pre = ListNode(0)
    pre.next = head
    curr = head
    head = pre
    while curr and curr.next:      # curr =1, curr.next =2
        pre.next = curr.next       # 0 --> 2
        curr.next = pre.next.next  # 1 --> 3  # curr.next.next
        pre.next.next = curr       # 3 --> 1
        pre = curr                 # pre = 1
        curr = curr.next           # curr= 3
    return head.next

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


def isSymmetric( root):
    """
    :type root: TreeNode
    :rtype: bool
    这种python写法比java简洁
    """
    if root is None:
        return True
    stack = [[root.left,root.right]]
    # p = root.left
    # q = root.right
    while stack:
        node1,node2 = stack.pop()
        if node1 and node2:
            if node1.val != node2.val:
                return False
            else:
                stack.append([node1.left,node2.rigth])
                stack.append([node1.right,node2.left])
        else:
            if node1 == node2:     #这种情况是两个节点都是none，所以直接判断。
                continue
            else:
                return False

    return True


def levelOrderBottom(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
        return []

    level_dict = {}
    def reverse_tree(r,level):
        if not r:
            return
        if level in level_dict:
            level_dict[level].append(r.val)
        else:
            level_dict[level] = [r.val]
        if r.left:
            reverse_tree(r.left,level + 1)
        if r.right:
            reverse_tree(r.right,level + 1)
    reverse_tree(root,0)
    boot_up_last = [level_dict[l] for l in sorted(level_dict,reverse=True) ]
    return  boot_up_last
    # pass

def levelOrder( root):
    """
    时间用时较多，不是优解；
    层次遍历，一层一层的输出节点
    :param root:
    :return:
    """
    if not root:
        return []
    queue,qn,res = [root],[],[]

    while queue:
        qn,res1 =[],[]
        while queue:
            tmp = queue.pop(0)
            res1.append(tmp.val)
            if tmp.left:
                qn.append(tmp.left)
            if tmp.right:
                qn.append(tmp.right)
        res.append(res1)
        queue = qn

    return res


def readBinaryWatch(num):
    """
    二进制时间表；
    :type num: int
    :rtype: List[str]
    """
    pass

def binaryTreePaths( root):

    pass
def hasPathSum( root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """

    pass
def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    #这种解法时间耗费多
    # res = []
    # for i in xrange(numRows):
    #     tmp=[]
    #     for j in xrange(i+1):
    #         if i-1<0 or j-1<0 or j>i-1:
    #             tmp.append(1)
    #         else:
    #             tmp.append(res[i-1][j]+res[i-1][j-1])
    #     res.append(tmp)
    # return res
    if numRows == 0:
        return []
    res = [[1], ]
    for i in range(0, numRows - 1):
        l = [sum(p) for p in list(zip(res[i], res[i][1:]))]
        l.insert(0, 1)
        l.append(1)
        res.append(l)
    return res

def isBalanced(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True
    if abs(getHeight(root.left) - getHeight(root.right)) > 1:return False
    return isBalanced(root.left) and isBalanced(root.right)

def getHeight(root):
    return 0 if root is None else max(getHeight(root.left),getHeight(root.right))+1


def trailingZeroes(n):
    """
    求解N的阶乘后面0的个数；
    10 = 2*5；
    :type n: int
    :rtype: int
    """
    sum=0
    i=1
    while pow(5,i) <= n:
        sum += n/pow(5,i)
        i+=1
    return sum


def sumOfLeftLeaves( root):
    """
    :type root: TreeNode
    :rtype: int
    计算左叶子之和
    """
    if not root:
        return 0
    if root.left and not root.left.left and not root.left.right:
        return root.left.val + sumOfLeftLeaves(root.right)
    return sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right)

# while True:
# 	a = (raw_input())
# 	a = [int(w) for w in a.split(" ")]
# print insertSort(a)
# a = [[1,3],[3,4],[2,2],[1,10],[5,7]]
# print a
if __name__ == '__main__':
    while True:
        a = int(raw_input())
        print trailingZeroes(a)

    # while True:
    #     a = (raw_input())
    #     a = [int(w) for w in a.split(" ")]

        # a =  int(raw_input())
        # print isPowerOfFour(a)