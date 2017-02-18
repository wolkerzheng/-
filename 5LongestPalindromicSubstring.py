#encoding=utf8

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<=0:
            return s

        newStr = "#!"
        for c in s :
            newStr +=c+"!"
        newStr += "#"
        # print newStr
        maxList = [1,1]

        for i in range(2,len(newStr)):
            tmp = 1

            while i+tmp<len(newStr) and newStr[i-tmp] == newStr[i+tmp]:
                tmp += 1

            maxList.append(tmp)
        # print maxList
        maxLong = max(maxList)
        index = [i for i in range(len(maxList)) if maxList[i] == maxLong][0]

        print maxLong,index

        pass


if __name__ == '__main__':
    s = Solution()
    s.longestPalindrome("bbbb")
    pass