# square of N number
def square_gener():

    N = int(input("Enter a number: "))


    for i in range(1, N + 1):
        yield i ** 2

for square in square_gener():
    print(square)


# even numbers.
def even_generator(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number: "))

even_nums = even_generator(n)

print(",".join(str(num) for num in even_nums))


# Divisable by 3 and 4.
def generate_divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input('Enter a number: '))
divisible_gen = generate_divisible_by_3_and_4(n)

for num in divisible_gen:
    print(num)

# Square of all numbers between a and b
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

a = 3
b = 7
for square in squares(a, b):
    print(square)

# Numbers from n down to 0.
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = 5
for num in countdown(n):
    print(num)
