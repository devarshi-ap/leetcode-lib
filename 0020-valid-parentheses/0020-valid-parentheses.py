class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1: return False

        bracketMap = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []

        for x in s:
            if x in "([{":
                # x is opening bracket --> add to stack
                stack.append(x)
            else:
                # x is closing bracket --> should expect its own opening from stack pop
                if (len(stack) == 0) or stack.pop() != bracketMap.get(x):
                    return False
        
        return len(stack) == 0