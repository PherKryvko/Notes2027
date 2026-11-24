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