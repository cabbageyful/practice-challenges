"""Given num_people in circle, kill [kill_every]th person, return survivor.

    >>> find_survivor(4, 2)
    1

    >>> find_survivor(41, 3)
    31


As a sanity case, if never skip anyone, the last person will be our survivor:

    >>> find_survivor(10, 1)
    10

"""


class Node(object):
    """Node template"""

    def __init__(self, data, prev=None, next=None):
        """node info, the node before it and the node after."""
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        """Node data"""

        return "<Data: {}, Prev: {}, Next: {}>".format(self.data, self.prev, self.next)

    @classmethod
    def make_dll(cls, num):
        """Given num items, creates a doubly-linked list.

            >>> test1 = Node.make_dll(5)

            >>> test1.data
            1

            >>> test1.next.next.next.data
            4

            >>> test1.prev.data
            5
        """

        assert 1 < num, 'Insert number greater than 1.'

        # make a circle, where last node.next will point to head

        head = current = previous = cls(1)

        for n in range(2, num + 1):
            # make current node instance w/ prev set to whatever prev is now
            current = Node(n, prev=previous)
            # make prev's next attr equal to current node
            previous.next = current
            # prev can be reset to current node b4 looping again
            previous = current

        # set the last 'current' node's next attr to head
        # set head's prev attr to 'current' so we have a full circle
        current.next = head
        head.prev = current

        return head


def find_survivor(num_people, kill_every):
    """Given num_people in circle, kill [kill_every]th person, return survivor."""

    target = Node.make_dll(num_people)

    while target.next != target:
        # counting from target, go to the killeveryth person
        # 

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
