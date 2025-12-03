import sys


class IntSet:

    def __init__(self):
        self.datas = list()

    def add(self, num):
        if num not in self.datas:
            self.datas.append(num)

    def remove(self, num):
        if num in self.datas:
            self.datas.remove(num)

    def check(self, num):
        if num in self.datas:
            return 1
        else:
            return 0

    def toggle(self, num):
        if num in self.datas:
            self.datas.remove(num)
        else:
            self.datas.append(num)

    def all(self):
        self.datas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    def empty(self):
        self.datas = list()


num_iter = int(sys.stdin.readline())
sets = IntSet()
command_dict = {
    'add': sets.add,
    'remove': sets.remove,
    'check': sets.check,
    'toggle': sets.toggle,
    'all': sets.all,
    'empty': sets.empty
}

for _ in range(num_iter):
    commands = list(map(str, (sys.stdin.readline().split())))
    command = commands[0]
    function = command_dict[command]
    result = None
    if command == 'all' or command == 'empty':
        function()
    elif command == 'check':
        data = int(commands[1])
        result = function(data)
    else:
        data = int(commands[1])
        function(data)
    if result is not None:
        print(result)
