u"""单向链表"""


from .linked_list_node import LinkedListNode


class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def tail(self):
        ite = self.head
        while ite is not None and ite.nextNode is not None:
            ite = ite.nextNode
        return ite

    def concatenate(self, another_link_list):
        tail = self.tail()

        if tail is None:
            self.head = another_link_list.head
            self.length = another_link_list.length
        else:
            tail.nextNode = another_link_list.head
            self.length += another_link_list.length

        return self

    def append(self, value):
        if self.head is None:
            self.head = LinkedListNode(value)
        else:
            ite = self.head
            while ite.next is not None:
                ite = ite.next
            ite.next = LinkedListNode(value)

        self.length += 1

        return self

    def prepend(self, value):
        if self.head is None:
            self.head = LinkedListNode(value)
        else:
            node = LinkedListNode(value, self.head.nextNode)
            self.head = node

        self.length += 1

        return self

    def search(self, value):
        if self.head is None:
            return None
        else:
            ite = self.head
            while ite.value is not value and ite.nextNode is not None:
                ite = ite.nextNode

            if ite.nextNode is None:
                return None
            else:
                return ite.value

    def remove_value(self, value):
        if self.head is None:
            return True
        elif self.head.value is value:
            self.head = None
            self.length = 0
        else:
            pre = self.head
            ite = pre.nextNode
            while ite.value is not value and ite.nextNode is not None:
                pre = ite
                ite = ite.nextNode
            if ite.value is value:
                pre.nextNode = ite.nextNode
                self.length -= 1
                return True

            return False

    def remove_nth(self, n):
        if self.head is None:
            return False
        else:
            i = 0
            pre = ite = self.head

            while i < n - 1 and ite is not None:
                i += 1
                pre = ite
                ite = ite.nextNode

            if ite is not None:
                pre.nextNode = ite.nextNode
                self.length -= 1
                return True
            else:
                return False
