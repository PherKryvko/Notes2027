#Given counts = {"apple": 2}, add one to "apple", and add one to "pear" 
# without causing a KeyError. Then show just the keys and just the values as lists.

counts = {"apple": 2}

counts["apple"] = counts.get("apple", 0) + 1
counts["pear"] = counts.get("pear", 0) + 1

print(list(counts.keys()))
print(list(counts.values()))