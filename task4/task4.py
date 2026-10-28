""" Task: 
● E-Commerce Inventory Analyzer: A shop owner has a messy product list with 
duplicates, missing prices, and mixed categories. Clean the data, group by category, find 2the top 5 most expensive items per category, and produce a summary dictionary — written in a Pythonic style using comprehensions throughout. """

products = [
    {"name": "Laptop", "price": 150000, "category": "Electronics"},
    {"name": "Phone", "price": 80000, "category": "Electronics"},
    {"name": "Laptop", "price": 150000, "category": "Electronics"},     {"name": "Headphones", "price": 5000, "category": "Electronics"},
    {"name": "Keyboard", "price": None, "category": "Electronics"},  
    {"name": "Shirt", "price": 2500, "category": "Clothing"},
    {"name": "Shoes", "price": 7000, "category": "Clothing"},
    {"name": "Jacket", "price": 9000, "category": "Clothing"},
    {"name": "Watch", "price": 12000, "category": "Accessories"},
    {"name": "Bag", "price": 6000, "category": "Accessories"},
]

cleaned_products = []
seen = set()

for product in products:
    name = product.get("name")
    price = product.get("price")
    category = product.get("category")

    if not name or not category or price is None:
        continue

    try:
        price = float(price)
    except (ValueError, TypeError):
        continue

    if price < 0:
        continue

    key = (name.strip().lower(), price, category.strip().lower())

    if key not in seen:
        seen.add(key)
        cleaned_products.append({
            "name": name.strip(),
            "price": price,
            "category": category.strip().title()
        })

categories = {p["category"] for p in cleaned_products}

grouped_products = {
    category: [p for p in cleaned_products if p["category"] == category]
    for category in categories
}


top_5 = {
    category: sorted(items, key=lambda p: p["price"], reverse=True)[:5]
    for category, items in grouped_products.items()
}

summary = {
    category: {
        "total_products": len(items),
        "average_price": round(
            sum(p["price"] for p in items) / len(items), 2
        ),
        "most_expensive": max(items, key=lambda p: p["price"])["name"],
        "top_5": [p["name"] for p in items]
    }
    for category, items in top_5.items()
}

print("Cleaned Products:")
print(cleaned_products)

print("\nTop 5 Products Per Category:")
for category, items in top_5.items():
    print(category, ":", items)

print("\nSummary Dictionary:")
print(summary)
