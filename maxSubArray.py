#encoding=utf-8
import math
"""
输入一个数组：
求解最大子数组和
"""
def getMaxCrossNum(nums,low,mid,high):

	"""
	求最大子数组问题，求解中间问题
	"""
	left_sum = -100000
	sum = 0
	for i in range(mid,-1,-1):
		sum+=nums[i]
		if sum>left_sum:
			left_sum = sum
			max_left = i
	right_sum = -10000
	sum = 0
	for j in range(mid+1,high):
		sum += nums[j]
		if sum>right_sum:
			right_sum = sum
			max_right = j

	return left_sum+right_sum

def findMaxSubArray(nums,low,high):
	if low == high:
		return nums[low]
	else:
		mid = int(math.floor((low+high)/2.0))
		left = findMaxSubArray(nums,low,mid)
		right = findMaxSubArray(nums,mid+1,high)
		cross = getMaxCrossNum(nums,low,mid,high)
		if left>cross and left >right:
			return left
		elif right>cross and right>left:
			return right
		else:
			return cross
def getMaxSubArray(nums):
	if not nums:
		return 
	low,high = 0,len(nums)
	nall,sum = nums[0],nums[0]
	for i in range(low+1,high):

		# sum = sum+nums[i]
		sum = max(nums[i],sum+nums[i])
		nall = max(nall,sum)
	return nall
nums = [-2,-5,6,-2,-3,1,5,-6]
# nums = [1, -2, 3, 10, -4, 7, 2, -5]
low = 0
high = len(nums) - 1
print findMaxSubArray(nums,low,high)
print getMaxSubArray(nums)



