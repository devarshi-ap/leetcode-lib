class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ans = ""
        for letter in s: ans += letter.lower() if letter.isalnum() else ""
        return ans == ans[::-1]