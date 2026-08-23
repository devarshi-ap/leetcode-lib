class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set() # represents chars in current window
        maxL = 0

        # sliding window, update chars{} on slide, window slides until chars{} is balanced (.values()=1).
        l,r = 0,0
        while r < len(s):
            # print(l, r, s[l:r], mySet)
            # update chars{}
            if s[r] not in mySet: # new char, add to window/chars{}, and move r-->
                mySet.add(s[r])
                r += 1
            else: # dupe char, keep removing s[l] and sliding l until set is valid
                while s[r] in mySet:
                    mySet.discard(s[l])
                    l += 1
            maxL = max(maxL, len(mySet))
        return maxL


                
                