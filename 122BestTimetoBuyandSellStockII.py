#encoding=utf8


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int],an array for which the ith element is the price of a given stock on day i.
        :rtype: int
        """
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))
        # pass



if __name__ == '__main__':

    S = Solution()
    S.maxProfit([])