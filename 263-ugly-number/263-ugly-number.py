class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False if n<=0 else (2*3*5)**32 % n == 0