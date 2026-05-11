# prices = [7,6,4,3,1]
prices = [7,1,5,3,6,4]


def maxProfit(prices):
	# On2 time, 01 space
	# max_profit = 0
	# for i, val1 in enumerate(prices):
	# 	for j in range(i+1, len(prices)): 
	# 		if val1 < prices[j]:
	# 			new_max_profit = prices[j] - val1
	# 			if  new_max_profit > max_profit:
	# 				max_profit = new_max_profit
	
	# return max_profit

	# On time, 01 space
	max_profit = 0
	buy_price = prices[0]
	for sell_price in prices:
		if sell_price <= buy_price:
			buy_price = sell_price
		else:
			max_profit = max(max_profit, sell_price - buy_price)

	return max_profit				

			
res = maxProfit(prices)
print('Results: ', res)	
