# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i += 6

    return True


t = int(input())
for i in range(t):
    n = int(input())
    if (isPrime(n)):
        print("Prime")
    else:
        print("Not prime")

