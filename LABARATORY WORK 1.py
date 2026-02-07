# задача 1
def analyze_text(text):
    text1 = text.lower()
    text2 = ""
    for alpha in text1:
        if alpha.isalpha() or alpha == " ":
            text2 += alpha
    dauysty = "aeiouy"
    zhana_text = ""
    for alpha in text2:
        if alpha in dauysty:
            zhana_text += alpha
    text3 = text2.split()
    result = ""
    text4 = ''
    for word in text3:
        if len(word) >= 5:
            if word[0] == word[-1]:
                if word not in result:
                    result += word + " "
                    text4 += word + "," + " "

    return {
        "дауысты әріптер:" : set(zhana_text),
    "дауысты әріптер саны:": len(set(zhana_text)),
        "слова длиной ≥ 5:": text4,
        "жауабы:": result
    }
kerek_matyn = input("керек мәтінді жазыңыз:")
print(analyze_text(kerek_matyn))

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
main = lambda text:" ".join(
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


# 4 задча
def main(text):
    result = []
    for word in text.split():
        for ch in word[1:-1]:

























































































































            
            if ch.isupper():
                result.append(word.lower())


    return " ".join(result)
text = input("soz engiz:")
print(main(text))
















