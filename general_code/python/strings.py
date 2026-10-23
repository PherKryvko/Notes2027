"""
Part 1: Predict the output

s = "Hello, World". What do s[::3], s[-1:-6:-1] and s[7:] give?
1: 3 skips in 3 iterations, so Hl r
2: #World
3: W

"ab" * 3 + "c" * 0 + "!"
#ababab!

" Python ".strip().upper().replace("O", "0")
#PYTH0N

"a,b,,c".split(",") and "one two three".split(" "). Why do they differ from "one two three".split()?
#First uses commas to split ,second uses spaces albeit you can just do .split() for space?

"Mississippi".count("ss") and "Mississippi".find("ss", 3)
#2 & 5 as it starts from 3 and has past the first ss

"Z" < "a" and "apple" < "apricot". Why do these give the results they do?
 True, True.  A is higher in value and apple is smaller than apricot in text length
"""



""" Spot bug
greeting = "Hi" followed by greeting.append("!"). What error, and how do you fix it?
total = "5" + 5. What error, and what are two ways to fix it?

"""

greeting = "Hi" #as append is list
greeting = greeting + "!"
print(greeting)

total = int("5") + 5
#OR
total = float("5") + 5

"""QUICK TESTS"""
#Turn " the QUICK brown fox " into "The Quick Brown Fox".
sentence = " the QUICK brown fox "
sentence = sentence.strip().lower().title()
print(sentence)

#From email = " Chris.Elliott@DXC.com ", produce the lowercase username before the @, with no spaces.
email = " Chris.Elliott@DXC.com "
email = email.strip()
index = email.find("@")
temp_email_name = email[0:index]
temp_email_name = temp_email_name.lower()
temp_email_name = temp_email_name + email[index::]
print(temp_email_name)
email = email

#OR
email = " Chris.Elliott@DXC.com "
email = email.strip()
email_parts = email.split("@")
email_parts[0] = email_parts[0].lower()
email = email_parts[0] + "@" + email_parts[1]
print(email)

"""
extract the filename without its extension, giving "q3".
"""
path = r"C:\Users\Chris\Reports\2026\q3.xlsx"
path_split = path.split("\\")
print(path_split[-1])
path_index_dot = path_split[-1].find(".")
path_filename = path_split[-1][0:path_index_dot]
print(path_filename)

"""
Mask a card number so "4111111111111234" becomes "************1234". The length must work for any card number.
"""
card_number = "4111111111111234"
card_ending = card_number[len(card_number) - 4::]
length = len(card_number) - 4
card_rest = "*" * length
print(card_rest + card_ending)

"""
Print a row with name = "Alice" and score = 93.456 so the name is left-aligned in 10 characters, 
then |, then the score right-aligned in 8 characters to 1 decimal place.
"""
name = "Alice" 
score = 93.456
print(f"{name:<10} | {score:>8.2f}") 


"""
Check whether "Never odd or even" is a palindrome, ignoring spaces and case.
"""
def is_palindrome():    
    left = 0
    right = len(palindrome_fixed) -1 
    
    while left < right:
        if palindrome_fixed[left] != palindrome_fixed[right]:
            return False
        
        left+=1
        right-=1
    return True

palindrome = "Never odd or even" 

palindrome_fixed = palindrome.lower().replace(" ", "")
print(palindrome_fixed)

palindrome_check = is_palindrome()


"""
Count the vowels in "Programming is fun", ignoring case.

A, E, I, O, U
"""
sent = "Programming is fun"

total_vowels = 0

for char in sent:
    char_lowered = char.lower()
    
    match char_lowered:
        case "a":
            total_vowels+= 1
        case "e":
            total_vowels+=1
        case "i":
            total_vowels+=1
        case "o":
            total_vowels+=1
        case "u":
            total_vowels+=1 
    
print(f"VOWELS {total_vowels}")


"""
How many bytes does "€" take in UTF-8, and what is len("€")? Explain the difference between the two numbers.
"""
#bytes is memory, who knows as this isnt needing to be known.... 
#it will be more however, than the len that is 1 