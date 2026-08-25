class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """ naive (won't work for cars, [car, ca, rs]):
        for w in wordDict: s = s.replace(w, "")
        return not s
        """

        # create boolean-char table (true=marked; want all marked)
        n = len(s) + 1
        dp = [False]*n
        dp[0] = True # arr[0] = ""

        # loop through, check if in wordDict, create new checkpoints marked True
        for i in range(n):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        
        return dp[-1]