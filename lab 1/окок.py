# 1
def analyze_text(text):
    vowels = "aeiouyауоыиэяюёе"
    unique_vowels = []
    words = []
    current = ""
    for ch in text.lower():
        if ch.isalpha():
            if ch in vowels and ch not in unique_vowels:
                unique_vowels.append(ch)
            current += ch
        else:
            if current != "":
                words.append(current)
                current = ""
    if current != "":
        words.append(current)
    result_words = []
    for word in words:
        if len(word) >= 5 and word[0] == word[-1] and word not in result_words:
            result_words.append(word)
    return (len(unique_vowels), " ".join(result_words))








# 2
task2 = lambda s: " ".join(
    list(
        filter(
            lambda w: len(w) % 2 == 0,
            map(
                lambda w: w[::-1],
                filter(lambda w: not any(ch.isdigit() for ch in w), s.split())
            )
        )
    )
)






# 3
def top_k_words(text, k):
    cleaned = ""
    for ch in text.lower():
        if ch.isalpha() or ch.isdigit() or ch == " ":
            cleaned += ch
        else:
            cleaned += " "
    words = cleaned.split()
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    items = []
    for word in counts:
        items.append([word, counts[word]])
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[j][1] > items[i][1] or (items[j][1] == items[i][1] and items[j][0] < items[i][0]):
                items[i], items[j] = items[j], items[i]
    result = []
    for i in range(min(k, len(items))):
        result.append(items[i][0])
    return result







# 4
task4 = lambda s: " ".join(
    map(
        lambda w: w.lower(),
        filter(
            lambda w: sum(1 for ch in w if ch.isupper()) == 1 and not w[0].isupper() and not w[-1].isupper(),
            s.split()
        )
    )
)





# 5
def compress_text(text):
    if text == "":
        return ""
    result = ""
    current = text[0]
    count = 1
    for i in range(1, len(text)):
        if text[i].lower() == current.lower():
            count += 1
        else:
            if count == 1:
                result += current
            else:
                result += current + str(count)
            current = text[i]
            count = 1
    if count == 1:
        result += current
    else:
        result += current + str(count)
    return result




# 6
task6 = lambda s: list(
    filter(
        lambda w: len(w) >= 4 and not any(ch.isdigit() for ch in w) and len(set(w)) == len(w),
        s.split()
    )
)




# 7
def palindrome_words(text):
    cleaned = ""
    for ch in text.lower():
        if ch.isalpha() or ch.isdigit() or ch == " ":
            cleaned += ch
        else:
            cleaned += " "
    words = cleaned.split()
    unique = []
    for word in words:
        if len(word) >= 3 and word == word[::-1] and word not in unique:
            unique.append(word)
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if len(unique[j]) > len(unique[i]) or (len(unique[j]) == len(unique[i]) and unique[j] < unique[i]):
                unique[i], unique[j] = unique[j], unique[i]
    return unique

# 8
task8 = lambda s: " ".join(
    map(
        lambda w: w if any(ch.isdigit() for ch in w) else ("VOWEL" if w[0].lower() in "aeiouyауоыиэяюёе" else "CONSONANT"),
        s.split()
    )
)



# 9
def alternate_case_blocks(text, n):
    result = ""
    block_index = 0

    for i in range(0, len(text), n):
        block = text[i:i + n]
        if block_index % 2 == 0:
            result += block.upper()
        else:
            result += block.lower()
        block_index += 1

    return result.replace(" ", "")




# 10
task10 = lambda s: sum(
    1 for w in s.split()
    if len(w) >= 5 and any(ch.isdigit() for ch in w) and not w[0].isdigit()
)
# Task 11
def common_unique_chars(s1, s2):
    result = ""

    for ch in s1:
        if ch != " " and not ch.isdigit() and ch in s2 and ch not in result:
            result += ch

    return result


# Task 12
task12 = lambda s: list(
    filter(
        lambda w: len(w) > 3 and w[0] == w[-1] and w != w[::-1],
        s.split()
    )
)


# Task 13
def replace_every_nth(text, n, char):
    words = text.split()
    short_positions = set()
    pos = 0
    for word in words:
        if len(word) < 3:
            for i in range(pos, pos + len(word)):
                short_positions.add(i)
        pos += len(word)
        while pos < len(text) and text[pos] == " ":
            pos += 1
    result = ""
    for i in range(len(text)):
        if (i + 1) % n == 0 and text[i] != " " and not text[i].isdigit() and i not in short_positions:
            result += char
        else:
            result += text[i]
    return result






