#encoding=utf8

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        wordDict = {}
        res = []
        for num in nums:
            if num not in wordDict:
                wordDict[num] = 0
            wordDict[num] += 1
        sortedList = sorted(wordDict.items(), key=lambda item: item[1],reverse=True)
        for i in range(k):
            res.append(sortedList[i][0])

        return res

if __name__ == '__main__':

    s = Solution()
    print s.topKFrequent([1,1,1,2,2,3],2)