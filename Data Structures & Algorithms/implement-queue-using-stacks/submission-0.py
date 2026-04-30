class MyQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        n=len(self.stack1)
        for i in range(n-1):
            popped=self.stack1.pop()
            self.stack2.append(popped)
        top=self.stack1[-1]    
        self.stack1 = self.stack2[::-1]
        self.stack2=[]
        return top
        

    def peek(self) -> int:
        n=len(self.stack1)
        for i in range(n-1):
            popped=self.stack1.pop()
            self.stack2.append(popped)
        top=self.stack1[-1]
        m=len(self.stack2)
        for i in range(m):
            popped=self.stack2.pop()
            self.stack1.append(popped)
        return top


        

    def empty(self) -> bool:
        return len(self.stack1)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()