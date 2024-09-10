class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        left, right = 0, len(needle) - 1
        
        while right < len(haystack):
            if haystack[left:right+1] == needle:
                return left
            left += 1
            right += 1

        return -1

        