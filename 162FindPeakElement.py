#encoding=utf8
class Solution(object):
    def findPeakElement(self, nums):
        """
        o(logn)
        If num[i-1] < num[i] > num[i+1], then num[i] is peak
		If num[i-1] < num[i] < num[i+1], then num[i+1...n-1] must contains a peak
		If num[i-1] > num[i] > num[i+1], then num[0...i-1] must contains a peak
		If num[i-1] > num[i] < num[i+1], then both sides have peak
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
        	return 0
        start = 0
        end = len(nums) -1
        while start<end:
        	mid = (start + end) /2
        	
        	if nums[mid]>nums[mid+1]:
        		end = mid
        	else:
        		start = mid+1
        return start
    def findPeakElement2(self, nums):
        """
        暴力
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0,len(nums)-1):
        	if nums[i]>nums[i+1]:
        		return i
        return len(nums)-1
        pass

if __name__ == '__main__':
	s = Solution()
	print s.findPeakElement([1, 2,3,1])
