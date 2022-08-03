import unittest


# очередь на кольцевом буфере
class LimitedQueue():
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('Очередь переполнена, добавление невозможно')

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x


# очередь на связном списке
class Node():
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class ListQueue():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, Node):
        Node.next = None
        if self.is_empty():
            self.head = Node
            self.tail = Node
        else:
            self.tail.next = Node
            self.tail = Node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        result, self.head = self.head, self.head.next
        self.size -= 1
        return result


class QueueTest(unittest.TestCase):
    def setUp(self):
        self.node5 = Node('node5')
        self.node4 = Node('node4')
        self.node3 = Node('node3')
        self.node2 = Node('node2')
        self.node1 = Node('node1')

    def some_test(self, queue):
        queue.push(self.node1)
        assert not queue.is_empty()
        queue.push(self.node2)
        assert queue.pop().value == 'node1'
        assert queue.pop().value == 'node2'
        assert queue.is_empty()
        queue.push(self.node3)
        queue.push(self.node4)
        queue.push(self.node5)
        assert queue.size == 3

    def test_limit(self):
        queue = LimitedQueue(5)
        self.some_test(queue)
        assert queue.queue[queue.head] == self.node3
        # поскольку в tail хранится индекс элемента, в который должна быть
        # произведена следующая запись, последний добавленный элемент имеет
        # индекс tail - 1
        assert queue.queue[queue.tail - 1] == self.node5

    def test_list(self):
        queue = ListQueue()
        self.some_test(queue)
        assert queue.head == self.node3
        assert queue.tail == self.node5


if __name__ == '__main__':
    unittest.main()
