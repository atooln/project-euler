# https://projecteuler.net/problem=35
import math

def isPrime(x:int):
    if x == 1:
        return True

    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True


def isCircularPrime(x:str,c:int):
    if c == len(str(x)):
        return True

    if not isPrime(int(x)):
        return False

    return isCircularPrime(x[1:]+x[0], c+1)

if __name__ == "__main__":
    count = 0
    for i in range(2,1000000):
        if isCircularPrime(str(i),0):
            print(i)
            count+=1
    print(count)
