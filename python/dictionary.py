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