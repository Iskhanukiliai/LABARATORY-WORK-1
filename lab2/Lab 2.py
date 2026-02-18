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
            amount = int(parts[3])
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
    r.write(f"Уникальных пользователей: {len(users)}\n")
    r.write(f"Всего покупок: {buy_count}\n")
    r.write(f"Общая сумма: {total_sum}\n")
    r.write(f"Самый активный покупатель: {max_user}\n")
    r.write(f"Средний чек: {avg_check}\n")
print("Отчёт создан: report.txt")