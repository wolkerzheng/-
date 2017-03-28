#encoding=utf8


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return False
        if sum(nums)%2 !=0 :
            return False
        bestSum = sum(nums) / 2


        return



if __name__ == '__main__':

    a = Solution()

    print a.canPartition([1, 2,3,5])