# Task 14
task14 = lambda s: ",".join(
    filter(
        lambda w: len(set(w.lower())) > 3 and all(w.lower().count(v) <= 1 for v in "aeiouyауоыиэяюёе"),
        s.split()
    )
)






# Task 15
def word_pattern_sort(text):
    words = text.split()
    groups = {}
    for word in words:
        length = len(word)
        if length not in groups:
            groups[length] = []
        groups[length].append(word)

    lengths = list(groups.keys())
    for i in range(len(lengths)):
        for j in range(i + 1, len(lengths)):
            if lengths[j] < lengths[i]:
                lengths[i], lengths[j] = lengths[j], lengths[i]
    vowels = "aeiouyауоыиэяюёе"
    for length in lengths:
        group = groups[length]
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                count_i = 0
                count_j = 0
                for ch in group[i].lower():
                    if ch in vowels:
                        count_i += 1
                for ch in group[j].lower():
                    if ch in vowels:
                        count_j += 1
                if count_j > count_i or (count_j == count_i and group[j].lower() < group[i].lower()):
                    group[i], group[j] = group[j], group[i]
    result = []
    for length in lengths:
        for word in groups[length]:
            result.append(word)
    return result





# Task 16
def transform_list(nums):
    result = []
    for num in nums:
        if num < 0:
            continue
        elif num % 2 == 0:
            result.append(num * num)
        elif num > 10:
            s = 0
            for ch in str(num):
                s += int(ch)
            result.append(s)
        else:
            result.append(num)
    return result







# Task 17
task17 = lambda nums: list(
    map(
        lambda x: x * x,
        filter(
            lambda x: (x % 3 == 0 or x % 5 == 0) and x % 15 != 0 and len(str(abs(x))) % 2 == 1,
            nums
        )
    )
)


# Task 18
def flatten_and_filter(lst):
    numbers = []
    def extract(items):
        for item in items:
            if type(item) == list:
                extract(item)
            elif type(item) in (int, float):
                numbers.append(item)
    extract(lst)
    result = []
    for num in numbers:
        if num > 0 and num % 4 != 0 and len(str(int(num))) > 1:
            result.append(num)
    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if result[j] < result[i]:
                result[i], result[j] = result[j], result[i]
    return result




# Task 19
task19 = lambda a, b: [x for x, y in zip(a, b) if x == y and x % 2 == 0]





# Task 20
def max_subarray_sum(nums, k):
    max_sum = None
    for i in range(len(nums) - k + 1):
        current_sum = 0
        valid = True
        for j in range(i, i + k):
            if nums[j] <= 0:
                valid = False
                break
            current_sum += nums[j]
        if valid:
            if max_sum is None or current_sum > max_sum:
                max_sum = current_sum
    return max_sum

# Task 21
def count_leaf_values(d):
    count = 0
    for v in d.values():
        if type(v) == dict:
            count += count_leaf_values(v)
        elif type(v) == list:
            for item in v:
                if type(item) == dict:
                    count += count_leaf_values(item)
                else:
                    count += 1
        else:
            count += 1
    return count


# Task 22
task22 = lambda a, b: {x for x in a if x > (sum(b)/len(b) if b else 0) and x not in b}


# Task 23
def group_by_last_letter(words):
    result = {}
    for word in words:
        if word == "":
            continue
        key = word[-1]
        if key not in result:
            result[key] = []
        if word not in result[key]:
            result[key].append(word)
    return result


# Task 24
def union_of_filtered_sets(sets_list):
    result = set()
    for s in sets_list:
        for x in s:
            if x > 10 and x % 2 == 1:
                result.add(x)
    return result


# Task 25
task25 = lambda d: {
    k: (lambda lst: (lambda p: p if p != 1 or len(lst) > 0 else None)(
        (lambda res: res)(
            (lambda nums: (lambda r: r)(
                (lambda r=1: [r := r * x for x in nums][-1] if nums else 1)()
            ))([x for x in lst if x > 0])
        )
    ))(d[k])
    for k in d if [x for x in d[k] if x > 0]
}


# Task 26
def remove_elements_with_common_digits(s):
    digit_count = {}
    for num in s:
        for d in str(abs(num)):
            digit_count[d] = digit_count.get(d, 0) + 1

    result = set()
    for num in s:
        ok = True
        for d in str(abs(num)):
            if digit_count[d] > 1:
                ok = False
                break
        if ok:
            result.add(num)
    return result


