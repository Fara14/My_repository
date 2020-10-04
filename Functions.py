#receives two numbers as input. Return a tuple: the sum and product of the given numbers
def f1(x, y):
    return (x + y, x * y)

print(f1(4, 10))


#calculates sqrt(x + sqrt(y))
def f2(x, y):
    return (x + y ** 0.5) ** 0.5

print(f2(5, 16))


#prints numbers between 1000 and 4250 (both inclusive) that are divisible by 5 but not divisible by 3
def f3(x, y):
    a = []
    for i in range(x, y + 1):
        if i % 5 == 0 and i % 3 != 0:
            a.append(i)
    return a

print(f3(1000, 4250))


#takes a number as input. If it is from 3 to 6 inclusive, then decrease it by 13. If it is from 8 to 41, then decrease it by 50.
# If it is not more than 0 or more than 2000, then increase it by 4 times. Otherwise, make it zero. Return the result
def f4(x):
    if 3 <= x <= 6:
        return x - 13
    elif 8 < x < 41:
        return x - 50
    elif x <= 0 or x > 2000:
        return x * 4
    else: return int(x == 0)

print(f4(2))


#takes a value in Celsius and displays the temperature in Fahrenheit
def f5(x):
    return (9/5) * x + 32

print(f5(0))


#at the entrance receives the amount of the deposit in the bank and the annual interest.
# Display the amount of the deposit after 5 years
def f6(x, y):
    return (x * (1 + 0.01 * y) ** 5)

print(f6(200000, 5))

#receives as input the number of weeks, months, years and displays the number of days during this time.
# Assume that there are 30 days in a month.
def f7(x, y, z):
    return x * 7, y * 30, z * 360

print(f7(0, 4, 3))

#returns prime factors of a given number
def f8(x):
    a = []
    for i in range(1, x + 1):
        if x % i == 0:
            a.append(i)
    return a

print(f8(40))

#returns all divisors of a given natural number
def f9(x):
    return x
#я не понял задания f8 и f9 :(