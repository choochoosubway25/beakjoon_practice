import sys


class IntQueue:

    def __init__(self):
        self.datas = list()
        self.sizes = 0

    def push(self, num):
        self.datas.append(num)
        self.sizes += 1

    def pop(self):
        if self.sizes == 0:
            return -1
        else:
            num = self.datas[0]
            self.datas = self.datas[1:]
            self.sizes -= 1
            return num

    def size(self):
        return self.sizes

    def empty(self):
        if self.sizes == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.sizes == 0:
            return -1
        else:
            return self.datas[0]

    def back(self):
        if self.sizes == 0:
            return -1
        else:
            return self.datas[-1]


num_iter = int(sys.stdin.readline())
queues = IntQueue()
command_dict = {
    'push': queues.push,
    'pop': queues.pop,
    'size': queues.size,
    'empty': queues.empty,
    'front': queues.front,
    'back': queues.back
}
for _ in range(num_iter):
    commands = list(map(str, (sys.stdin.readline().split())))
    command = commands[0]
    function = command_dict[command]
    result = None
    if command == 'push':
        commands[1] = int(commands[1])
        function(commands[1])
    else:
        result = function()
    if result is not None:
        print(result)
