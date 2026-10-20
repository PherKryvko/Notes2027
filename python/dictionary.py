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
"""
