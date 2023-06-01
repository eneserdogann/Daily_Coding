prices = [7,1,5,3,6,4]

def maxProfit(prices) -> int:
    if len(set(prices)) < 2:
        return 0
    maxprofit = 0
    minprofit = prices[0]
    for i in range(1, len(prices)):
        maxprofit = max(maxprofit, prices[i] - minprofit)
        minprofit = min(minprofit, prices[i])
    return maxprofit

print(maxProfit(prices))