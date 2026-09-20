class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        minPrice = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            sellToday = prices[i] - minPrice
            if sellToday > maxProfit:
                maxProfit = sellToday
            if prices[i] < minPrice:
                minPrice = prices[i]
        return maxProfit