class Solution(object):
”"“
”"“
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        imax=imin=r = nums[0]
        for i in range(1,len(nums)):
            
            if nums[i]<0:
                imax,imin = imin,imax
            imax = max(nums[i],nums[i]*imax)
            imin = min(nums[i],nums[i]*imin)
            r = max(r,imax)
        return r
