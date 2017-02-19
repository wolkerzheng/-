#encoding=utf8
class Solution(object):
    """docstring for Solution"""
    def __init__(self):
        pass
        
    def hammingDistance(self, x, y):
            """
            461. Hamming Distance
            两个整数，位的不同个数。eg:1(0001)4(0100);则有两个位不同
            先异或取出两个数位数不同的位置，再一步步检查其1的个数
            :type x: int
            :type y: int
            :rtype: int
            """
            z = x ^ y
            count = 0
            while z>0:
                print z
                if z&0x1 == 1:
                    count += 1
                z = z>>1
            return count

def findInSortedMatrix(m,x):
    """
    """
    if m is None:
        return False
    i,j = 0,0
    while j < len(m[0])and i <len(m): #列数
        if m[i][j] == x:
            return True
        elif m[i][j] < x:
            j = j+1
        else:
            j = j-1
            while i < len(m):
                if m[i][j] == x:
                    return True
                else:
                    i = i+ 1
    return False
        

def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        x = num ^ 0xFFFFFFFF
        res = 0
        
        while x>0:
            if x &0x1 == 1:
                res = 2*res + 1
            x = x>>1
        return res
def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxRes = 0
    tmp = 0
    for i in range(len(nums)):

        if nums[i] == 1:
            tmp +=1
            if maxRes < tmp:
                maxRes = tmp
        else:
            
            tmp = 0

    return maxRes

def islandPerimeter(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
    for i in range(len(grid)):
        
        for j in range(len(grid[i])):
            
            pass
    pass       
if __name__ == '__main__':
    # a = Solution()
    
    
    # print a.hammingDistance(1,4)
    m = [[1,2,8,9],
        [2,4,9,12],
        [4,7,10,13]]
    print findInSortedMatrix(m,8)
    print findMaxConsecutiveOnes([1,1,0,1,1,1])