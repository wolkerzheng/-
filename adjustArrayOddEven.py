#encoding=utf8

def Solution(nums):
    """

    调整数组形式是奇数位于偶数前
    :param nums:
    :return:
    """

    n = len(nums)
    i,j = 0,n-1
    while i < j:
        while i<=j and nums[i]%2!=0:
            i+=1

        while i<=j and nums[j]%2==0:
            j -= 1
        if i<j:
            nums[i],nums[j] = nums[j],nums[i]

    print nums
    return nums
def isEven(n):
    """
    判断是否为偶数
    :param n:
    :return:
    """
    return n&1==0
print isEven(1)
nums=[4, 2,1, 5, 3]
Solution(nums)