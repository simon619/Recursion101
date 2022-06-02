import time

print('Fibonacci in Iterative Way')
print('--------------------------')


def fibo1(n):
    length = n + 1  # Index of the list is positive natural number
    seq = [0] * length
    seq[1] = seq[2] = 1
    for i in range(3, len(seq)):
        seq[i] = seq[i - 1] + seq[i - 2]

    seq.pop(0)
    return seq[len(seq) - 1], seq  # Time complexity in Linear


if __name__ == '__main__':
    term = int(input('Enter a term and term has to be greater than 2: '))
    num, series = fibo1(term)
    print(f'{term}th number is {num}')
    print(f'Series is {series}')

print('Fibonacci in Recursive Way')
print('--------------------------')


def fibo2(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo2(n - 1) + fibo2(n - 2)  # Time complexity is 2^n


if __name__ == '__main__':
    term = int(input('Enter a term and term has to be greater than 2: '))
    num = fibo2(term)
    print(f'{term}th number is {num}')

