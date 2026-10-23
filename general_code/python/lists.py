"""
Given nums = [3, -1, 4, -1, 5], write lines that produce, 
without changing nums, 

a sorted copy, 
a reversed copy, 
and the total, smallest and largest values. 

Then predict what print(nums.reverse()) shows and what nums is afterwards.
"""
nums = [3, -1, 4, -1, 5]

sorted_nums = sorted(nums)
reversed_nums = reversed(nums)
total_nums = sum(nums)
smallest_nums = min(nums)
largest_nums = max(nums)
#it reverses it to this 5, -1, 4, -1, 3 and the operation shows None

print(nums.reverse())

print(nums)