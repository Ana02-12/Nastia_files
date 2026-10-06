class MyQueue:

    def __init__(self):
        #ожидающие своей очереди
        self.stack2 = []
        #хранит очередь
        self.stack1 = []

    #добавить элемент в ожидающих -=-=-=-=-=-=
    def push(self, x: int) -> None:
        self.stack2.append(x)

    #забрать последний -=-=-=-=-=-=-=-=-=-=-=
    def pop(self) -> int:
        self.peek() #сначала найти последний
        return self.stack1.pop()

    #посмотреть последний -=-=-=-=-=-=-=-=-=
    def peek(self) -> int:
        #если в очереди никого нет
        if not self.stack1:
            #запишем в неё ожидающих
            while self.stack2:
                last = self.stack2.pop()
                self.stack1.append(last)
        #вернем первого в очереди
        return self.stack1[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2

