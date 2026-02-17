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
f = lambda s: ' '.join(w.lower() for w in s.split() if sum(c.isupper() for c in w[1:-1]) == 1)

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