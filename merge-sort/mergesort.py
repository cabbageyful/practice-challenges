"""Merge sort.

    >>> merge_sort([19, 6, 51, 4, 42, 8])
    [4, 6, 8, 19, 42, 51]

    >>> merge_sort([3, 5, 10, 2, 1, 9, 7, 6, 4, 8])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> merge_sort([])
    []

    >>> merge_sort([7, 6])
    [6, 7]

    >>> merge_sort([16])
    [16]

"""


def merge_sort(lst):
    """Divide and conquer: reduce to lists of 0-1 items, then recombine."""

    if len(lst) < 2:
        return lst

    midpoint = len(lst) / 2

    first_lst = merge_sort(lst[:midpoint])
    second_lst = merge_sort(lst[midpoint:])

    return make_merge(first_lst, second_lst)


def make_merge(first_lst, second_lst):
    """Combine two unordered list of lists into one sorted list."""

    final = []

    while len(first_lst) > 0 or len(second_lst) > 0:
        if not first_lst:
            final.append(second_lst.pop(0))
        elif not second_lst:
            final.append(first_lst.pop(0))
        elif first_lst[0] < second_lst[0]:
            final.append(first_lst.pop(0))
        else:
            final.append(second_lst.pop(0))

    return final


def better_merge_sort(lst):
    """Try to do it in all in one function without using pop.

    >>> better_merge_sort([19, 6, 51, 4, 42, 8])
    [4, 6, 8, 19, 42, 51]

    >>> better_merge_sort([3, 5, 10, 2, 1, 9, 7, 6, 4, 8])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> better_merge_sort([])
    []

    >>> better_merge_sort([25, 26])
    [25, 26]

    """

    if len(lst) > 1:
        half = len(lst) / 2
        half_uno = better_merge_sort(lst[:half])
        half_dos = better_merge_sort(lst[half:])

        uno_idx = dos_idx = nuevo = 0

        while len(half_uno) > uno_idx and len(half_dos) > dos_idx:
            if half_uno[uno_idx] > half_dos[dos_idx]:
                lst[nuevo] = half_dos[dos_idx]
                dos_idx += 1
            else:
                lst[nuevo] = half_uno[uno_idx]
                uno_idx += 1
            nuevo += 1

        while len(half_uno) > uno_idx:
            lst[nuevo] = half_uno[uno_idx]
            uno_idx += 1
            nuevo += 1

        while len(half_dos) > dos_idx:
            lst[nuevo] = half_dos[dos_idx]
            dos_idx += 1
            nuevo += 1

    return lst



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
