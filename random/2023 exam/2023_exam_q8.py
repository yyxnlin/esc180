def remove_every_second_even(L, bool=True):
    if len(L) == 0:
        return []

    if L[0] % 2 == 0:
        bool = not bool
        if bool:
            return remove_every_second_even(L[1:], bool)
    return [L[0]] + remove_every_second_even(L[1:], bool)

print(remove_every_second_even([1, 2, 3, 0, 10, 11, 12, 16, 20]))