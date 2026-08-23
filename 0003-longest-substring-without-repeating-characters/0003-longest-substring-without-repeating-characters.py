class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set() # represents chars in current window
        maxL = 0

        # sliding window, update chars{} on slide, window slides until chars{} is balanced (.values()=1).
        l,r = 0,0
        for r, r_char in enumerate(s):
            # print(l, r, s[l:r], mySet)

            # dupe char, keep removing s[l] and sliding l--> until set is valid
            while r_char in mySet:
                mySet.discard(s[l])
                l += 1
            # new char, add to window/chars{}, and move r-->
            mySet.add(s[r])
            maxL = max(maxL, len(mySet))
        return maxL


                
                