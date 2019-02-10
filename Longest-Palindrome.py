

def getMaxPalindromeLength(word, left, right):
    """
    :type word: str
    :type left, right: int
    :type right = (left) or (left + 1)

    For any index in word, check if any substring fits the rules for a palindrome,
    and return the length of the palindrome. Subtracts from the left index
    (move further left on word, and adds to right index (move further right on word).

    >>> getMaxPalindromeLength('aba', 0, 0)
    1

    >>> getMaxPalindromeLength('aba', 1, 1)
    3

    >>> getMaxPalindromeLength('l000l', 2, 2)
    5

    >>> getMaxPalindromeLength('haaiii!1', 1, 2)
    2

    """


    while (left >= 0) and (right < len(word) and (word[left] == word[right])):
        left -= 1
        right += 1

    return right - left - 1



def longestPalindrome(phrase):
    """
    For every phrase (type: str), iterate over the num of characters, using
    getMaxPalindromeLength (type: func) check for the length of the longest palindromic string.
    If none, return ''.

    >>> longestPalindrome('l0001')
    'l000l'

    >>> longestPalindrome('')
    ''

    >>> longestPalindrome('haaiii!1')
    'aaii'

    """

    if len(phrase) <= 0 or type(phrase) is not str:
        return ''

    maxLen = 0
    start = 0
    end = 0

    length = len(phrase)

    for i in range(length):

        len1 = getMaxPalindromeLength(phrase, i, i)
        len2 = getMaxPalindromeLength(phrase, i, i + 1)

        maxLen = max(len1, len2)

        if maxLen > (end - start):
            start = i - ((maxLen - 1) / 2)
            end = i + maxLen / 2

    return phrase[start:end+1]



if __name__ == '__main__':
    import doctest
    doctest.testmod()