# Task 27
task27 = lambda d: {
    k: v for k, v in d.items()
    if len(k) % 2 == 1 and v > 1 and all(v % i != 0 for i in range(2, int(v**0.5)+1))
}


# Task 28
def sorted_unique_chars(strings):
    chars = set()
    for s in strings:
        for ch in s:
            if ch != " " and not ch.isdigit():
                chars.add(ch)
    result = list(chars)
    for i in range(len(result)):
        for j in range(i+1, len(result)):
            if result[j] < result[i]:
                result[i], result[j] = result[j], result[i]
    return result


# Task 29
task29 = lambda d: sorted(
    d.keys(),
    key=lambda k: (d[k] % 10, k)
)


# Task 30
def partition_by_sum_parity(s):
    even_set = set()
    odd_set = set()

    for num in s:
        s_digits = sum(int(ch) for ch in str(abs(num)))
        if s_digits % 2 == 0:
            even_set.add(num)
        else:
            odd_set.add(num)

    return (even_set, odd_set)


# Task 31
task31 = lambda d: {
    k: v for k, v in d.items()
    if len(v) == len(set(v)) and all(len(x) > 3 for x in v)
}


# Task 32
def pairwise_intersections(sets_list):
    if len(sets_list) < 2:
        return []
    result = []
    for i in range(len(sets_list)-1):
        result.append(sets_list[i] & sets_list[i+1])
    return result


# Task 33
task33 = lambda d: (
    lambda avg: {
        k: v for k, v in d.items()
        if sum(v)/len(v) > avg
    }
)(sum(x for lst in d.values() for x in lst) / sum(len(lst) for lst in d.values()))




# Task 34
def top_k_smallest_unique(nums, k):
    unique = list(set(nums))
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if unique[j] < unique[i]:
                unique[i], unique[j] = unique[j], unique[i]
    return set(unique[:k])




# Task 35
task35 = lambda d: {
    k: v for k, v in d.items()
    if v % 3 != 0 and len(k) % 2 == 1
}




# Task 36
def all_subsets_of_size_k(s, k):
    s = list(s)
    result = []
    def backtrack(start, current):
        if len(current) == k:
            result.append(set(current))
            return
        for i in range(start, len(s)):
            current.append(s[i])
            backtrack(i+1, current)
            current.pop()

    backtrack(0, [])
    return result




# Task 37
task37 = lambda d: {
    k: (lambda x: (lambda f=1: [f := f*i for i in range(1, x+1)][-1])(x) if x < 6 else x)
    for k, x in d.items()
}




# Task 38
def multi_symmetric_difference(sets_list):
    if not sets_list:
        return set()
    result = sets_list[0].copy()
    for s in sets_list[1:]:
        result = result ^ s
    return result




# Task 39
task39 = lambda d: sorted(
    d.keys(),
    key=lambda k: (sum(1 for ch in k.lower() if ch in "aeiouyауоыиэяюёе"), -d[k])
)




# Task 40
def analyze_dict_keys(d):
    import string
    result = set()

    for k in d:
        if type(k) == str and not any(ch.isdigit() for ch in k):
            for ch in k:
                if ch not in string.punctuation and ch != " ":
                    result.add(ch)

