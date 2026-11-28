"""List Transformer (micro-project 02). Write each step yourself, then check with the prints.

Run with:  python list_transformer.py
"""


def show(label, value):
    print(f"{label}: {value}")


# Build 1: create a shopping list
shopping = ["milk", "eggs", "bread"]
show("start", shopping)

# Build 2: append, extend, remove and pop deliberately.
# TODO: append one item, extend with two items, remove one item by value, pop the last item.
# Print the list and the return value after each one.
shopping.append("E")
shopping.extend(["Q", "W"])
shopping.remove("milk")
what = shopping.pop(-1)

# Build 3: reversed copy, then reverse in place.
# TODO: make rev = a reversed copy with [::-1]; check shopping is unchanged.
# TODO: then call shopping.reverse() on its own line; check it returns None.
rev = shopping[::-1]
if shopping.reverse() == None:
    print("WOO")

# Verify: a reversed copy must not change the original.
# TODO: add an assert for each rule the note lists.
#Not done asserts yet