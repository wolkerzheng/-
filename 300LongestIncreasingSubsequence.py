#encoding=utf8
class Solution(object):
    
    def lengthOfLIS(self, nums):
        """
        最长递增序列O(n^2)
        dp[i]表示以第i个数为结尾时候，其最长的递增序列
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums)==0:
        	return 0
        dp = [1]*len(nums)
        for i in xrange(1,len(nums)):
        	for j in xrange(0,i):
        		if nums[j]<nums[i]:
        			dp[i] = max(dp[i],dp[j]+1)
        		
        res = max(dp) 
        return res

    def lengthOfLIS2(self, nums):
        """
        最长递增序列O(nlogn)
        tail[i]表示存储长度为i+1的所有递增子序列的最小尾部
		例如： nums = [4,5,6,3], 所有可能的序列为:
		len = 1   :      [4], [5], [6], [3]   => tails[0] = 3
		len = 2   :      [4, 5], [5, 6]       => tails[1] = 5
		len = 3   :      [4, 5, 6]            => tails[2] = 6
        :type nums: List[int]
        :rtype: int
        """
		size = 0
		tails = [0] * len(nums)
		for x in nums:
			i, j = 0, size
			while i != j:
				m = (i + j) / 2
				if tails[m] < x:
					i = m + 1
				else:
					j = m
			tails[i] = x
			size = max(i + 1, size)
		print tails
		return size
		
if __name__ == '__main__':
	s = Solution()
	print s.lengthOfLIS2([1, 2,3,1])
