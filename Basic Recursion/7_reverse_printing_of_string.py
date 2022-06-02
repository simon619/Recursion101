def rev_string(st, pointer):
    if pointer < 0:
        return ''
    else:
        return st[pointer] + rev_string(st, pointer - 1)


if __name__ == '__main__':
    st = str(input('Enter a String: '))
    rev = rev_string(st, len(st) - 1)
    print(f'The Reverse of "{st}" Is "{rev}" And It\'s Length is {len(rev)}')
