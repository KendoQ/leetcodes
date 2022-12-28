# Given a list of stock prices for n days return the maximum
# profit with a single buy/sell transaction.

# Constraints:
# 1 <= n <= 10^5
# 1 <= price <= 10^4

# Example:
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 
# (price = 6), profit = 6-1 = 5.

# Since a sell cannot happen before a buy, we only pass
# through the array a single time. A solution will find
# lowest buy price and highest sell price in a single
# pass we do this in a two-pointer-ish way buy either moving
# the buy or sell price at each index and tracking the
# max profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize pointer. We only need 1 to track
        # the buy price. Initialize max profit
        P = prices[0]
        res = 0

        # Loop over each price
        for price in prices:

            # If we find a lower price, buy here
            if price < P:
                P = price

            # If we can increase profit, sell here
            elif price - P > res:
                res = price - P

            # In any other case, continue
            else:
                continue
        
        # return result
        return res
    # We pass through the array only once, using 
    # two integers for the buy and sell price
    # Time: O(n), Space: O(1)