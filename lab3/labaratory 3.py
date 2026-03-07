#ex 1
check = lambda x: "polozhitelno" if x > 0 else ("otrisatelno" if x <  0 else "zero")
print(check(5))
print(check(-5))

#ex 2
words = ["арбуз", "кот", "машина", "дом", "ананас"]
word = sorted(words, key = lambda x: (len(x) , words[0]))
print(word)

#ex 3
numbers = [5, 12, 7, 20, 33, 8]
num = list(filter(lambda i : i % 2 == 0 and i > 10, numbers))
print(num)


