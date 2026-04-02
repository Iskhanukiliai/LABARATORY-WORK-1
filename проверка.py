shop =  """2026-02-01;user_1;LOGIN
2026-02-01;user_2;LOGIN
2026-02-01;user_1;BUY;120
2026-02-01;user_3;LOGIN
2026-02-01;user_2;BUY;300
2026-02-01;user_1;BUY;50
2026-02-01;user_2;LOGOUT"""

users = set()
total_sum = 0
buy_count = 0
users_spend ={}

with open("shop_logs.txt", "w", encoding = "utf-8") as f:
    f.write(shop)
with open("shop_logs.txt", "r", encoding = "utf-8") as f:
    for line in f:
        part = line.strip().split(";")
        data = part[0]
        user = part[1]
        actions = part[2]

        users.add(user)

        for actions in part:
            if actions == "BUY":
                price = int(part[3])
                buy_count += 1
                total_sum += price

                if user not in users_spend:
                    users_spend[user] = price
                else:
                    users_spend[user] += price

max_name = None
max_sum = 0
for user in users_spend:
    if users_spend[user] > max_sum:
        max_name = user
        max_sum = users_spend[user]
if buy_count != 0:
    avg_price = total_sum / buy_count
else:
    avg_price = 0

with open("report.txt", "w", encoding = "utf -8") as t:
    t.write(f"satyp alushy: {buy_count}\n")
    t.write(f"ortasha: {avg_price}")

with open("report.txt", "r", encoding = "utf-8") as a:
    print(a.read())

