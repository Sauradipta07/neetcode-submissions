class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        options="+-*/"
        numstk=[]
        for i in range(len(tokens)):
            if tokens[i] not in options:
                numstk.append(int(tokens[i]))
            else:
                b=numstk.pop()
                a=numstk.pop()                              
            if tokens[i] == "+":
                numstk.append(a+b)
            if tokens[i] == "-":
                numstk.append(a-b)
            if tokens[i] == "*":
                numstk.append(a*b)
            if tokens[i] == "/":
                result=abs(a)//abs(b)
                if (a < 0) != (b < 0):
                    result = -result
                numstk.append(result)
        return numstk[-1]

        