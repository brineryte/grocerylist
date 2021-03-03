import json

with open("Data/tonight.json", "r") as f:
    meals = json.load(f)

all_items = []
for items in meals.values():
    all_items += items

print("\n".join(set(all_items)))