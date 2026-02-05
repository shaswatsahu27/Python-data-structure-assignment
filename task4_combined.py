# Given data (from previous tasks)
products = ["Laptop", "Mobile Phone", "Headphones", "Smart Watch", "Camera", "Keyboard"]
categories = ["Electronics", "Electronics", "Accessories", "Wearable", "Electronics", "Accessories"]

price_dict = {
    "Laptop": 55000,
    "Mobile Phone": 28000,
    "Headphones": 2000,
    "Smart Watch": 8000,
    "Camera": 25000,
    "Keyboard": 1500
}

# 1. Create catalog list of tuples (product_name, price, category)
catalog = []

for i in range(len(products)):
    product = products[i]
    price = price_dict[product]
    category = categories[i]
    catalog.append((product, price, category))

print("Catalog:", catalog)

# 2. Create category_to_products dictionary
category_to_products = {}

for product, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []
    category_to_products[category].append(product)

print("Category to Products:", category_to_products)

# 3. Print products in the category with maximum number of products
max_category = None
max_count = 0

for category in category_to_products:
    count = len(category_to_products[category])
    if count > max_count:
        max_count = count
        max_category = category

print("Category with maximum products:", max_category)
print("Products in this category:", category_to_products[max_category])
