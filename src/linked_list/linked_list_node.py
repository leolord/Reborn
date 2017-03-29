class LinkedListNode:
    value = None,
    nextNode = None,

    def __init__(self, value, next_node = None):
        self.value = value
        self.nextNode = next_node

    def set_next(self, next_node):
        self.nextNode = next_node

    def set_value(self, value):
        self.value = value
