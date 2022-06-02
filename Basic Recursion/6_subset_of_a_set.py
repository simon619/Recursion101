def get_subset(set, pointer):
    if pointer == -1:
        return [[]]
    smaller = get_subset(set, pointer - 1)
    extra = [set[pointer]] * 1
    new = []
    for small in smaller:
        new.append(small + extra)
    return smaller + new


if __name__ == '__main__':
    set = [1, 2, 3, 4]
    subset = get_subset(set, len(set) - 1)
    print(f'Subset of {set} is {subset} with lenght of {len(subset)}')