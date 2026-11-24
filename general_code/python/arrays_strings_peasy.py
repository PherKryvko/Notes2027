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

