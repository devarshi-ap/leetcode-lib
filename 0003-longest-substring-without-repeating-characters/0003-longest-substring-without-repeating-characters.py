class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maxL = 0
        seen = {} # char -> count

        # window = [start:end]
        for end in range(len(s)):
            currChar = s[end]
            seen[currChar] = seen.get(currChar, 0) + 1 # add new entry or increment

            # pwwkew {p: 1, w: 1} -> +w -> {p: 1, w: 2}
            while seen[currChar] > 1:
                if seen[s[start]] == 1:
                    del seen[s[start]]
                else:
                    seen[s[start]] -= 1
                start += 1

            maxL = max(maxL, end - start + 1)
        
        return maxL
