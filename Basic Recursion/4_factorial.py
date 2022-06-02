def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    x = int(input('Enter A Positive Integer Number: '))
    num = factorial(x)
    print(f'Factorial of {x} is {num}')
