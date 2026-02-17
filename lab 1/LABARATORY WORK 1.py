# задача 1

def analyze_text(text):
    text_lower = text.lower()
    clean_text = ""
    for ch in text_lower:
        if ch.isalpha() or ch == " ":
            clean_text += ch

    vowels = "aeiouy"
    unique_vowels = []
    for ch in clean_text:
        if ch in vowels and ch not in unique_vowels:
            unique_vowels.append(ch)
    num_unique_vowels = len(unique_vowels)

    words = clean_text.split()
    selected = []
    for w in words:
        if len(w) >= 5 and w[0] == w[-1] and w not in selected:
            selected.append(w)

    return (num_unique_vowels, ' '.join(selected))

# задача 2
matyn = input("мәтін енгіз:")
def main(text):
    result =[]
    for word in text.split():
        digit = False
        for ch in word:
            if ch.isdigit():
                digit = True
                break
        if not digit:
            word2 = word[::-1]
            if len(word2) % 2 == 0:
                result.append(word2)
    return " ".join(result)


print(main(matyn))
# lambda
main = lambda text: " ".join(
    map(
        lambda word: word[::-1],
        filter(
            lambda word: not any(ch.isdigit() for ch in word) and len(word) % 2 == 0,
            text.split()
        )
    )
)
matyn = input("matyn engiz:")
print(main(matyn))

# 3 задача
def top_k_words(text, k):
    text = text.lower()
    clean = ""
    for c in text:
        if c.isalnum() or c == " ":
            clean += c
    words = clean.split()
    uniq = []
    cnt = []
    for w in words:
        if w in uniq:
            i = uniq.index(w)
            cnt[i] += 1
        else:
            uniq.append(w)
            cnt.append(1)
    for i in range(len(uniq)):
        for j in range(len(uniq)-1):
            if cnt[j] < cnt[j+1] or (cnt[j]==cnt[j+1] and uniq[j] > uniq[j+1]):
                cnt[j], cnt[j+1] = cnt[j+1], cnt[j]
                uniq[j], uniq[j+1] = uniq[j+1], uniq[j]
    res = []
    for i in range(min(k, len(uniq))):
        res.append(uniq[i])
    return res

# 4 задача
f = lambda s: [w for w in s.split() if sum(c.isupper() for c in w[1:-1]) == 1]
text = "heLlo WorLd PyThon tesTing ABCde"
print(f(text))
# 5 задача
def compress_text(text):
    if not text:
        return ""

    result = ""
    count = 1
    for i in range(1, len(text)):
        if text[i].lower() == text[i - 1].lower():
            count += 1
        else:
            result += text[i - 1] + (str(count) if count > 1 else "")
            count = 1
    result += text[-1] + (str(count) if count > 1 else "")

    return result

# 6 задача
f = lambda s:[w for w in s.split() if len(w) >= 4 and w.isalpha() and len(set(w)) == len(w)]
text = "test code 123 python lambda loop abcde aabb"
print(f(text))

# 7 zadacha
def palindrome_words(text):
    proverka = ""
    for ch in text:
        if ch.isalpha() or ch.isspace():
            proverka += ch.lower()
    words = proverka.split()
    unique_palindromes = []
    for word in words:
        if len(word) >= 3 and word == word[::-1]:
            if word not in unique_palindromes:
                unique_palindromes.append(word)
    unique_palindromes.sort(key=lambda w: (-len(w), w))
    return unique_palindromes
text = "Madam, level, noon, gagag! radar level kayak?"
print("7 zadacha: ", palindrome_words(text))

# 8 zadacha
f = lambda s: ' '.join(
    w if any(c.isdigit() for c in w) else ("VOWEL" if w[0].lower() in "aeiouy" else "CONSONANT")
    for w in s.split()
)
text = "apple banana 123orange cat elephant dog2"
print(f(text))

