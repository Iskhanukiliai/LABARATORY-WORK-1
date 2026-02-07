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

