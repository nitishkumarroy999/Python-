# Python 3 program for the above approach


# Function to find maximum profit possible
# by buying and selling at most one stack
def findMaximumProfit(prices, i, k,
					buy, v):

	# If no stock can be chosen
	if (i >= len(prices) or k <= 0):
		return 0

	if (v[i][buy] != -1):
		return v[i][buy]

	# If a stock is already bought
	if (buy):
		v[i][buy] = max(-prices[i]
						+ findMaximumProfit(prices, i + 1,
											k, not buy, v),
						findMaximumProfit(prices, i + 1, k,
										buy, v))
		return v[i][buy]

	# Otherwise
	else:
		# Buy now
		v[i][buy] = max(prices[i]
						+ findMaximumProfit(
			prices, i + 1, k - 1, not buy, v),
			findMaximumProfit(prices, i + 1, k,
							buy, v))
		return v[i][buy]


# Function to find the maximum
# profit in the buy and sell stock
def maxProfit(prices):

	n = len(prices)
	v = [[-1 for x in range(2)]for y in range(n)]

	# buy = 1 because atmost one
	# transaction is allowed
	return findMaximumProfit(prices, 0, 1, 1, v)


# Driver Code
if __name__ == "__main__":

	# Given prices
	prices = [7, 1, 5, 3, 6, 4]

	# Function Call to find the
	# maximum profit possible by
	# buying and selling a single stock
	ans = maxProfit(prices)

	# Print answer
	print(ans)
