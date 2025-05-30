# Step 1: Create empty inventory dictionary
inventory = {}  # DICTIONARY: key = gadget name (string), value = quantity (int)

# Step 2: Add gadgets to inventory
inventory["laptop"] = 15
inventory["smartphone"] = 30
inventory["headphones"] = 20
inventory["smartwatch"] = 10

# Step 3: Update quantity (got a shipment!)
inventory["smartphone"] += 5   # Increase smartphones by 5 (using += operator)

# Step 4: Access quantity of an item
laptop_qty = inventory["laptop"]
print("Quantity of laptops:", laptop_qty)

# Step 5: List all items and quantities using dictionary method .items()
print("\nInventory Items and Quantities:")
for gadget, qty in inventory.items():
    print(f"{gadget}: {qty}")

# Step 6: Using list methods and slicing
gadget_list = list(inventory.keys())  # Convert dictionary keys to a list
print("\nAll gadgets:", gadget_list)
print("First 3 gadgets:", gadget_list[:3])        # Slicing first 3
print("Reversed gadget list:", gadget_list[::-1]) # Slicing with step -1 (reverse)

# Step 7: Tuple example (immutable pair)
smartwatch_tuple = ("smartwatch", inventory["smartwatch"])
print("\nTuple example:", smartwatch_tuple)

# Step 8: Bonus - Check if an item exists
check_gadget = "tablet"
if check_gadget in inventory:
    print(f"\n{check_gadget} is in inventory, quantity: {inventory[check_gadget]}")
else:
    print(f"\n{check_gadget} NOT found in inventory.")

# Step 9: Remove an item using pop()
removed = inventory.pop("headphones", None)
print("\nRemoved item:", removed)
print("Updated inventory:", inventory)

# Step 10: Extra List method - sort gadgets alphabetically
sorted_gadgets = sorted(gadget_list)
print("\nSorted gadgets:", sorted_gadgets)