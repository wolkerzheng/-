#encoding=utf8

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        start = nums[n-1]
        all = nums[n-1]
        for i in range(n-2,-1,-1):
            if start <0:
                start = 0
            start += nums[i]
            all = max(start,all)
        return all


    def maxSubArrayDivideAndCon(self,nums):
        """
        wrong code
        最大子串在左半部1.nums[0...n/2-1]
        最大子串在右半部2.nums[n/2,n]
        最大子串不在前两者情况,在中间出现,跨过中间两个
        :param nums:
        :return:
        """

        if len(nums) ==0: return -100000000
        # n = len(nums)
        end = len(nums)
        start = 0
        mid = (start+end)/2
        if start >= end: return nums[start]

        sum1 = self.maxSubArrayDivideAndCon(nums[start:mid-1])
        sum2 = self.maxSubArrayDivideAndCon(nums[mid:end])
        sum3 = self.maxSubArrayDivideAndCon(nums[start+mid/2:end-mid/2])

        pass
        return max(sum3,max(sum1,sum2))




if __name__ == '__main__':

    s = Solution()
    # print s.maxSubArrayDivideAndCon([-1,-2,3])
    pass