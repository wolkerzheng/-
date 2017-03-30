#encoding=utf8
"""
给定一个字符串s，将s分割成一些子串，使每个子串都是回文。

返回s符合要求的的最少分割次数。
dp[i][j] = min(dp[i][k]+dp[k+1][j]+1)
optm:
dp[j] = dp[i-1]+1

 dp[i] - 表示子串（0，i）的最小回文切割，则最优解在dp[s.length-1]中。（0,i）的子串中包括了i+1个字符。
 分几种情况：
  1.初始化：当字串s.substring(0,i+1)(包括i位置的字符)是回文时，dp[i] = 0(表示不需要分割)；否则，dp[i] = i（表示至多分割i次）;
  2.对于任意大于1的i，如果s.substring(j,i+1)( 1 =< j <=  i ,即遍历i之前的每个子串)是回文时，dp[i] = min(dp[i], dp[j-1]+1);
   (注：j不用取0是因为若j == 0，则又表示判断（0，i）)。
"""
class Solution(object):
    def minCut(self, s):
        """
        dp[i] - 表示子串（0，i）的最小回文切割
        1.初始化：当字串s.substring(0,i+1)(包括i位置的字符)是回文时，dp[i] = 0(表示不需要分割)；否则，dp[i] = i（表示至多分割i次）;
        2.对于任意大于1的i，如果s.substring(j,i+1)( 1 =< j <=  i ,即遍历i之前的每个子串)是回文时，dp[i] = min(dp[i], dp[j-1]+1);
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0 for _ in range(n)]
        for i in range(0, n):
            if isPalindrome(s[0:i + 1]):
                dp[i] = 0
            else:
                dp[i] = i

        for i in range(1,n):

            for j in range(i,0,-1):
                if isPalindrome(s[j:i+1]):
                    dp[i] = min(dp[i],dp[j-1]+1)

        return dp[n-1]

    def minCut1(self,s):
        """"
        o(n) 空间，简单
        大体思路和之前一个一样
        在判断回文部分进行了优化，时间简短
        """
        n = len(s)
        dp = [0 for _ in range(n+1)]
        for i in range(0, n+1):

            dp[i] = i-1

        for i in range(0, n):
            j=0
            # 奇数情况
            while  i-j>=0 and i+j<n and s[i-j]==s[i+j]:

                dp[i+j+1] = min(dp[i+j+1],1+dp[i-j])
                j += 1
            j = 1
            #偶数情况
            while i-j+1 >= 0 and i + j < n and s[i-j+1] == s[i + j]:
                dp[i + j+1] = min(dp[i + j+1], 1 + dp[i-j+1])
                j +=1
        return dp[n]
        pass
def isPalindrome(string):
    """
    判断是否为回文串
    双向指针
    :param string:
    :return:
    """
    start,end = 0,len(string)-1

    while start <= end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1

    return True

if __name__ == '__main__':

    string = "leet"
    for s in ['leet','ab','aab',"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"]:
        a = Solution()
        # print a.minCut(s)
        print a.minCut1(s)
