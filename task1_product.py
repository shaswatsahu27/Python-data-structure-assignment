# 1. Create a list of products
products = ["Laptop", "Mobile Phone", "Headphones", "Smart Watch", "Camera", "Keyboard"]

# 2. Create a tuple for a sample product
sample_product = ("Laptop", 55000, "Electronics")

# 3. Print the 2nd and last product from the list
print("2nd product:", products[1])
print("Last product:", products[-1])

# 4. Append two new products and print updated list
products.append("Mouse")
products.append("Tablet")
print("Updated products list:", products)

# Extra (optional)
# Convert tuple to list, change price, and convert back to tuple
sample_product_list = list(sample_product)
sample_product_list[1] = 52000  # updated price
sample_product = tuple(sample_product_list)

print("Updated sample product tuple:", sample_product)
