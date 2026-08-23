class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # False if ransomNote uses more chars than available
        if len(ransomNote) > len(magazine):
            return False

        # create char-freq for magazine, then reduce from magazine while iterating through ransomNote
        char_freq = {}
        for c in magazine:
            char_freq[c] = char_freq.get(c, 0) + 1 # gets c's value (0 if not in dict) then + 1
        
        # reduce each char in ransomNote from magazine
        for c in ransomNote:
            # don't got that char
            if char_freq.get(c, 0) <= 0:
                return False
            # do got that char, reduce count
            char_freq[c] -= 1
        
        return True