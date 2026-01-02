class Solution:
    def isPalindrome(self, s: str) -> bool:
        # ptrA from start, ptrB from end
        l = 0
        r = len(s)-1

        if len(s) < 2: # empty string & chars = Palindrome
            return True

        while l < r:
            # skip non-alphanumerics and spaces
            if not s[l].isalnum() or s[l] == " ":
                l += 1
                continue # jump back up
            elif not s[r].isalnum() or s[r] == " ":
                r -= 1
                continue # jump back up
            
            print(s[l], l, s[r], r)
            if s[l].lower() == s[r].lower(): # same char ==> move pointers in
                l += 1
                r -= 1
            else:
                return False # not same char ==> not palindrome
        
        return True
            