class MyStack:

    def __init__(self):
        self.queue = []
        self.stack = []       

    def push(self, x: int) -> None:
        self.queue.append(x) 

    def pop(self) -> int:
        while self.queue:
            self.stack.append(self.queue.pop(0))
        return self.stack.pop()
        

    def top(self) -> int:
        while self.queue:
            self.stack.append(self.queue.pop(0))
        return self.stack[-1]
        

    def empty(self) -> bool:
        return not self.stack and not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
