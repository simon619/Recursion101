print('Summation of nth Positive Natural Number')
print('1 + 2 + 3 + 4 + .... + n = n(n + 1) / 2')


def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)


if __name__ == '__main__':
    x = int(input('Enter the term: '))
    num = sum(x)
    print(f'Summation of 1st {x} numbers is {num}')

print('')
print('Summation Square of nth Positive Natural Number')
print('1^2 + 2^2 + 3^2 + 4^2 + .... + n^2 = n(n + 1)(2n + 1) / 6')


def sum_sq(n, end_num):
    if n == end_num:
        return n ** 2
    else:
        return n ** 2 + sum_sq(n + 1, end_num)


if __name__ == '__main__':
    x = int(input('Enter the term: '))
    num = sum_sq(0, x)
    print(f'Summation of 1st {x} numbers is {num}')

print('')
print('Summation Square of nth Positive Natural Number')
print('(-1)^0 + (-1)^1 + (-1)^2 + (-1)^3 + .... + (-1)^n = ?')

carry_the_value = []


def sum_(n, end_num):
    carry_the_value.append((-1) ** n)
    if n == end_num:
        return (-1) ** end_num
    else:
        return (-1) ** n + sum_(n + 1, end_num)


if __name__ == '__main__':
    x = int(input('Enter the term: '))
    num = sum_(0, x)
    print(f'Summatin of 1st {x} numbers is {num}')
    print(f'Series: {carry_the_value}')
