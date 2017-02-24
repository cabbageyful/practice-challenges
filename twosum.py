"""Given array of numbers and an target int, return the pairs of the indicies 
where the sum of the index values equal target int.

>>> a = [1, 3, 5, 7, 9]
>>> sorted(find_twosum(a, 8))
[(1, 7), (3, 5), (5, 3), (7, 1)]

>>> sorted(find_twosum([], 0))
[]

>>> sorted(find_twosum([4, 6, 8, -1, -6, -8], 0))
[(-8, 8), (-6, 6), (6, -6), (8, -8)]

>>>

"""
from collections import defaultdict

def find_twosum(arr, target):

    target_sums = defaultdict(int)
    for num in arr:
        target_sums[num] = target - num

    sums_in_array = target_sums.items()

    for item in sums_in_array:
        if item[1] not in arr:
            sums_in_array.remove(item)

    return sums_in_array





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n****Yay all tests passed!****\n"