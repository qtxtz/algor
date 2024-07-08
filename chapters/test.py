from collections import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minVal = float('inf')
        for p in prices:
            if p < minVal:
                minVal = p
            if p - minVal > profit:
                profit = p - minVal
        return profit