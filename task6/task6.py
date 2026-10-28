""" Task: 
● Order Discount Pipeline: An online store needs a data pipeline that takes a raw list of customer orders, applies category-based discount rules, filters out orders below a 
minimum threshold, and returns a processed summary with total revenue — using no 
traditional `for` loops anywhere."""
from functools import reduce

orders = [
    {"customer": "Ali", "category": "Electronics", "price": 5000},
    {"customer": "Sara", "category": "Clothing", "price": 2000},
    {"customer": "Ahmed", "category": "Books", "price": 800},
    {"customer": "Ayesha", "category": "Electronics", "price": 1500},
    {"customer": "Bilal", "category": "Clothing", "price": 6000},
]

discounts = {
    "Electronics": 0.10,
    "Clothing": 0.20,
    "Books": 0.05
}

minimum_price = 1000

discounted_orders = list(map(
    lambda order: {
        **order,
        "discount": discounts.get(order["category"], 0),
        "final_price": order["price"] * (
            1 - discounts.get(order["category"], 0)
        )
    },
    orders
))

processed_orders = list(filter(
    lambda order: order["final_price"] >= minimum_price,
    discounted_orders
))

total_revenue = reduce(
    lambda total, order: total + order["final_price"],
    processed_orders,
    0
)

summary = {
    "total_orders_received": len(orders),
    "orders_accepted": len(processed_orders),
    "orders_rejected": len(orders) - len(processed_orders),
    "total_revenue": round(total_revenue, 2),
    "processed_orders": processed_orders
}

print("Processed Orders:")
print(processed_orders)

print("\nFinal Summary:")
print(summary)
