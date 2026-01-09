class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpenMap = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        bracketStack = []
        for x in s:
            if x in "([{":
                # x is opening bracket --> add to stack
                bracketStack.append(x)
            else:
                # x is closing bracket --> should expect its own opening from stack pop
                if (len(bracketStack) == 0) or bracketStack.pop() != closeToOpenMap.get(x):
                    return False
        
        # stack should be empty (closed all opening brackets in stack)
        return True if len(bracketStack) == 0 else False
