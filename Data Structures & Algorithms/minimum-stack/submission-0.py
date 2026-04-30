class MinStack:
    def __init__(self):
        self.items = []      # regular stack
        self.mins   = []      # parallel stack of current minimums

    # ---------- helpers ----------
    def is_empty(self) -> bool:
        return not self.items

    # ---------- core API ----------
    def push(self, val: int) -> None:
        self.items.append(val)
        # push new min
        if not self.mins or val <= self.mins[-1]:
            self.mins.append(val)
        else:
            self.mins.append(self.mins[-1])

    def pop(self) -> None:
        if self.is_empty():
            raise IndexError("pop from empty stack")
        self.mins.pop()
        self.items.pop()

    def top(self) -> int:
        if self.is_empty():
            raise IndexError("top from empty stack")
        return self.items[-1]

    def getMin(self) -> int:
        if self.is_empty():
            raise IndexError("getMin from empty stack")
        return self.mins[-1]