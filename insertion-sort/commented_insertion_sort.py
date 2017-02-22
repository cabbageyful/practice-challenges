"""Insertion sort algorithm with step-by-step comments.
"""


def insertion_sort(alist):
    """Given a list, sort it using insertion sort."""

    # loop thru everything in the list except for the first item which is trivially sorted
    for i in range(1, len(alist)):
        # temp variable to store the value of the index we are currently on
        to_place = alist[i]
        # temp variable to store index prior to i. This is the end of the sorted part of the array
        sorted_pt = i - 1
        # as long as we are in range & the item we're trying to place is smaller than the item at the position of the subarray we're looping thru
        while sorted_pt >=0 and to_place < alist[sorted_pt]:
            # moves an item one space ahead in array to make room for the smaller value
            alist[sorted_pt + 1] = alist[sorted_pt]
            # decrements the sorted pt index to account for the item that was just moved
            #    when sorted_pt is -1, means we have reached the beginning of alist
            sorted_pt = sorted_pt - 1
        # if sorted_pt is -1, and the item we're placing is smaller than every other item in the array 
        alist[sorted_pt + 1] = to_place

    return alist
    