
"""
>>> length_count(range(50))
50

>>> length_count(range(9))
9

>>> length_count('ayyy')
4

>>> length_count([])
0

>>> length_count(['black', 'lives', 'matter'])
3

>>> length_count(['i', 'love', 'recursion', 'like', 'i', 'love', 'recursion'])
7

>>> length_count([1])
1

>>> length_count('There is no economic justice without racial justice.')
52

"""


def length_count(thing):
    if not thing:
        return 0

    return 1 + length_count(thing[1:])



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "**Passed**"