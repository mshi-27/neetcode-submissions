class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        buy_ind = 0
        sell_ind = 1
        res = prices[sell_ind] - prices[buy_ind]
        while (sell_ind < len(prices) - 1):
            sell_ind += 1
            if prices[sell_ind - 1] < prices[buy_ind]:
                buy_ind = sell_ind - 1
            res = max(res, prices[sell_ind] - prices[buy_ind])
        return max(0, res)