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

#ex 4
numbers = [5, 12, 7, 20, 33, 8]
num = list(map(lambda i : i**2 if i % 2 == 0 else i * 3, numbers))
print(num)

#ex 5
compare = lambda a, b: "a >" if a > b else ("b>" if b > a else "==")
print(compare(4, 5))

#ex 6
numbers = [0, -3, 5, -7, 8]
result = [(lambda x: "on san" if x > 0 else ("teris san" if x < 0 else "zero"))(n) for n in numbers]
print(result)
#ex 7

def even_numbers(n):
    for i in range(1, n +1):
        if i % 2 == 0:
            if i % 4 == 0:
                yield "4 кратно"
            else:
                yield i
for x in even_numbers(15):
    print(x)

#ex 8
def filter_words(word):
    for w in  words:
        if len(w) > 4 :
            if "a" in w:
                yield "c a"
            else:
                yield w
words = ["кот", "машина", "арбуз", "дом"]
for w in filter_words(word):
    print(w)
#ex 8
def infinite_numbers():
    n = 1
    while True:
        if n % 3 == 0 and n % 5 == 0 :
            yield "FizzBuzz"
        elif n % 3 == 0 :
            yield "Fizz"
        elif n % 5 == 0 :
            yield "Buzz"
        else:
            yield n
        n += 1
gen = infinite_numbers()
for _ in range(15):
    print(next(gen))

#ex 9
def squares(n):
    for i in range(1, n + 1):
        sq = i ** 2
        if sq % 2 == 0:
            yield "чётный квадрат""
        else:
            yield sq
for x in squares(5):
    print(x)

#ex 10

squares = [i*i for i in range(1, 21) if i % 2 == 0]
print(squares)

#ex 11
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
products = [(lambda row: row[0]*row[1]*row[2])(row) for row in matrix]
print(products)