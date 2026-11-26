"""
Question 1. Given counts = {"apple": 2}, add one to "apple" and one to "pear", 
which isn't a key yet. Use .get() so neither line can raise KeyError. 
Then print just the keys and just the values as lists.
"""

counts = {"apple": 2}

counts["apple"] = counts.get("apple", 0) + 1
counts["pear"] = counts.get("pear", 0) + 1

print(list(counts.keys()))
print(list(counts.values()))

"""
Question 2. Spot the two bugs in this code. The player has just scored again and made an assist:

stats = {"goals": 3}
stats["goals"] = 1
stats["assists"] += 1
"""

stats = {"goals": 3}
stats["goals"] = stats.get("goals", 0) + 1 #was setting to 1 instead of adding
stats["assists"] = stats.get("assists", 0) + 1 #missing .get as no key

"""
Question 3. When do you use d[key], d.get(key, default), and key in d? Give one situation for each.
"""
#d[key] is used to access values from a key in a dict
#d.get(key, default) is used to get a value, albeit if no key no errror
#key in d, is used to check if key in dict

#Use [key] if key must exist, keyerror for bug, and .get if missing a key is fine, in to see if key is in 

"""
Question 4. Predict the output of this code, writing the exact printed text:

d = {"a": 1, "b": 2}
k = d.keys()
print(list(d.values()), list(d.items()))
d["c"] = 3
print(k)
"""

#1 2, a, b
#a, b, c  as dict keys

"""
Question 6. Given:

players = [{"name": "Ana", "stats": {"goals": 2}}, {"name": "Ben", "stats": {"goals": 4}}]

Without a loop, add one goal to Ana, append a new player Cal with 0 goals, and print Ben's goals. 
Write the code and the output you expect.
"""
players = [{"name": "Ana", "stats": {"goals": 2}}, {"name": "Ben", "stats": {"goals": 4}}]
players[0]["stats"]["goals"] += 1

players.append({"name": "Cal", "stats": {"goals": 0}})

print(players[1]["stats"]["goals"])

print(players) #to see for myself


"""
Question 7. Given stock = {"apple": 0, "pear": 4}, predict the output of each:

a) stock.get("apple")    0
b) stock.get("banana")   None
c) stock.get("banana", 0)  0
d) "apple" in stock  True
e) "banana" in stock  False

Then answer in one sentence: why is (c) a bad way to check whether banana is in stock?

It is bad due to the fact that if it isn't in stock, it still returns, albeit 0, as .get still returns,
as well, IF we stock it as an item, vs quantity in store, 0 is bad, so use in 
"""


"""
Question 8. Predict each output:

a) {"Name": "Chris"}.get("name")   None
b) {"Name": "Chris"}.get("name", "unknown")  unknown  
c) "apple" in {"apple": 0}     True
d) len({"a": 1, "b": 2})  2
"""


"""
Question 9. Using d = {"x": 1, "y": 2}, predict each output. The note says parts b and d need comprehensions, so skip those for now:

a) list(d.items())    x : 1, y : 2
c) d.get("X", "nope")  nope
e) after v = d.values() and then d["z"] = 3, what does list(v) show? 1, 2, 3 as values
"""


"""
Question 10a. Given:

matches = [
    {"player": "Ana", "scored": True},
    {"player": "Ben", "scored": False},
    {"player": "Ana", "scored": True},
    {"player": "Cal", "scored": True},
    {"player": "Ben", "scored": True},
]

Build goals as a dict counting how many times each player scored, 
counting only where scored is True. Use .get() for each increment. 
Expected: {"Ana": 2, "Cal": 1, "Ben": 1}. Paste your code and output.
"""

matches = [
    {"player": "Ana", "scored": True},
    {"player": "Ben", "scored": False},
    {"player": "Ana", "scored": True},
    {"player": "Cal", "scored": True},
    {"player": "Ben", "scored": True},
]

goals = {}

for match in matches:
    if match.get("scored") == True:
        goals[match["player"]] = goals.get(match["player"], 0) + 1
        
print(goals)