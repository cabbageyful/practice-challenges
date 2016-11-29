"""Given two lists, find the smallest difference between any two nums.

For example, given the lists:

  {10, 20, 14, 16, 18}
  {30, 23, 54, 33, 96}

The result would be 3, since 23 - 20 = 3 is the smallest difference of
any pair of numbers in those lists.

IMPORTANT: you must solve this with an algorithm that is faster than
O(ab)---that is, you cannot compare each item of list a against
each item of list b (that would be O(ab) time).

Joel Burton <joel@joelburton.com>.

Adapted from a problem in `Cracking the Coding Interview, 6th Edition`.
Gayle Laakmann McDowell, Career Cup (Palo Alto, CA). 2015.
"""


def smallest_diff(a, b):
    """Return smallest diff between all items in a and b, comparing one item
    from each list.

        >>> smallest_diff([10, 20, 30, 40], [15, 25, 33, 45])
        3

        >>> smallest_diff([101, 100, 102, 305], [3, 4, 99, 95])
        1
    """

    sorted_a = sorted(a)
    sorted_b = sorted(b)

    merged_ab = []

    while len(sorted_a) > 0 or len(sorted_b) > 0:
        if not sorted_a:
            merged_ab.append(sorted_b.pop(0))
        elif not sorted_b:
            merged_ab.append(sorted_a.pop(0))
        elif sorted_a[0] < sorted_b[0]:
            merged_ab.append(sorted_a.pop(0))
        elif sorted_b[0] < sorted_a[0]:
            merged_ab.append(sorted_b.pop(0))

    differences = set()

    for i in range(len(merged_ab) - 1):
        differences.add(abs(merged_ab[i + 1] - merged_ab[i]))

    return min(differences)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE WORK!\n"
