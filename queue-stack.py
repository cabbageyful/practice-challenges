"""HackerRank 30 Day Challenge day 18.
Implement a class that has two instance variables, stack and queue, and
respective methods.

Both are implemented with lists, so the Queue dequeue method is O(n) and not O(1).

Problem written by @blondiebytes
"""

class StackQueue(object):
    """Not a stack and queue but a stack AND a queue."""
    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, char):
        """Pushes a character from a string to the end of stack."""
        self.stack.append(char)


    def enqueueCharacter(self, char):
        self.queue.append(char)


    def popCharacter(self):

        return self.stack.pop()

    def dequeueCharacter(self):

        return self.queue.pop(0)