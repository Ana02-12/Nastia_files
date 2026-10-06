def maxProfit(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        #«Если сегодня продать,
        #сколько я заработаю,
        #если купить по самой дешёвой цене,
        #которую видел раньше?»
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

#prices = [7,1,5,3,6,4]
prices = [24, 23, 22, 21, 25]
print(maxProfit(prices))
