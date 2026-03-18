def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def special_numbers(n):
    for x in range(1, n + 1):
        if x % 3 == 0 and x % 5 == 0:
            yield "FizzBuzz"
        elif x % 3 == 0:
            yield "Fizz"
        elif x % 5 == 0:
            yield "Buzz"
        elif prime(x):
            yield "простое"
        else:
            yield x
for n in special_numbers(15):
    print(n)