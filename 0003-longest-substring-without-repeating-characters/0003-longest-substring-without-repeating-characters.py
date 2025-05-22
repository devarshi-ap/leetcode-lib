class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxL = 0
        seen = {} # char -> count

        # window = [start:end]
        for right in range(len(s)):
            currChar = s[right]
            seen[currChar] = seen.get(currChar, 0) + 1 # add new entry or increment

            # pwwkew {p: 1, w: 1} -> +w -> {p: 1, w: 2}
            while seen[currChar] > 1:
                if seen[s[left]] == 1:
                    del seen[s[left]]
                else:
                    seen[s[left]] -= 1
                left += 1

            maxL = max(maxL, right - left + 1)
        
        return maxL
