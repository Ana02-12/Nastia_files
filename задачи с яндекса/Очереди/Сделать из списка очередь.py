def main():
    queue = []

    while True:
        command = input().split()

        #добавить
        if command[0] == 'push':
            queue.append(int(command[1]))
            print('ok')

        #забрать первый
        elif command[0] == 'pop':
            if len(queue) == 0:
                print('error')
            else:
                print(queue.pop(0))

        #посмотреть на первый
        elif command[0] == 'front':
            if len(queue) == 0:
                print('error')
            else:
                print(queue[0])

        #узнать размер
        elif command[0] == 'size':
            print(len(queue))

        #очистить список
        elif command[0] == 'clear':
            queue.clear()
            print('ok')

        #завершить
        elif command[0] == 'exit':
            print('bye')
            break



if __name__ == '__main__':
    main()
