class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        matches = 0
        balance = 0
        for char in s:
            balance += 1 if char == 'R' else -1
            if balance == 0:
                matches += 1

        return matches
        