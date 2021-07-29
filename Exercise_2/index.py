def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def main():
    sum = 0
    for i in range(1, 35):
        n = fibonacci(i)
        while n <= 4000000:
            if n % 2 == 0:
                sum += n
            if n <= 4000000:
                break

    print(sum)

main()