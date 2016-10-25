"""Given num_people in circle, kill [kill_every]th person, return survivor.

    >>> find_survivor(4, 2)
    1

    >>> find_survivor(41, 3)
    31


As a sanity case, if never skip anyone, the last person will be our survivor:

    >>> find_survivor(10, 1)
    10

"""
# classes for nodes

class Node(object):
    """Node template"""
    
    def __init__(self, data, prev=None, next=None):
        """node info, the node before it and the node after."""
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        """Node data"""

        return "<{}; Prev: {}; Next: {}>".format(self.data, self.prev, self.next)

# class for doubly linked list

class DoublyLinkedList(object):
    """docstring for DoublyLinkedList"""
    def __init__(self, first_node=None, last_node=None):
        """Initializes an empty head and tail on creation if none supplied."""

        assert isinstance(first_node, Node) or first_node is None
        assert isinstance(last_node, Node) or last_node is None
        self.first = first_node
        self.last = last_node

    def add_node_to_top(self, new_node):
        """Makes & adds node object to the beginning of doubly-linked list."""

        if not isinstance(new_node, Node):
            new_node = Node(new_node)

        # if no head, this node is head
        if self.first is None and self.last is None:
            self.first = new_node
            self.last = new_node

        # if there is a head, need to set current head to this node.next,
        # then change this node to head
        else:
            new_node.next = self.first
            self.first = new_node

    def add_node_to_end(self, new_node):

        if not isinstance(new_node, Node):
            new_node = Node(new_node)

        # if no tail & head, this node is the both
        if self.last is None and self.first is None:
            self.last = new_node
            self.first = new_node
        # else, set this node.prev to the current tail/last
        # then change the last node
        else:
            new_node.prev = self.last
            self.last = new_node

    def remove_node_by_index(self, index):
        pass
        # if head, then set head to head.next
        # if tail, then set tail to tail.prev
        # if other,

    def get_node_index(self, info):

        assert isinstance(info, Node), 'This is not even a node dude.'


# need to traverse the doubly linked list by index
# 


def find_survivor(num_people, kill_every):
    """Given num_people in circle, kill [kill_every]th person, return survivor."""

    assert isinstance(num_people, int), 'Please input number of people.'
    assert isinstance(kill_every, int), 'Please input number to skip.'

    people_lst = range(1, num_people + 1)

    while len(people_lst[:]) > 1:
        del people_lst[::kill_every]

    return people_lst[0]

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
