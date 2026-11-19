
def is_palindrome(s):
    x = 0
    y = len(s) - 1
    
    while x < y:
        if s[x] != s[y]:
            return False
        
        x+=1
        y-=1
    
    return True

#it is O(n) for time and O(1) for space as no lists of values. ::-1 is worse
#for space it creates a new list for space making it O(n)

##2:
nums = [1,2,3,44,44,33,2]

for i in range(len(nums)): 
    if nums[i] > nums[i + 1]: #the bug is that it will exceed the value of the length items
        print("")
#To fix it, the range should be in range(len(nums) -1)

#3 -No clue.. i didnt do this personally
#I assume it is better as it allows to iterate through linearly


#4 banana should be text.   p returns 2

#5 prefix is a and suffix is c, the start and last. the first val in a collection

#6 
def first_greater(nums, target):
    
    for index, i in enumerate(nums):
        if i > target:
            return index
        
    return -1 #nothing found

#7 new again not done...

#8 it is O(1) when no lists are stored but just vars
def count(c):
    tally = {}
    for chars in c:
        tally[chars] = tally.get(chars, 0) + 1
        
    return tally
        
