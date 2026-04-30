from collections import deque
class MyStack:

    def __init__(self):
        self.que_1 = deque()
        self.que_2 = deque()

    def push(self, x: int) -> None:
        self.que_1.append(x)
        

    def pop(self) -> int:
        n=len(self.que_1)
        for i in range(n-1):
            popped=self.que_1.popleft()
            self.que_2.append(popped)
        self.que_1,self.que_2 = self.que_2,self.que_1
        return self.que_2.popleft()
        

    def top(self) -> int:
        n=len(self.que_1)
        for i in range(n):
            popped=self.que_1.popleft()
            self.que_2.append(popped)
        self.que_1,self.que_2 = self.que_2,self.que_1
        return popped

    def empty(self) -> bool:
        if len(self.que_1)==0:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()