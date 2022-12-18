#10.4

class Queue:

    def __init__(self):
        self.items = []

    def __str__(self):   # podglądanie kolejki
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):   # nigdy nie jest pusta
        return False

    def put(self, data):
        if self.is_full():
            raise Exception("Queue is full!")

        self.items.append(data)

    def get(self):
        if self.is_empty():
            raise Exception("Queue is empty!")

        return self.items.pop(0)




