class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        naive approach: 2-stride:
        1st stride (l-r): create stack of vowels
        2nd stride (l-r): swap out current vowel with vowels.pop()
        O(2N)
        -----
        vowels = [x for x in s if x.lower() in ['a', 'e', 'i', 'o', 'u']]
        result = ""
        for i in range(len(s)):
            result += vowels.pop() if s[i].lower() in ['a', 'e', 'i', 'o', 'u'] else s[i]
        return result
        -----

        Optimized --> Two Pointers (O(N)):
        icecream
        l      r
        
        while l < r
            move l until it locks on a vowel
            move r until it locks on a vowel
            swap
            move both in
        """

        l, r = 0, len(s) - 1
        s = list(s)
        vowels = set("aeiouAEIOU")

        while l < r:
            while l < r and s[l] not in vowels: # lock L onto vowel
                l += 1
            
            while l < r and s[r] not in vowels: # lock R onto vowel
                r -= 1
            
            s[l], s[r] = s[r], s[l] # L,R both on vowels, so swap (then move both up)
            l += 1
            r -= 1
        
        return ''.join(s)