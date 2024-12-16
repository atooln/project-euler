# https://projecteuler.net/problem=1


def mult_3_5(arr:list):
    count = 0
    for i in arr:
        if i%3==0 or i%5==0:
            count+=i
    return count - arr[-1]




if __name__ == "__main__":
    test = [i+1 for i in range(1000)]
    print(test)
    print(mult_3_5(test))
