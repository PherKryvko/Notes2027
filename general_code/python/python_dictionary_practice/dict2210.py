"""
Write down what you expect tally to print.
Build tally from an empty dict with a for loop, using .get() for every increment.
Print tally.
Print the keys as a list, then the values as a list.
"""
pets = ["cat", "dog", "cat", "bird", "cat", "dog"]  #3 cat, 2 dog, 1 bird

tally = {}

for pet in pets:
    tally[pet] = tally.get(pet, 0) + 1
    
print(tally)
print(list(tally.keys()))
print(list(tally.values()))


"""
Predict each output as a comment: stock.get("pear"), stock.get("fig"), stock.get("fig", 0), "pear" in stock, "fig" in stock.
Write an if/else using in that prints exactly missing if "fig" isn’t a key, otherwise prints its quantity.
In one sentence: why is if stock.get("pear"): a bad way to check that pear is in stock?
"""
stock = {"pear": 0, "plum": 5} #0, None, 0, True, False

if "fig" in stock:
    print(stock["fig"])
else:
    print("missing")
    
#it's a bad way as if it is zero value, it treats it as a false.


"""
Add one goal in one line, using +=.
What would stats["goals"] = 1 do instead? One sentence.
Add one to "saves", which isn’t a key yet, in one line, without it crashing.
"""
stats = {"goals": 3, "assists": 1}
stats["goals"] += 1 #just =1 would set it to 1
stats["saves"] = stats.get("saves", 0) + 1


"""
Append a player named "Cal" with 0 goals. Then, without writing a number like [2] as the index, print the new player’s name.
"""
players = [{"name": "Ana", "goals": 2}, {"name": "Ben", "goals": 4}]

players.append({"name": "Cal", "goals": 0})
print(players[-1]["name"]) #isn't 2 OR

#A for loop version
for player in players:
    if player["name"] == "Cal":
        print(player["name"])

    
"""
{"Name": "Chris"}.get("name", "unknown")   #name isn't matching Name
list({"x": 1, "y": 2}.values()) #1, 2
len({"a": 1, "b": 2}) #2
"b" in {"a": 1, "b": 2} #True
"""

