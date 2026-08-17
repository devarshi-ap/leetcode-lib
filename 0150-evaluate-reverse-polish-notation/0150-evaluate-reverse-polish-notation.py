class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = [] # (int's)

        for token in tokens:
            # operator ? pop 2 nums from stack, eval, put back result
            if token in "+-/*":
                b = numStack.pop() # op2 (added last)
                a = numStack.pop() # op1

                if token == "+":
                    numStack.append(a + b)
                elif token == "-":
                    numStack.append(a - b)
                elif token == '*':
                    numStack.append(a * b)
                else:
                    numStack.append(int(a / b)) # int(..) rounds down
            # num ? add to stack
            else:
                numStack.append(int(token))

        return numStack[0] # result is last num standing in stack