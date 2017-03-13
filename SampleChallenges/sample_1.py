"""Problem 1 for Sample Challenges.

Validate Socket Address (for Python)

You are working on an SSH client and need an auxiliary function that determines whether a given string, such as "127.12.23.43:5000", represents a valid socket address.

A valid socket address has the format x.y.z.w:port, where  x, y, z, w are integers ranging from 0 and 255, inclusive, 
and port is an integer ranging from 1 to 65,535, inclusive. 

For example, the string "127.12.23.43:5000" is a valid socket address, while the string "127.A:-12" is not.

Implement the Python function is_valid_socket that returns a boolean value indicating if its input string represents a valid socket address.

****

>>> is_valid_socket('')
False

>>> is_valid_socket('127.12.23.43:5000')
True

>>> is_valid_socket('127.A:-12')
False

>>> is_valid_socket('0.0.0.0:1')
True

>>> is_valid_socket('90.0.0.40:7456')
True

>>> is_valid_socket('afbodfid')
False

>>> is_valid_socket('155.6.6.7:65535')
True

>>> is_valid_socket('255.0.8.90:-7')
False
"""


import re

def is_valid_socket(socket_str):
    if not socket_str:
        return False

    socket_check = re.split('(\W+)', socket_str)

    if len(socket_check) != 9:
        return False

    if socket_check[1] and socket_check[3] and socket_check[5] != '.':
        return False

    if socket_check[7] != ':':
        return False

    socket_nums = socket_check[:8:2]
    port_num = socket_check[8]

    for num in socket_nums:
        if 0 > num > 255:
            return False

    if 1 > port_num > 65535:
        return False

    return True



##########################
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "GOOD JOB!!!!"