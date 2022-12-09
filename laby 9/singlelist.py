class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0  # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def __iter__(self):  # wykorzystanie funkcji generatora
        node = self.head
        while node:
            yield node.data
            node = node.next

    def is_empty(self):
        # return self.length == 0
        return self.head is None

    def count(self):  # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:  # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:  # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):  # klasy O(1)
        if self.head:  # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:  # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):  # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:  # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None  # czyszczenie łącza
        self.length -= 1
        return node  # zwracamy usuwany node

    def search(self, data):
        if self.is_empty():
            return None
        else:
            current = self.head
            while current.data != data:
                if current.next:
                    current = current.next
                else:
                    return None

            return current

    def find_min(self):
        if self.is_empty():
            return None
        else:
            value = self.head.data
            min_ele = self.head
            current = self.head

            for i in range(self.length):
                if (current.data < value):
                    value = current.data
                    min_ele = current
                current = current.next

        return min_ele

    def find_max(self):
        if self.is_empty():
            return None
        else:
            value = self.head.data
            max_ele = self.head
            current = self.head

            for i in range(self.length):
                if current.data > value:
                    value = current.data
                    max_ele = current
                current = current.next

        return max_ele

    def reverse(self):
        if self.is_empty():
            return None
        else:
            prev = None
            current = self.head

            while (current != None):
                next = current.next
                current.next = prev
                prev = current
                current = next
            self.head = prev
