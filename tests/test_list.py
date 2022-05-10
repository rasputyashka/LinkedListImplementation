import sys
import pathlib
import unittest
from string import ascii_letters
from random import shuffle


BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from main import LinkedList


class TestingLinkedList(unittest.TestCase):

    def test_init(self):
        letters = list(ascii_letters)
        shuffle(letters)
        list1 = LinkedList(letters)
        list2 = LinkedList(letters)
        self.assertEqual(list1, list2)

    def test_iter(self):
        letters = list(ascii_letters)
        for i in range(100):
            shuffle(letters)
            list1 = list(LinkedList(letters))
            list2 = list(LinkedList(letters))
            self.assertEqual(list1, list2)

    def test_contains(self):
        letters = list(ascii_letters)
        shuffle(letters)
        test_list = LinkedList(letters)
        for letter in letters:
            self.assertIn(letter, test_list)

    def test_len(self):
        for i in range(100):
            test_list = LinkedList(range(i))
            self.assertEqual(len(test_list), i)

    def test_reversed(self):
        letters = list(ascii_letters)
        for i in range(100):
            shuffle(letters)
            self.assertEqual(list(LinkedList(letters))[::-1], list(reversed(LinkedList(letters))))

    def test_getitem(self):
        letters = list(ascii_letters)
        for i in range(len(letters)):
            shuffle(letters)
            test_list = LinkedList(letters)
            self.assertEqual(test_list[i], letters[i])

    def test_appending(self):
        test_list = []
        test_linked_list = LinkedList()
        for i in range(100):
            self.assertEqual(test_list, list(test_linked_list))
            test_list.append(i)
            test_linked_list.append(i)

    def test_popping(self):
        N = 100
        test_list = list(range(N))
        test_linked_list = LinkedList(range(N))
        for i in range(N):
            self.assertEqual(test_list, list(test_linked_list))
            self.assertEqual(test_list.pop(), test_linked_list.pop())

    def test_left_appending(self):
        test_list = []
        test_linked_list = LinkedList()
        for i in range(100):
            self.assertEqual(test_list, list(test_linked_list))
            test_list.insert(0, i)
            test_linked_list.append_left(i)

    def test_left_popping(self):
        N = 100
        test_list = list(range(N))
        test_linked_list = LinkedList(range(N))
        for i in range(N):
            self.assertEqual(test_list, list(test_linked_list))
            self.assertEqual(test_list[0], test_linked_list.pop_left())
            del test_list[0]


if __name__ == '__main__':
    unittest.main()