# 9 zadacha
def alternate_case_blocks(text, n):
    result = ""
    for i in range(0, len(text), n):
        block = text[i:i+n]
        if (i // n) % 2 == 0:
            result += block.upper()
        else:
            result += block.lower()
    return result
text = "abcdefghijklmnopqrstuvwxyz"
print(alternate_case_blocks(text, 5))

# 10 zadacha
f = lambda s: sum(1 for w in s.split() if len(w) >= 5 and not w[0].isdigit() and any(c.isdigit() for c in w))
text = "abc123 1start 12345 a1b2c3 abcde5 9xyz"
print(f(text))

#11 zadacha
def common_unique_chars(s1, s2):
    result = ""
    for ch in s1:
        if ch.isalpha() and ch in s2 and ch not in result:
            result += ch
    return result
s1 = "abracadabra 123"
s2 = "barbecue 456"
print(common_unique_chars(s1, s2))

#12 zadacha
f = lambda s: [w for w in s.split() if len(w) > 3 and w[0].lower() == w[-1].lower() and w.lower() != w[::-1].lower()]
text = "abca abba level radar testt helloH abcdba"
print(f(text))

# 13 zadacha
def replace_every_nth(text, n, char):
    result = ""
    count = 0
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == " " or ch.isdigit():
            result += ch
            i += 1
            continue
        if ch.isalpha():
            start = i
            while i < len(text) and text[i].isalpha():
                i += 1
            word = text[start:i]
            if len(word) < 3:
                result += word
                continue
            for c in word:
                count += 1
                if count % n == 0:
                    result += char
                else:
                    result += c
        else:
            count += 1
            if count % n == 0:
                result += char
            else:
                result += ch
            i += 1
    return result
text = "Hello world 123 ab cd python test"
print(replace_every_nth(text, 3, "*"))

# 14 zadacha
f = lambda s: ','.join(
    w for w in s.split()
    if len(set(w.lower())) > 3
    and all(w.lower().count(v) <= 1 for v in "aeiouy")
)
text = "planet apple stone queue cryptography education sky"
print(f(text))

# 15 zadacha
def word_pattern_sort(text):
    vowels = "aeiouy"
    words = text.split()
    length_groups = {}
    for w in words:
        l = len(w)
        if l not in length_groups:
            length_groups[l] = []
        length_groups[l].append(w)
    result = []
    for l in sorted(length_groups):
        group = length_groups[l]
        vowel_counts = []
        for w in group:
            count = 0
            for c in w.lower():
                if c in vowels:
                    count += 1
            vowel_counts.append(count)
        n = len(group)
        for i in range(n):
            for j in range(n - 1):
                if vowel_counts[j] < vowel_counts[j + 1] or \
                        (vowel_counts[j] == vowel_counts[j + 1] and group[j] > group[j + 1]):
                    group[j], group[j + 1] = group[j + 1], group[j]
                    vowel_counts[j], vowel_counts[j + 1] = vowel_counts[j + 1], vowel_counts[j]
        result.extend(group)
    return result
text = "apple banana kiwi pear orange grape plum"
print(word_pattern_sort(text))

# 16 zadacha
def transform_list(nums):
    result = []
    for n in nums:
        if n < 0:
            continue
        if n % 2 == 0:
            result.append(n ** 2)
        elif n > 10:
            s = 0
            temp = n
            while temp > 0:
                s += temp % 10
                temp //= 10
            result.append(s)
        else:
            result.append(n)
    return result
nums = [4, -3, 15, 8, 7, 22, 11, -5]
print(transform_list(nums))

# 17 zadacha
f = lambda nums: list(
    map(lambda x: x*x,
        filter(lambda x: (x % 3 == 0 or x % 5 == 0) and x % 15 != 0 and len(str(abs(x))) % 2 == 1, nums)
    )
)
nums = [3, 5, 15, 30, 9, 25, 7, 105, 45, 81]
print(f(nums))

# 18 zadacha
def flatten_and_filter(lst):
    result = []
    def walk(sub):
        for x in sub:
            if type(x) == list:
                walk(x)
            elif type(x) == int:
                if x > 0 and x % 4 != 0 and abs(x) >= 10:
                    result.append(x)
    walk(lst)
    for i in range(len(result)):
        for j in range(0, len(result) - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result
lst = [1, [12, -3, [8, 15, [16, 23]], 4], 7, [5, [44, 19]]]

print(flatten_and_filter(lst))