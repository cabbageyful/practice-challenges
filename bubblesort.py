"""HackerRank 30 day challenge day 20
Bubble Sort 
"""

def bubble_sort(lst):
    """Given array a, of size n, sort in ascending order.
    Once sorted, prints info on numSwaps needed, firstElement, lastElement
    """

    numSwaps = 0

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j + 1] < lst[j]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                numSwaps += 1

    print 'Array is sorted in {} swaps.\nFirst Element: {}\nLast Element: {}'.format(numSwaps, lst[0], lst[-1])
