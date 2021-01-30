class Deque:
    def __init__(self):
        self.back_stack = []
        self.front_stack = []

    def push_front(self, key):
        self.front_stack.append(key)
        return "ok"

    def push_back(self, key):
        self.back_stack.append(key)
        return "ok"

    def pop_front(self):
        if len(self.back_stack) == 0 and len(self.front_stack) == 0:
            return "error"
        if len(self.front_stack) != 0:
            return self.front_stack.pop()
        if len(self.front_stack) == 0 and len(self.back_stack) != 0:
            self.front_stack = self.back_stack[::-1]
            self.back_stack = []
            return self.front_stack.pop()

    def pop_back(self):
        if len(self.back_stack) == 0 and len(self.front_stack) == 0:
            return "error"
        if len(self.back_stack) != 0:
            return self.back_stack.pop()
        if len(self.back_stack) == 0 and len(self.front_stack) != 0:
            self.back_stack = self.front_stack[::-1]
            self.front_stack = []
            return self.back_stack.pop()

    def front(self):
        if len(self.back_stack) == 0 and len(self.front_stack) == 0:
            return "error"
        if len(self.front_stack) != 0:
            return self.front_stack[-1]
        if len(self.front_stack) == 0 and len(self.back_stack) != 0:
            return self.back_stack[0]

    def back(self):
        if len(self.back_stack) == 0 and len(self.front_stack) == 0:
            return "error"
        if len(self.back_stack) != 0:
            return self.back_stack[-1]
        if len(self.back_stack) == 0 and len(self.front_stack) != 0:
            return self.front_stack[0]

    def clear(self):
        self.back_stack.clear()
        self.front_stack.clear()
        return "ok"

    def size(self):
        return len(self.back_stack) + len(self.front_stack)


def process_deque(commands):
    deque = Deque()
    result = []
    for command in commands:
        command_splitted = command.split()
        operation = command_splitted[0]
        if operation == "push_front":
            result.append(deque.push_front(int(command_splitted[1])))
        if operation == "push_back":
            result.append(deque.push_back(int(command_splitted[1])))
        if operation == "pop_front":
            result.append(deque.pop_front())
        if operation == "pop_back":
            result.append(deque.pop_back())
        if operation == "front":
            result.append(deque.front())
        if operation == "back":
            result.append(deque.back())
        if operation == "size":
            result.append(deque.size())
        if operation == "clear":
            result.append(deque.clear())
    return result