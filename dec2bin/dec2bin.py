import string

"""Convert a decimal number to binary representation.

For example::

    >>> dec2bin(0)
    '0'

    >>> dec2bin(1)
    '1'

    >>> dec2bin(2)
    '10'

    >>> dec2bin(4)
    '100'

    >>> dec2bin(15)
    '1111'

    >>> dec2bin(100)
    '1100100'

    >>> dec2bin(-5)
    '101'

"""
# For example, using our alternate solution::

#     >>> dec2bin_forwards(0)
#     '0'

#     >>> dec2bin_forwards(1)
#     '1'

#     >>> dec2bin_forwards(2)
#     '10'

#     >>> dec2bin_forwards(4)
#     '100'

#     >>> dec2bin_forwards(15)
#     '1111'


def dec2bin(num):
    """Convert a decimal number to binary representation."""

    assert isinstance(num, int), 'Please input an integer'

    binary_num = '0'

    if num == 0:
        return binary_num

    # iterate only through range of numbers starting with 1 and including number
    # if it's an odd number, add a 1 at the end of binary number string
    # if it's even, and there is at least a zero in the string, but a 1
        # where the last zero is and change everything after that to a zero
    # if it's even and there are no zeros, we need to reset to a 1 followed by zeros and increase
        # the length of the binary number string by 1

    for i in range(1, num + 1):
        if i % 2 != 0:
            binary_num = binary_num[:-1] + '1'
        else:
            if binary_num.rfind('0') != -1:
                last_zero = binary_num.rfind('0')
                binary_num = binary_num[:last_zero] + '1' + binary_num[last_zero + 1:].replace('1', '0')
            else:
                binary_num = '1' + '0'*len(binary_num)

    return binary_num



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
