class MinStack:
    

    def __init__(self):
        self.stk=[]
        self.min_stk=[]
        

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.min_stk or val<=self.min_stk[-1]:
            self.min_stk.append(val)
        else:
            self.min_stk.append(self.min_stk[-1])

    def pop(self) -> None:
        if not self.stk:
            return -1
        self.stk.pop()
        self.min_stk.pop()

        

    def top(self) -> int:
        if not self.stk:
            return -1
        return self.stk[-1]
        

    def getMin(self) -> int:
        if not self.min_stk:
            return -1
        return self.min_stk[-1]
        
