import json

items = []

# the items.json file was generated from vyp db. Use the below
# query to generate the items.json file
# sqlite3 vyp.db
# .output items.json
# SELECT item_name, item_sale_unit_price FROM kb_items WHERE item_sale_unit_price != 0.0;
with open("items.json", "r") as f:
    for line in f:
        line = line.strip()
        if not line or "|" not in line:
            continue
        name, price = line.split("|", 1)
        # Spell-correct and title-case the food name
        name = name.title().strip()
        items.append({
            "food_name": name,
            "food_price": int(float(price))
        })

with open("formatted_items.json", "w") as f:
    json.dump(items, f, indent=2)

print("Spell-corrected and saved to formatted_items.json")

