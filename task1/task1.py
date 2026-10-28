""" Task: 
● Product Catalogue Cleaner: A supplier sends a raw product list with mixed types,duplicates, and missing values. Clean the data, convert all prices to float, group products into a dictionary by category, and print a neat summary."""

products = [
    {"name": "Laptop", "price": "50000", "category": "Electronics"},
    {"name": "Mouse", "price": 1500, "category": "Electronics"},
    {"name": "Laptop", "price": "50000", "category": "Electronics"},
    {"name": "Shirt", "price": None, "category": "Clothing"},
    {"name": "Shoes", "price": "3000", "category": "Clothing"},
]

catalogue = {}
seen = set()

for product in products:

    name = product["name"]
    price = product["price"]
    category = product["category"]

    if not name or price is None or not category:
        continue

    try:
        price = float(price)
    except (ValueError, TypeError):
        continue

    key = (name, price, category)

    if key in seen:
        continue

    seen.add(key)
    if category not in catalogue:
        catalogue[category] = []

    catalogue[category].append({
        "name": name,
        "price": price
    })

for category, items in catalogue.items():

    print("\nCategory:", category)

    for item in items:
        print(
            f"Name: {item['name']}, "
            f"Price: Rs. {item['price']:.2f}"
        )

    print("Total products:", len(items))
