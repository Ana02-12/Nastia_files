#импортируем очередь с двумя концами
from collections import deque
#чтобы сымитировать обычную очередь
#представим, что у нас есть только два метода
#append() - добавить в конец
#popleft() - забрать из начала

#вариаант с одной очередью -=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-
class MyStack:

    def __init__(self):
        #атрибут для хранения очереди
        #[← взять     положить →]
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)

        #перемещаем все элементы,
        #которые были до x, в конец очереди
        for _ in range(len(self.queue) - 1):
            #первый элемент очереди
            first = self.queue.popleft()
            #добавим его в конец
            self.queue.append(first)

    def pop(self):
        return self.queue.popleft()

    def top(self):
        return self.queue[0]

    def empty(self):
        return len(self.queue) == 0
#вариант две очереди -=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-
class Mystack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        self.queue2.append(x)
        while self.queue1:
            first = self.queue1.popleft()
            self.queue2.append(first)
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        return self.queue1.popleft()

    def top(self):
        return self.queue1[0]

    def empty(self):
        return len(self.queue1) == 0






























