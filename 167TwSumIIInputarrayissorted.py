#encoding=utf8


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i,num in enumerate(numbers):

            if target-num in dic:
                return [dic[target-num]+1,i+1]
            dic[num] = i
        pass
    def twoSum1(self,numbers,target):

        l,r = 0,len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r] ==target:
                return [l,r]
            elif numbers[l]+numbers[r] < target:
                l +=1
            else:
                r -=1

        pass

if __name__ == '__main__':

    S = Solution()
    print S.twoSum([2, 7, 11, 15],9)
    pass
