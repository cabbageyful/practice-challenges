"""
>>> has_balanced_brackets("<ok>")
True

>>> has_balanced_brackets("<[ok]>")
True

>>> has_balanced_brackets("<[{(yay)}]>")
True

>>> has_balanced_brackets("<ok>")
True

>>> has_balanced_brackets("<[ok]>")
True

>>> has_balanced_brackets("<[{(yay)}]>")
True

>>> has_balanced_brackets(">")
False

>>> has_balanced_brackets("(This has {too many} ) closers. )")
False

>>> has_balanced_brackets("<{Not Ok>}")
False

>>> has_balanced_brackets("No brackets here!")
True

"""


def has_balanced_brackets(string):
    """Given a string, returns True if brackets are balanced, otherwise False.
    Bracket types checked: {}, [], (), <>

    """
    assert isinstance(string, str), 'Input must be a string'

    if not string:
        return True

    bracket_lst = set(["<", ">", "{", "}", "(", ")", "[", "]"])

    bracket_dict = {"<": ">", "{": "}", "(": ")", "[": "]" }

    brackets_in_string = []

    for ltr in string:
        if ltr in bracket_lst:
            brackets_in_string.append(ltr)

    if not brackets_in_string:
        return True
    elif (len(brackets_in_string) % 2) != 0:
        return False
    else:
        first_half = brackets_in_string[:(len(brackets_in_string)/2)]
        second_half = brackets_in_string[len(brackets_in_string)/2:]
        second_half = second_half[::-1]
        for i, j in zip(first_half, second_half):
            if j != bracket_dict[i]:
                return False
        return True
        
        



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\nALL TESTS HAVE PASSED!\n"
