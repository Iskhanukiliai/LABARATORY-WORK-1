import json
orders_data = [
    {
        "order_id": 1,
        "user": "Ali",
        "items": ["phone", "case"],
        "total": 300000
    },
    {
        "order_id": 2,
        "user": "Dana",
        "items": ["laptop"],
        "total": 800000
    },
    {
        "order_id": 3,
        "user": "Ali",
        "items": ["mouse", "keyboard"],
        "total": 70000
    }
]
with open("orders.json", "w", encoding="utf-8") as f:
    json.dump(orders_data, f, ensure_ascii=False, indent=2)

with open("orders.json", "r", encoding="utf-8") as f:
    orders = json.load(f)

total_revenue = 0
user_orders = {}
item_count = {}
top_user = ""
max_order_price = 0
most_popular_item = ""
max_item_count = 0
total_items_sold = 0

for order in orders:
    total_revenue += order["total"]

    user = order["user"]
    if user not in user_orders:
        user_orders[user] = 0
    user_orders[user] += 1

    if order["total"] > max_order_price:
        max_order_price = order["total"]
        top_user = user

    for item in order["items"]:
        total_items_sold += 1
        if item not in item_count:
            item_count[item] = 0
        item_count[item] += 1


for item in item_count:
    if item_count[item] > max_item_count:
        max_item_count = item_count[item]
        most_popular_item = item




with open("summary.json", "w", encoding="utf-8") as f:
    json.dump(orders.json", f, ensure_ascii=False, indent=2)

print("Толық сумма:", total_revenue)
print("Қолданушы бойынша заказ", user_orders)
print("Барлығы сатылған товар:", total_items_sold)
print("Топ-қодануша:", top_user)
print("Ең көп сатлылған товар:", most_popular_item)

