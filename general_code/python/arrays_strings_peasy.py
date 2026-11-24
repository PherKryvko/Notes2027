"""
write is_palindrome(s) with two pointers, state its time and extra space, and say why s[::-1] costs more space.
"""

#Time is O(n)
#Auxilary Space is O(1) 
#::1 costs more as it is creating a brand new string 

def is_palindrome(word):
    left = 0
    right = len(word) -1 
    
    while left < right:
        if word[left] != word[right]:
            return False
        
        right -=1
        left+=1
        
    return True

print(is_palindrome("EEEEE"))


"""
Count character frequencies in a string with a loop, with no Counter. What is the space complexity, and when is it O(1)?
"""
def character_frequencies(string):
    char_freq = {}
    
    for char in string:
        char_freq[char] = char_freq.get(char, 0) + 1
        
    return char_freq

hello = "Hello"
new_char_dict_tally = character_frequencies(hello)

print(new_char_dict_tally) #O(n) space complexity, O(n) time, it is only o(1) if it isn't a collective of data and just singular totals or one key


"""
**Question 3:** Write a fixed-size sliding window that returns the maximum sum of any k 
consecutive numbers. Why is `new_sum = old_sum - leaving + entering` better than re-summing each window?
"""
def window_slide(nums, window_size):
    window_sum = sum(nums[0:window_size])
    largest = window_sum
    
    index = 1
    
    while index <= len(nums) - window_size:
        window_sum = window_sum - nums[index -1] + nums[index - 1 + window_size]
        
        if window_sum > largest:
            largest = window_sum
        
        index+=1
            
    return largest

#it is better as it reduces the o(n*k) to o(1) for big-time per step

"""
Question 6: Write first_greater(nums, target) using enumerate(). 
It should return the index of the first value greater than target, or -1 if there isn't one. Where must the return -1 go, and why?
"""

def first_greater(nums, target):

    for index, n in enumerate(nums):
        if n > target:
            return index
        
    return -1 #goes here as if no result, it needs a return of -1

"""
Question 7: Best Time to Buy and Sell Stock. 
Write a one-pass best-so-far solution and state its complexity.
Why update the minimum price before, or independently of, the profit?
"""
"""
lowest so far: the cheapest price you've seen on any earlier day, which is the best day to have bought.
best profit so far: the most you could have made.
"""

def best_buy(l):
    
    lowest_purchase_total = l[0]
    best = 0
    
    for i in l:
        if i < lowest_purchase_total:
            lowest_purchase_total = i
            
        sell_amount = i - lowest_purchase_total
        if sell_amount > best:
            best = sell_amount
    
    return best


print(best_buy([7, 1, 5, 3, 6, 4]))

