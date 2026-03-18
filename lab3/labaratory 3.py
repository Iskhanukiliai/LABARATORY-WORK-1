# ex 1
check = lambda x: "положительное" if x > 0 else ("отрицательное" if x < 0 else "ноль")
print(check(5))
print(check(-3))
print(check(0))
print("==========================")


# ex 2
words = ["арбуз", "кот", "машина", "дом", "ананас"]
word = sorted(words,  key =lambda w: (len(w), w[0]))
print(word)
print("==========================")


# ex 3
numbers = [5, 12, 7, 20, 33, 8]
new_numbers = list(filter(lambda n: n % 2 == 0 and n > 10, numbers))
print(new_numbers)
print("==========================")


# ex 4
numbers = [1, 2, 3, 4, 5, 6]
new_numbers = list(map(lambda n: n ** 2 if n % 2 == 0 else n * 3, numbers))
print(new_numbers)
print("==========================")


# ex 5
compare = lambda a, b: "a больше" if a > b else("b больше" if b > a else "равны")
print(compare(2, 3))
print(compare(10, 7))
print(compare(3, 5))
print(compare(4, 4))
print("==========================")


# ex 6
numbers = [0, -3, 5, -7, 8]
result =  [(lambda n:"положительное" if n > 0 else ("отрицательное" if n < 0 else "ноль"))(n) for n in numbers]
print(result)
print("==========================")


# ex 7
def even_numbers(n):
    for i in range(1, n +1):
        if i % 2 == 0:
            if i % 4 == 0:
                yield "кратно 4"
            else:
                yield i
for a in even_numbers(10):
    print(a)
print("==========================")


# ex 8
words = ["кот", "машина", "арбуз", "дом"]
def filter_words(words):
    for i in words:
        if len(i) > 4:
            if "а" in i:
                yield "с а"
            else:
                yield i
for w in filter_words(words):
    print(w)
print("==========================")


# ex 9
def infinite_numbers():
    n = 1
    while True:
        if n % 3 == 0 and n % 5 == 0:
            yield "FizzBuzz"
        elif n % 3 == 0:
            yield "Fizz"
        elif n % 5 == 0:
            yield "Buzz"
        else:
            yield n
        n += 1
gen = infinite_numbers()
for n in  range(15):
    print(next(gen))
print("==========================")

# ex 10
def suares(n):
    for  i in  range(1, n+1):
        sq = i ** 2
        if i % 2 == 0:
            yield "чётный квадрат"
        elif i % 3 == 0:
            yield sq
for x in suares(5):
    print(x)
print("==========================")


# ex 11
result = [x**2 for x in range(1, 21) if x % 2 == 0]
print(result)
print("==========================")

# ex 12
from functools import reduce
matrix = [[1,2,3], [4,5,6], [7,8,9]]
result = [reduce(lambda a, b: a * b, row) for row in matrix]
print(result)
print("==========================")

# ex 13
matrix = [[1,2,3], [4,5,6], [7,8,9]]

result = [row[0] * row[1] * row[2] for row in matrix]

print(result)
print("==========================")



