words = ["red", "blue", "red", "green", "blue", "red"]
count = {}

for word in words:
    count[word] = count.get(word, 0) + 1
    
print(list(count.keys()) + list(count.values()))

"""
Using the tally from Q4 (the one with red, blue and green):

a) Get the keys as a list.
b) Get the values as a list.
c) Find the total number of words using .values() and sum().

Expected output: the keys list ['red', 'blue', 'green'], the values list [3, 2, 1], and a total of 6.
"""
print(list(count.keys()))
print(list(count.values()))
print(sum(count.values()))


"""
team = [{"name": "Ana", "goals": 2}, {"name": "Ben", "goals": 4}]
Add a new player, Dan, with 1 goal to the end of team.
Print Dan’s name without using a number like [2]. Use [-1] instead.
"""
team = [{"name": "Ana", "goals": 2}, {"name": "Ben", "goals": 4}]
team.append({"name": "Dan", "goals": 1})
print(team[-1]["name"])


"""
Try g now: write an if/else that prints missing if banana isn’t a key, and otherwise prints its quantity.

"""
stock = {"apple": 0, "pear": 4}

if "banana" in stock:
    print(stock["banana"])
else:
    print("missing")
    
    
    
    
"""
names = ["Ana", "Ben", "Ana", "Ana"]
counts = {}
for name in names:
    counts[name] += 1
print(counts.keys)

Fix it so the output is {'Ana': 3, 'Ben': 1}.
"""

names = ["Ana", "Ben", "Ana", "Ana"]
counts = {}
for name in names:
    counts[name] = counts.get(name, 0) + 1
    
print(counts)


"""
matches = [
    {"player": "Ana", "scored": True},
    {"player": "Ben", "scored": False},
    {"player": "Ana", "scored": True},
    {"player": "Cal", "scored": True},
    {"player": "Ben", "scored": True},
]
Build a dict called goals that counts how many times each player scored. 
Only count the rows where scored is True, and use .get() for each increment.

Expected: {"Ana": 2, "Cal": 1, "Ben": 1}
"""
matches = [
    {"player": "Ana", "scored": True},
    {"player": "Ben", "scored": False},
    {"player": "Ana", "scored": True},
    {"player": "Cal", "scored": True},
    {"player": "Ben", "scored": True},
]

players_goals = {}

for match in matches:
    if match["scored"] == True:
        players_goals[match["player"]] = players_goals.get(match["player"], 0) + 1

print(players_goals)