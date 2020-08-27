import math


def isPrime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


my_number = int(input("Nhập vào một số nguyên N = "))
count = 0
for i in range(1, my_number + 1):
    if isPrime(i):
        count += 1
print(count)