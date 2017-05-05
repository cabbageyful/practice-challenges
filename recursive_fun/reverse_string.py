""" 
>>> reverse_string('tacocat')
'tacocat'

>>> reverse_string('jennifer')
'refinnej'

>>> reverse_string('chicken dinner')
'rennid nekcihc'

>>> reverse_string('ayyy')
'yyya'

>>> reverse_string('a')
'a'

>>> reverse_string('')
''

>>> reverse_string('i put my thing down flip it and reverse it')
'ti esrever dna ti pilf nwod gniht ym tup i'


"""

def reverse_string(words):
    if len(words) < 2:
        return words

    return reverse_string(words[-1]) + reverse_string(words[:-1])



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "/ All tests passed \\"

