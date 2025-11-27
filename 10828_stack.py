import sys


class IntStack:

    def __init__(self):
        self.datas = list()
        self.size = 0

    def push(self, num):
        self.datas = self.datas.append(num)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return -1
        else:
            num = self.datas[-1]
            self.datas = self.datas[:-1]
            return num

    def size(self):
        return self.size

    def empty(self):
        if self.size == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.size == 0:
            return -1
        else:
            return self.datas[-1]


num_iter = int(sys.stdin.readline())
stacks = IntStack()
command_dict = {'push': stacks.push, 'pop': stacks.pop, 'size': stacks.size, 'empty': stacks.empty, 'top': stacks.top}
for _ in range(num_iter):
    commands = list(map(str, (sys.stdin.readline().split())))
    command = commands[0]
    function = command_dict[command]
    result = None
    if command == 'push':
        function(commands[1])
    else:
        result = function()
    if result is not None:
        print(result)
