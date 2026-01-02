class Solution:
    def isPalindrome(self, s: str) -> bool:
        # ptrA from start, ptrB from end
        ptrA = 0
        ptrB = len(s)-1

        if len(s) < 2: # empty string & chars = Palindrome
            return True

        while ptrA < ptrB:
            # skip non-alphanumerics and spaces
            while (not s[ptrA].isalnum() or s[ptrA] == " ") and ptrA < ptrB:
                ptrA += 1
            while (not s[ptrB].isalnum() or s[ptrB] == " ") and ptrA < ptrB:
                ptrB -= 1
            
            print(s[ptrA], ptrA, s[ptrB], ptrB)
            if s[ptrA].lower() == s[ptrB].lower(): # same char ==> move pointers in
                ptrA += 1
                ptrB -= 1
            else:
                return False # not same char ==> not palindrome
        
        return True
            