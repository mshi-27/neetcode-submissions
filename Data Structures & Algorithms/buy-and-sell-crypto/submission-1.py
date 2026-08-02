class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sorted_prices = sorted(prices)
        d = defaultdict(list) # val to indices in sorted 
        res = 0
        for i, num in enumerate(sorted_prices):
            d[num].append(i)
        
        for i, price in enumerate(prices):
            if i == len(prices) - 1:
                break
            sorted_prices[d[price][0]] = None
            d[price].pop(0)
            tail = len(sorted_prices) - 1
            print(price)
            print(tail)
            print(d)
            print(sorted_prices)
            while sorted_prices[tail] == None:
                tail -= 1
            profit = sorted_prices[tail] - price

            print(profit)
            res = max(res, profit)
        return res
