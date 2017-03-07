"""Given two input arrays with values containing integers between 0-9,
return an array with integers between 0-9.

>>> a = [5, 6, 9, 4]
>>> b = [1, 3, 4, 8]
>>> add_two_arrays(a, b)
[7, 1, 4, 2]

>>> c = [1, 3, 5]
>>> d = [7, 8]
>>> add_two_arrays(c, d)
[2, 1, 3]

>>> add_two_arrays([], [])
None

"""

def add_two_arrays(lst1, lst2):

    if len(lst1) > len(lst2):
        longer_lst = lst1
        shorter_lst = lst2
    else:
        longer_lst = lst2
        shorter_lst = lst1

    output_array = []

    for i in range(len((longer_lst - 1), -1, -1):

        while shorter_lst[i] is not None:
            current_sum = longer_lst[i] + shorter_lst[i]
            if current_sum > 9 and i > 0:
                output_array.append(current_sum-10)
                longer_lst[i-1] = longer_lst[i-1] + 1    # check dis

            elif current_sum > 9 and i == 0:
                output_array.append(current_sum-10)
                output_array.append(1)

        else:
            if longer_lst[i] > 9:
                output_array.append(longer_lst[i]-10)
                longer_lst[i-1] = longer_lst[i-1] + 1

            else:
                longer_lst[]      


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\nGOOD WORK!! ALL TESTS HAVE PASSED!!\n"