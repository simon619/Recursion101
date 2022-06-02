def is_palidrome(s, left, right, mid):
    if left == mid:
        return True
    else:
        return s[left] == s[right] and is_palidrome(s, left + 1, right - 1, mid)


if __name__ == '__main__':
    st = str(input('Enter a string: '))
    st = st.lower()
    mid = len(st) // 2
    print(is_palidrome(st, 0, len(st) - 1, mid))
