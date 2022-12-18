import random


class RandomQueue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def is_full(self):
        return False

    def insert(self, item):    # wstawia element w czasie O(1)
        if self.is_full():
            raise Exception("The queue is full!!")

        self.items.append(item)


    def remove(self):  # zwraca losowy element w czasie O(1)

        if self.is_empty():
            raise Exception("The queue is empty!!")

        idx = random.randrange(len(self.items))
        self.items[idx], self.items[-1] = self.items[-1], self.items[idx]

        return self.items.pop()


    def clear(self):   # czyszczenie listy
        self.items = []





q = RandomQueue()

q.insert("a")
q.insert("b")
q.insert("c")
q.insert("d")

print(q.remove())
#
# q.clear()
# print(q.remove())






