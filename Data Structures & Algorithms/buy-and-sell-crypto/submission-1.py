class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far=prices[0]
        result=0
        for i in range(len(prices)):
            min_so_far=min(min_so_far,prices[i])
            result=max(result,prices[i]-min_so_far)
        return result
        