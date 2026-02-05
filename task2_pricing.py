# 1. Create a dictionary of product prices
price_dict = {
    "Laptop": 55000,
    "Mobile Phone": 30000,
    "Headphones": 2000,
    "Smart Watch": 8000,
    "Camera": 25000,
    "Keyboard": 1500
}

# Add a new product with price
price_dict["Mouse"] = 700

# Update the price of an existing product
price_dict["Mobile Phone"] = 28000

# Remove a product safely (handle non-existing product)
product_to_remove = "Tablet"
if product_to_remove in price_dict:
    del price_dict[product_to_remove]
else:
    print(product_to_remove, "not found in price list")

# 3. Calculate and print average price
total_price = sum(price_dict.values())
average_price = total_price / len(price_dict)
print("Average product price:", average_price)

# Extra (optional)
# Product with maximum and minimum price
max_product = max(price_dict, key=price_dict.get)
min_product = min(price_dict, key=price_dict.get)

print("Most expensive product:", max_product, "-", price_dict[max_product])
print("Least expensive product:", min_product, "-", price_dict[min_product])
