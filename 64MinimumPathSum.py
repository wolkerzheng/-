#encoding=utf8
"""
动态规划：

"""
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid and len(grid)==0 or len(grid[0])==0:
            return 0
        m,n = len(grid),len(grid[0])
        dp = [[float("inf")]*(n+1)]*(m+1)
        dp[0][1]=0
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i-1][j-1]
        return dp[m][n]

    def minPathSum1(self,grid):
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
S=Solution()
grid =
print S.minPathSum(grid)
