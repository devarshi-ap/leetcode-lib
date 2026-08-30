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
                # add to stack if opening bracket
                print(f"added {x} to stack")
                stack.append(x)
            else:
                # expect from pop if closing bracket
                expected = bracketMap.get(x)
                if len(stack) > 0:
                    actual = stack.pop()
                    print(f"{x}: {expected} vs. {actual}")
                    if expected != actual:
                        return False
                else:
                    return False
        
        return len(stack) == 0
        
        return 
