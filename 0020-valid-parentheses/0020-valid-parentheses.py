class Solution:
    def isValid(self, s: str) -> bool:
        targets = [] # holds closing brackets
        pairs = {"(": ")", "[": "]", "{": "}"}

        for bracket in s:
            if bracket in pairs.keys():
                # ([{ --> add closing counterpart to targets[]
                targets.append(pairs[bracket])
            else:
                # read CLOSING )]}, make sure its opening counterpart is top of targets[] before popping
                if targets:
                    if targets[-1] == bracket:
                        targets.pop()
                    else:
                        return False
                else:
                    # list is empty, unbalanced brackets
                    return False
        
        # targets better be empty
        return True if not targets else False