class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if stack and i in ('+','*','-','/'):
                opt1 = stack.pop()
                opt2 = stack.pop()
                if i == '+': stack.append(opt2+opt1)
                elif i == '-': stack.append(opt2-opt1)
                elif i == '*': stack.append(opt2*opt1)
                else: stack.append(int(opt2/opt1))
            else:
                stack.append(int(i))

        return stack.pop()