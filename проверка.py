words = ["кот", "машина", "арбуз", "дом", "ананас"]

result = [
    (word.upper() if len(word) > 4 else "short") + ("*" if "а" in word else "")
    for word in words
]

print(result)