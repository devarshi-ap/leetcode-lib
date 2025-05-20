class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # holds closing brackets
        brackets = {"(": ")", "[": "]", "{": "}"}

        for b in s:
            if b in brackets:
                # ([{ --> add closing counterpart to targets[]
                stack.append(brackets[b])
            else:
                # )]} --> make sure its opening counterpart is top of stack before popping
                if stack and stack[-1] == b:
                        stack.pop()
                else:
                    # list is empty, unbalanced brackets
                    return False
        
        # stack better be empty
        return not stack