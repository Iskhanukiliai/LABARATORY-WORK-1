def analyze_text(text):
    text1 = text.lower()
    text2 = ""
    for word in text1:
        if word.isalpha() or word == " ":
            text2 += word
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










