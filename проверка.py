words = ["арбуз", "кот", "машина", "дом", "ананас"]
word = sorted(words,  key =lambda w: (len(w), w[0]))
print(word)