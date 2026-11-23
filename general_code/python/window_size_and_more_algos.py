def max_window_sum(nums, window_size):
    largest_sum = sum(nums[0:window_size])

    index = 0
    while index <= len(nums) - window_size:
        total = sum(nums[index:index+window_size])
        
        if total > largest_sum:
            largest_sum = total
    
        index+=1
    return largest_sum


def max_window_sum_improved(nums, window_size): 
    window_total = sum(nums[0:window_size])
    largest_sum = window_total

    index = 1
    while index <= len(nums) - window_size:
        window_total = window_total - nums[index-1] + nums[index+window_size-1]

        if window_total > largest_sum:
            largest_sum = window_total

        index += 1
        
    return largest_sum
    


def window(nums, size):
    win_num = sum(nums[0:size])
    largest = win_num
    
    index = 1
    
    while index <= len(nums) - size:
        win_num = win_num - nums[index - 1] + nums[index + size - 1]
        
        if win_num > largest:
            largest = win_num
    
        index+=1
        
    return largest







def window_calc(nums, window_size):
    window_sum = sum(nums[0:window_size])
    largest = window_sum
    index = 1
    
    while index <= len(nums) - window_size:
        window_sum = window_sum - nums[index - 1] + nums[index + window_size -1]
        
        if window_sum > largest:
            largest = window_sum
        
        index+=1
            
    return largest




def win(nums, size):
    win_total = sum(nums[0:size])
    largest = win_total
    index = 1
    
    while index <= len(nums) - size:
        win_total = win_total - nums[index - 1] + nums[index + size - 1]
        
        if win_total > largest:
            largest = win_total
        
        index+= 1
        
    return largest













def win_calc(nums, win_size):
    win_total = sum(nums[0:win_size])
    largest = win_total
    index = 1
    
    while index <= len(nums) - win_size:
        win_total = win_total - nums[index - 1] + nums[index - 1 + win_size]
        
        if win_total > largest:
            largest = win_total
        
        index+=1
        
    return largest




def calc(nums, size):
    win_total = sum(nums[0:size])
    largest = win_total
    index = 1
    
    while index <= len(nums) - size:
        win_total = win_total - nums[index - 1] + nums[index - 1 + size]
        
        if win_total > largest:
            largest = win_total
        
        index+=1
        
    return largest


def win_movement(nums, size):
    win_total = sum(nums[0:size])
    largest = win_total
    index = 1
    
    while index <= len(nums) - size:
        win_total = win_total - nums[index - 1] + nums[index - 1 + size]
        
        if win_total > largest:
            largest = win_total
        
        index+=1
    return largest

max_window_size = 2
nums = [5, 1, -10, 4]
#print(max_window_sum_improved(nums, max_window_size))











#############################################################################Stock Problem
"""
For the stock problem, the prices are [2, 4, 1], one per day. You buy on one day and sell on a later day.
The profit is the sell price minus the buy price.

Your question: What’s the biggest profit you could make from [2, 4, 1], and which days would you buy and sell on?
"""

def best_buy_time_sell_time(prices):
    prices = [2, 4, 1]
    lowest = prices[0]
    best = 0
    
    for price in prices:
        if price - lowest > best:
            best = price - lowest
        if price < lowest:
            lowest = price
    return best

def calc_best_buy(prices):
    profit = prices[0] - prices[1]

    day_buy = 0
    day_sell = 1
    day_buy_price = prices[0]
    day_sell_price = prices[0]

    index = 0 
    while index < len(prices):
        if day_buy_price > prices[index] and index < day_sell:
            day_buy_price = prices[index]
            day_buy = index
        
        if day_sell_price < prices[index] and index > day_buy:
            day_sell_price = prices[index]
            day_sell = index
        
        index+=1
    profit = day_sell_price - day_buy_price

    print(f"profit: {profit} - Day Buy: {day_buy} - Day Sell: {day_sell}- Day Buy_price: {day_buy_price} - Day Sell_price: {day_sell_price}")

prices = [2, 4, 1]
calc_best_buy(prices)




def best_profit(prices):
    lowest = prices[0]
    best = 0

    for price in prices:
        if price - lowest > best:
            best = price - lowest
        if price < lowest:
            lowest = price

    return best

print(best_profit([2, 4, 1]))   # 2
print(best_profit([3, 1, 2]))   # 1
print(best_profit([7, 6, 4, 3, 1]))  # 0