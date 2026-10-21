"""
votes = ["yes", "no", "yes", "yes"]. Build count with a for loop and .get(), then print count, then print its keys as a list and its values as a list.

stock = {"apple": 0, "pear": 4}. Predict stock.get("apple"), stock.get("banana") and "apple" in stock. Then write an if/else using in that prints missing or the quantity for "banana". In one sentence, when would you pick .get() instead?

stats = {"goals": 3}. In two lines, add one goal and one assist (assists may not exist yet). What would stats["goals"] = 1 do instead?

players = [{"name": "Ana", "goals": 2}, {"name": "Ben", "goals": 4}]. Append a player named "Cal" with 0 goals, then print Cal’s name without using a number as an index.

Predict: {"Name": "Chris"}.get("name", "unknown"), list({"x": 1, "y": 2}.values()), len({"a": 1, "b": 2}) and "b" in {"a": 1, "b": 2}.
"""

#TASK ONE
votes = ["yes", "no", "yes", "yes"]
votes_dictionary = {}

for index, item in enumerate(votes):
    votes_dictionary[index] = item
    
print(len(votes_dictionary))
print(votes_dictionary.keys())
print(votes_dictionary.values())

#TASK TWO 
stock = {"apple": 0, "pear": 4} #Predict using get returns either the value or default set if applicable if not found
#Get is used if not sure if exists to prevent error 
for item in stock.keys():
    print(item) #for fun for loop
    
if stock.get("banana"):
    print(stock["banana"])
else:
    print("NOT FOUND")
    
#TASK THREE
stats = {"goals": 3}

stats["assists"] = stats.get("assists", 0) + 1
stats["goals"] = stats.get("goals", 0) + 1

#TASK FOUR
players = [{"name": "Ana", "goals": 2}, {"name": "Ben", "goals": 4}]

players.append({"name": "Cal", "goals": 0})

for item in players:
    if item["name"] == "Cal":
        print(item["name"])
        
#TASK FIVE
#Predict: {"Name": "Chris"}.get("name", "unknown"), list({"x": 1, "y": 2}.values()), len({"a": 1, "b": 2}) and "b" in {"a": 1, "b": 2}.
#If no chris become unknown for name...
#use 1, 2 as values, check the length of it being 2, and b is found in there so its True