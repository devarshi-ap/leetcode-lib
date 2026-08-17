class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # scan L->R
        numStack = []
        for x in tokens:
            # read operator (+-/*) ? pop 2 nums from stack & eval
            if x in "+-/*":
                b = numStack.pop() # op2 (added last)
                a = numStack.pop() # op1
                evalStr = a+x+b # ie. op1+op2
                result = eval(f"int({evalStr})")
                # print(evalStr,"=",result)
                numStack.append(str(result))
                # print(numStack)
            # read num ? go in stack
            else:
                numStack.append(x)
                # print(numStack)
        return int(numStack[0]) # result is last num standing in stack