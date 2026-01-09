class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpenMap = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        bracketStack = []
        for x in s:
            if x in "([{": # x is opening bracket --> add to stack
                bracketStack.append(x)
            else: # x is closing bracket --> should pop its expected from stack
                if (len(bracketStack) == 0) or bracketStack.pop() != closeToOpenMap.get(x):
                            return False
        
        return True if len(bracketStack) == 0 else False
