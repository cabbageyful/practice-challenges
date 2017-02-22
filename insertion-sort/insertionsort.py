"""Given a list, sort it using insertion sort.

For example::

    >>> from random import shuffle
    >>> alist = range(1, 11)

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> x = [3, 7, 4, 9, 5, 2, 6, 1]
    >>> insertion_sort(x)
    [1, 2, 3, 4, 5, 6, 7, 9]
"""


def insertion_sort(alist):
    """Given a list, sort it using insertion sort."""


    for i in range(1, len(alist)):
        to_place = alist[i]
        sorted_pt = i - 1
        while sorted_pt >=0 and alist[sorted_pt] > to_place:
            
            alist[sorted_pt + 1] = alist[sorted_pt]
            sorted_pt = sorted_pt - 1
        alist[sorted_pt + 1] = to_place

    return alist
    

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE SORTING!\n"
