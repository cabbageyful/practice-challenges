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
