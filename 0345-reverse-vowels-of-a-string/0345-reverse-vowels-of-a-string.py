class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        naive approach: 2-stride:
        1st stride (l-r): create stack of vowels
        2nd stride (l-r): swap out current vowel with vowels.pop()

        O(2N)
        """

        vowels = [x for x in s if x.lower() in ['a', 'e', 'i', 'o', 'u']]
        result = ""
        
        for i in range(len(s)):
            result += vowels.pop() if s[i].lower() in ['a', 'e', 'i', 'o', 'u'] else s[i]
        
        return result
                