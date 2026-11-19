"""
Write one function, inspect(sentence), that returns a dictionary. Then call it on a sentence and print the results.

Think of it in three parts, one per line of code:

Check the input. If the sentence is empty or only spaces, raise an error: ValueError, with a message. 
This is the same check as the empty-list check for average.

Work out the values. Each dictionary key gets one value:
length: how many characters
first_char and last_char: the first and last characters
reversed: the sentence backwards
words: the list of words
word_count: how many words there are
Return the dictionary. Put the values under their key names, then return it.

Outside the function, call it on a test sentence and print each key.

Write the function and the call, then paste the code and the printed output. Start with the empty check.

"""

sentence = "we are here today, gathered by our enemies and the fruitful vanguard amongst ourselves"

def avg(sentence):
    if len(sentence.strip()) == 0:
        raise ValueError("No text")

def dict_return(sentence):
    avg(sentence)
    
    dict_ = {}
    dict_["length"] = len(sentence)
    
    dict_["first_char"] = sentence[0]
    dict_["last_char"] = sentence[-1]
    dict_["reversed"] = sentence[::-1]
    dict_["words"] = sentence.split()
    dict_["word_count"] = len(sentence.split())
    
    return dict_

dict_return_ = {}
dict_return_ = dict_return(sentence)
print(f"{list(dict_return_.keys())} = {list(dict_return_.values())}")

























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



#Unseen problem: “Given a list of transaction IDs, return 
#the first ID that appears twice.” List your first steps in order, 
# then write the efficient solution and state its time and space.

def return_transaction_match_found(transactions):
    transactions = [1,2,3,33,33,33,2123,2131232134]
    
    new_dict = {}
    
    for t in transactions:
        new_dict[t] = new_dict.get(t, 0) + 1
        if new_dict[t] > 1:
            return t
    #o(n), o(n)
    
    
def seen(listed):
    saw = set()
    for t in transactions:
        if t in saw:
            return t
        saw.add(t)  
    return None