def analyze_students(data):
    import string

    vowels = "aeiouyауоыиэяюёе"
    students = []
    all_vowels = set()
    word_students = {}

    for student in data:
        name = student["name"]

        if any(ch.isdigit() for ch in name):
            continue

        name = name.title()

        processed = []
        for g in student["grades"]:
            if g <= 0:
                continue
            elif g % 2 == 1 and g < 10:
                s = 0
                for ch in str(g):
                    s += int(ch)
                processed.append(s)
            elif g % 2 == 0 and g >= 10:
                processed.append(g * g)
            else:
                processed.append(g)

        text = " ".join(student["comments"])
        cleaned = ""
        for ch in text:
            if ch not in string.punctuation:
                cleaned += ch.lower()
            else:
                cleaned += " "

        words = cleaned.split()

        unique_words = []
        for w in words:
            if len(w) >= 4 and w != w[::-1] and w not in unique_words:
                unique_words.append(w)

        student_vowels = set()
        for w in unique_words:
            for ch in w:
                if ch in vowels:
                    student_vowels.add(ch)
                    all_vowels.add(ch)

        for w in unique_words:
            if w not in word_students:
                word_students[w] = set()
            word_students[w].add(name)

        students.append({
            "name": name,
            "processed_grades": processed,
            "words": unique_words
        })

    word_counts = {}
    for w in word_students:
        if len(word_students[w]) >= 2:
            word_counts[w] = len(word_students[w])

    items = list(word_counts.items())
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if items[j][1] > items[i][1] or (items[j][1] == items[i][1] and items[j][0] < items[i][0]):
                items[i], items[j] = items[j], items[i]

    word_counts = dict(items)

    avg_list = []
    for st in students:
        if len(st["processed_grades"]) > 0:
            avg = sum(st["processed_grades"]) / len(st["processed_grades"])
        else:
            avg = 0
        avg_list.append((st["name"], avg))

    for i in range(len(avg_list)):
        for j in range(i+1, len(avg_list)):
            if avg_list[j][1] > avg_list[i][1] or (avg_list[j][1] == avg_list[i][1] and avg_list[j][0] < avg_list[i][0]):
                avg_list[i], avg_list[j] = avg_list[j], avg_list[i]

    students_by_avg = [x[0] for x in avg_list]

    by_len = {}
    for st in students:
        l = len(st["name"])
        if l not in by_len:
            by_len[l] = []
        if st["name"] not in by_len[l]:
            by_len[l].append(st["name"])

    return {
        "students": [{"name": s["name"], "processed_grades": s["processed_grades"]} for s in students],
        "word_counts": word_counts,
        "all_vowels": all_vowels,
        "students_by_avg": students_by_avg,
        "students_by_name_length": by_len
    }


def analyze_orders(orders):
    import string

    vowels = "aeiouyауоыиэяюёе"
    result_orders = []
    all_vowels = set()
    word_orders = {}
    unique_products = set()

    for order in orders:
        customer = order["customer"]

        if any(ch.isdigit() for ch in customer):
            continue

        customer = customer.title()

        processed_items = []

        for item in order["items"]:
            name = item["name"]
            price = item["price"]
            qty = item["quantity"]

            if price <= 0:
                continue

            if price > 100 and qty > 1:
                price = price * qty

            if qty % 2 == 1:
                s = sum(int(ch) for ch in str(int(price)))
                price += s

            processed_items.append({
                "name": name,
                "price": price,
                "quantity": qty
            })

            unique_products.add(name)

        text = " ".join(order["notes"])
        cleaned = ""
        for ch in text:
            if ch not in string.punctuation:
                cleaned += ch.lower()
            else:
                cleaned += " "

        words = cleaned.split()

        unique_words = []
        for w in words:
            if len(w) >= 4 and w != w[::-1] and w not in unique_words:
                unique_words.append(w)

        for w in unique_words:
            if w not in word_orders:
                word_orders[w] = set()
            word_orders[w].add(order["order_id"])

        for w in unique_words:
            for ch in w:
                if ch in vowels:
                    all_vowels.add(ch)

        result_orders.append({
            "order_id": order["order_id"],
            "customer": customer,
            "processed_items": processed_items
        })

    word_counts = {}
    for w in word_orders:
        if len(word_orders[w]) >= 2:
            word_counts[w] = len(word_orders[w])

    items = list(word_counts.items())
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if items[j][1] > items[i][1] or (items[j][1] == items[i][1] and items[j][0] < items[i][0]):
                items[i], items[j] = items[j], items[i]

    word_counts = dict(items)

    totals = []
    for o in result_orders:
        total = 0
        for it in o["processed_items"]:
            total += it["price"]
        totals.append((o["order_id"], total))

    for i in range(len(totals)):
        for j in range(i+1, len(totals)):
            if totals[j][1] > totals[i][1] or (totals[j][1] == totals[i][1] and totals[j][0] < totals[i][0]):
                totals[i], totals[j] = totals[j], totals[i]

    orders_by_total = [x[0] for x in totals]
    by_count = {}
    for o in result_orders:
        c = len(o["processed_items"])
        if c not in by_count:
            by_count[c] = []
        if o["order_id"] not in by_count[c]:
            by_count[c].append(o["order_id"])
    return {
        "orders": result_orders,
        "word_counts": word_counts,
        "all_vowels": all_vowels,
        "unique_products": unique_products,
        "orders_by_total": orders_by_total,
        "orders_by_item_count": by_count
