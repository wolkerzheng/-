#encoding=utf8
"""
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order
"""
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        begin,end = -1,-2
        minN = nums[n-1]
        maxN = nums[0]
        for i in xrange(1,n):
        	maxN = max(maxN,nums[i])
        	minN = min(minN,nums[i])
        	if nums[i]<max:
        		end = i
        	if nums[n-1-i]>minN:
        		begin = n-1-i
        return end-begin+1