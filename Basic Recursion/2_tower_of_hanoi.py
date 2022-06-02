def move_the_disk(n, fr, to, spear):
    if n == 1:
        print(f'Disk moved from {fr} to {to}')
    else:
        move_the_disk(n - 1, fr, spear, to)
        move_the_disk(1, fr, to, spear)
        move_the_disk(n - 1, spear, to, fr)


if __name__ == '__main__':
    move_the_disk(3, 'A', 'B', 'C')  # if N = number of disk. then total moves will be 2^N - 1
