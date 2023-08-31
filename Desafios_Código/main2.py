def search_products_by_price(min_price):
    found_products = []
    for product, data in inventory.items():
        if data["price"] >= min_price:
            found_products.append((data["id"], product))

    return found_products

inventory = {
    "Product A": {
        "id": 1,
        "price": 10.0,
        "quantity": 10
    },
    "Product B": {
        "id": 2,
        "price": 15.0,
        "quantity": 20
    },
    "Product C": {
        "id": 3,
        "price": 8.0,
        "quantity": 15
    }
}

min_price = float(input())
found_products = search_products_by_price(min_price)
print(found_products)
if found_products:
    print("Products Found:")
    for i in found_products:
        print(i[0], '-', i[1])
else:
    print("No product found.")