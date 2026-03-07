#ex 1
users = set()
buy_count = 0
total_sum = 0
user_spend = {}

with open("shop_logs.txt", "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(";")
        date = parts[0]
        user = parts[1]
        action = parts[2]

        users.add(user)

        if action == "BUY":
            amount = int(parts[3]) #amount- сумма, parts[3] сумма покупок, строка --> число
            buy_count += 1
            total_sum += amount

            if user not in user_spend:
                user_spend[user] = amount
            else:
                user_spend[user] += amount
max_user = None
max_sum = 0

for user in user_spend:
    if user_spend[user] > max_sum:
        max_sum = user_spend[user]
        max_user = user
if buy_count != 0:
    avg_check = total_sum / buy_count
else:
    avg_check = 0
with open("report.txt", "w", encoding="utf-8") as r:
    r.write(f"Қолданушылар саны: {len(users)}\n")
    r.write(f"Барлық сатылымдар саны: {buy_count}\n")
    r.write(f"Жалпы сумма: {total_sum}\n")
    r.write(f"Ең активный пайдаланушы: {max_user}\n")
    r.write(f"Средний чек: {avg_check}\n")
with open("report.txt", "r", encoding="utf-8") as f:
     print(f.read())


#ex2

import csv
zhumysshylar = """name,department,salary
Ali,IT,500000
Dana,HR,300000
Arman,IT,600000
Aruzhan,Marketing,400000
Dias,IT,450000"""
employees = []
with open("employees.csv", "w", encoding='utf-8') as f:
    f.write(zhumysshylar)
with open("employees.csv", 'r', encoding='utf-8') as f1:
    reader = csv.DictReader(f1)
    for row in reader:
        row['salary'] = int(row['salary'])
        employees.append(row)

total_salary = sum(emp['salary'] for emp in employees)
avg_salary = total_salary / len(employees)

dept_salary = {}
dept_count = {}

for emp in employees:
    dept = emp['department']
    if dept not in dept_salary:
        dept_salary[dept] = emp['salary']
        dept_count[dept] = 1
    else:
        dept_salary[dept] += emp['salary']
        dept_count[dept] += 1
avg_dept_salary = {dept: dept_salary[dept] / dept_count[dept] for dept in dept_salary}
max_avg_dept = max(dept_salary, key=avg_dept_salary.get)
highest_paid = max(employees, key=lambda employees: employees['salary'])
above_avg = [emp for emp in employees if emp['salary'] > avg_salary]
with open('high_salary.csv', 'w', newline='', encoding='utf-8') as f2:
    writer = csv.DictWriter(f2, fieldnames=['name', 'department', 'salary'])
    writer.writeheader()
    writer.writerows(above_avg)
print("Ortasha zarplata:", avg_salary)
print("max_avg_dept:", max_avg_dept)
print("highest_paid:", highest_paid)

#ex 3

import json

orders_data = [
    {"order_id": 1, "user": "Ali", "items": ["phone", "case"], "total": 300000},
    {"order_id": 2, "user": "Dana", "items": ["laptop"], "total": 800000},
    {"order_id": 3, "user": "Ali", "items": ["mouse", "keyboard"], "total": 70000}
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
    total_revenue += order['total']
    user = order['user']


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


print("Қолданушы бойынша заказ:", user_orders)
print("Барлығы сатылған товар:", total_items_sold)
print("Топ-қодануша:", top_user)
print("Ең көп сатлылған товар:", most_popular_item)