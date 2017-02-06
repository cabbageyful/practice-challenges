"""
Solution to HackerRank 30 Day Challenge Day 15
Problem & sample code by @harsha_s (https://www.hackerrank.com/harsha_s)

Problem: https://www.hackerrank.com/challenges/30-linked-list

"""
# rewrite of HackerRank provided code
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LL(object):
    def printLL(self, head):
        current = head
        while current:
            print current.data
            current = current.next

    # function needed to complete solution
    def insert_node(self, head, data):
        """Given predefined global variable head, inserts data at end of LL and
        returns the head. 
        If head is None, new data will be head.
        """

        if not head:
            head = Node(data)

        else:
            self._insert_node(data, head)

        return head

    def _insert_node(self, data, current):
        if current.next is None:
            current.next = Node(data)
        else:
            current = current.next
            self._insert_node(data, current)



###############
# if __name__ == '__main__':
#     import doctest
#     if doctest.testmod.failed() == 0:
#         print '\n****WOOOOOT ALL DONE!!****'



        