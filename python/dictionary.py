words = {
    "Value": "new",
    "Value2": "brand",
    "Value3": "Goal"
}


total = 0
for key, value in words.items():
    total += 1
print(f"total: {total}")

print(words.get("Value", "Not Found"))

"""
Spot the two bugs (the player has just scored again and made an assist):
"""
stats = {"goals": 3}
#stats["goals"] = 1
#stats["assists"] += 1
"""should become"""
stats["goals"] += 1
stats["assists"] = stats.get("assists", 0) + 1
print(stats)



d = {"a": 1, "b": 2}
k = d.keys()
print(list(d.values()), list(d.items()))
d["c"] = 3
print(k)

#prediction: 1, 2...  a1 b2.....  a.b.c

"""
Write a dict comprehension: from prices = {"apple": 0.5, "melon": 2.0, "kiwi": 0.3} build a dict of items under £1 with the price in pence. Then invert a dict.

!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""

"""
Write from memory: given counts = {"apple": 2},
add one to "apple" and one to "pear" (not yet a key) using .get(), 
so neither line can raise KeyError.
Then show just the keys and just the values as lists.
"""
counts = {"apple": 2}

counts["apple"] += 1
counts["pear"] = counts.get("pear", 0) + 1
print(counts.keys())
print(counts.values())


""" Spot bugs
stats = {"goals": 3}
stats["goals"] = 1
stats["assists"] += 1
"""

stats = {"goals": 3}
stats["goals"] += 1
stats["assists"] = stats.get("assists", 0) + 1 
#print(stats)


"""
Given players = [{"name": "Ana", "stats": {"goals": 2}}, {"name": "Ben", "stats": {"goals": 4}}], 
without a loop: add one goal to Ana, append a new player Cal with 0 goals, and print Ben's goals.
"""
players = [{"name": "Ana", "stats_": {"goals": 2}}, {"name": "Ben", "stats_": {"goals": 4}}]
players[0]["stats_"]["goals"] += 1
print(players[0])

players.append({"name": "cal", "stats_": {"goals": 0}})
print(players[players.count(key) - 1])

print(players[1]["stats_"]["goals"])