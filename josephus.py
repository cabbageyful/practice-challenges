# """Given num_people in circle, kill [kill_every]th person, return survivor.

#     >>> find_survivor(4, 2)
#     1

#     >>> find_survivor(41, 3)
#     31


# As a sanity case, if never skip anyone, the last person will be our survivor:

#     >>> find_survivor(10, 1)
#     10

# """


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

    pass

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"


# class DoublyLinkedList(object):
#     """docstring for DoublyLinkedList"""
#     def __init__(self, first_node=None, last_node=None):
#         """Initializes an empty head and tail on creation if none supplied."""

#         assert isinstance(first_node, Node) or first_node is None
#         assert isinstance(last_node, Node) or last_node is None
#         self.first = first_node
#         self.last = last_node

#     def print_list(self):
#         """Prints out the list."""
#         current = self.first

#         while current is not None:
#             print current
#             current = current.next

#         return current

#     def add_node_to_top(self, new_node):
#         """Makes & adds node object to the beginning of doubly-linked list."""

#         if not isinstance(new_node, Node):
#             new_node = Node(new_node)

#         # if no head, this node is head
#         if self.first is None and self.last is None:
#             self.first = new_node
#             self.last = new_node

#         # if there is a head, need to set current head to this node.next,
#         # then change this node to head
#         else:
#             new_node.next = self.first
#             self.first = new_node

#     def add_node_to_end(self, new_node):
#         """Adds a node to the end of the list."""

#         if not isinstance(new_node, Node):
#             new_node = Node(new_node)

#         # if no tail & head, this node is the both
#         if self.last is None and self.first is None:
#             self.last = new_node
#             self.first = new_node
#         # else, set this node.prev to the current tail/last
#         # then change the last node
#         else:
#             new_node.prev = self.last
#             self.last = new_node

#     def remove_node_by_index(self, index):
#         """Given the index of a node, removes the node from the doubly-linked list."""
#         # if head, then set head to head.next
#         previous = None
#         current = self.first
#         counter = 0

#         while current is not None and (counter < index):
#             previous = current
#             current = current.next
#             counter += 1

#         # at this point we're at our node, if index was first removed was the first/head
#         if previous is None:
#             self.first = current.next
#         # if at another node in the list, then need to set the previous node's next to the current node's next
#         else:
#             previous.next = current.next

#     def get_node_by_index(self, index):
#         """Returns node data given an index."""

#         if self.first is None:
#             return None

#         idx_counter = 0
#         current = self.first

#         while idx_counter < index:
#             idx_counter += 1
#             current = current.next

#         return current    # should work if index isnt in range, should return None
