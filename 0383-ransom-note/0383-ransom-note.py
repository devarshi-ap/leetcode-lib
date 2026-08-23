class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # create char-freq for magazine, then reduce from magazine while iterating through ransomNote
        char_freq = {}
        for c in magazine:
            char_freq[c] = char_freq.get(c, 0) + 1 # gets c's value (0 if not in dict) then + 1
        
        for c in ransomNote:
            if c not in char_freq:
                return False
            elif char_freq[c] >= 2:
                char_freq[c] -= 1
            else:
                char_freq.pop(c)
        return True