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





max_window_size = 2
nums = [5, 1, -10, 4]
print(max_window_sum_improved(nums, max_window_size))