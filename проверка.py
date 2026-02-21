users = set()
buy_count = 0
total_sum = 0
user_name = {}
logs = """2026-02-01;user_1;LOGIN
2026-02-01;user_2;LOGIN
2026-02-01;user_1;BUY;120
2026-02-01;user_3;LOGIN
2026-02-01;user_2;BUY;300
2026-02-01;user_1;BUY;50
2026-02-01;user_2;LOGOUT"""

with open("shop_logs.txt", "w", encoding="utf-8") as f:
    f.write(logs)

with open("shop_logs.txt", "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(";")
        name = parts[1]
        data = parts[0]
        actions = parts[2]
        users.add(name)

        if actions == "BUY":
            baga = int(parts[3])
            buy_count += 1
            total_sum += baga

            if name not in user_name:
                user_name[name] = baga
            else:
                user_name[name] += baga
max_user = None
max_pokupka = 0
for name in user_name:
    if user_name[name] > max_pokupka:
        max_pokupka = user_name[name]
        max_user = name
if buy_count != 0:
    mid_pokupka = total_sum / buy_count
else:
    mid_pokupka = 0

with open("result.txt", "w", encoding="utf-8") as f:
    f.write(f"Qoldanushylar sany: {len(users)}")
with open("result.txt", "r", encoding="utf-8") as f1:
    print(f1.read())




