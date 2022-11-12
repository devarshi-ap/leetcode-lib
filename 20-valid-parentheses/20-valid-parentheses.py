class Solution(object):
    def paren_matches(self, p, t):
        if p == "(" and t == ")":
            return True
        elif p == "[" and t == "]":
            return True
        elif p == "{" and t == "}":
            return True
        else:
            return False

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        isBalanced = True
        idx = 0

        while idx < len(s) and isBalanced:
            paren = s[idx]
            if paren in "({[":
                stk.append(paren)
            else:
                if stk == []:
                    isBalanced = False
                else:
                    top = stk.pop()
                    if not self.paren_matches(top, paren):
                        isBalanced = False
            idx += 1

        return True if stk == [] and isBalanced else False
        