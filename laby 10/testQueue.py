import unittest
from queue import Queue


class TestQueue(unittest.TestCase):

    def test_1(self):
        q = Queue()

        q.put("x")
        q.put("1")
        q.put("2")


        self.assertEqual((q.get() == "x"), 1)
        self.assertEqual((q.get() == "1"), 1)
        self.assertEqual((q.get() == "3"), 0)



        with self.assertRaises(Exception) as context:
            q.get()
        self.assertTrue("Queue is empty" in str(context.exception))








