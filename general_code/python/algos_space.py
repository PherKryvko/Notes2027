
n = [1,2,3,3,3,33,333,444]

def reverse(n):
    n = reversed(n)
    return n    

print(list(reverse(n)))

l = [1,2,333,33]
l = l[::-1] #o(1) o(n) space
l = reverse(l) #o(n) o(n) space
