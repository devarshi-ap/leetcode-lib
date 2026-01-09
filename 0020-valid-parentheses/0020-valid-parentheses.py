class Solution:
    def isValid(self, s: str) -> bool:
        bracketStack = []
        for x in s:
            if x in "([{": # x is opening bracket add to stack
                bracketStack.append(x)
            else: # x is closing bracket (should pop its expected from stack)
                match x:
                    case ")":
                        if (len(bracketStack) == 0) or bracketStack.pop() != "(":
                            return False
                    case "]":
                        if (len(bracketStack) == 0) or bracketStack.pop() != "[":
                            return False
                    case "}":
                        if (len(bracketStack) == 0) or bracketStack.pop() != "{":
                            return False
        
        return True if len(bracketStack) == 0 else False
