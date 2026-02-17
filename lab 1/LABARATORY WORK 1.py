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