sentence_example = "A e E eeee EEEE eeZ"

length = len(sentence_example)
a, c = sentence_example[0], sentence_example[-1]
print(f"{a} {c}")

reversed_1 = sentence_example[::-1] #or
print(f"{reversed_1}")

list_of_words = sentence_example.split()
lenggg = len(list_of_words)
print(list_of_words[-1])
print(list_of_words[0])

#IDK WHAT U MEAN for ste p3 

#I used a few f strings already 

if sentence_example == "":
    print("EMPTY")
    
    
    
    
#Write a Python function that
#returns a percentile (for example p50 or p99) from a list of latency numbers.


import math

def percentile(values, p):
    s = sorted(values)
    k = max(0, math.ceil(p / 100 * len(s)) - 1)
    return s[k]