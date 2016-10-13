# Uber whiteboarding


def calculate_total(num_str):
    """Given a string with addition and/or multiplication operations and integers, returns
    the mathematical result.

        >>> calculate_total('1+2*3')
        7

        >>> calculate_total('')
        0

        >>> calculate_total('54*10*10')
        5400

        >>> calculate_total('7+6*0')
        7

        >>> calculate_total('4+5+6')
        15

    """

    if not num_str:
        return 0

    assert isinstance(num_str, str), 'Input must be a string.'

    valid_operands = set(['+', '*'])
    valid_nums = {str(number) for number in range(10)}

    valid_input = valid_operands | valid_nums

    assert not ({num for num in num_str} - valid_input), 'Only ints, * or + allowed in the input string.'

    add_this_lst = num_str.split('+')
    # ['1', '2*3']

    for i in range(len(add_this_lst)):
        if '*' in add_this_lst[i]:          # there is a *, so we need to do multiplication 1st
            multiply_only = add_this_lst[i].split('*')
            multiply_total = 1
            for mult_num in multiply_only:
                multiply_total *= int(mult_num)
            add_this_lst[i] = multiply_total         # change out multiplication operations w/ their value

    # print add_this_lst

    total = 0
    for j in range(len(add_this_lst)):
        total += int(add_this_lst[j])

    return total


def find_total(number_str):
    """Recursively find the total of a string of integers with either + or minus."""

    pass    

if __name__ == '__main__':
    from doctest import testmod
    if testmod().failed == 0:
        print 'What what! You did it!'


