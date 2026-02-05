# Parallel list of categories matching the products list
products = ["Laptop", "Mobile Phone", "Headphones", "Smart Watch", "Camera", "Keyboard"]
categories = ["Electronics", "Electronics", "Accessories", "Wearables", "Electronics", "Accessories"]

# 1. Create a set of categories
categories_set = set(categories)S
print("Initial categories set:", categories_set)

# 2. Add a new category and show duplicates are ignored
categories_set.add("Gaming")
categories_set.add("Electronics")  # duplicate
print("Categories after adding new and duplicate:", categories_set)

# 3. Check if a category exists in the set
print("Is 'Electronics' in categories?", "Electronics" in categories_set)

# Extra (optional)
# Total number of unique categories
print("Total unique categories:", len(categories_set))
