class Solution:
    def isPalindrome(self, s: str) -> bool:
        # ptrA from start, ptrB from end
        ptrA = 0
        ptrB = len(s)-1

        if len(s) < 2: # empty string & chars = Palindrome
            return True

        while ptrA < ptrB:
            # skip non-alphanumerics and spaces
            if not s[ptrA].isalnum() or s[ptrA] == " ":
                ptrA += 1
                continue
            elif not s[ptrB].isalnum() or s[ptrB] == " ":
                ptrB -= 1
                continue
            
            print(s[ptrA], ptrA, s[ptrB], ptrB)
            if s[ptrA].lower() == s[ptrB].lower(): # same char ==> move pointers in
                ptrA += 1
                ptrB -= 1
            else:
                return False # not same char ==> not palindrome
        
        return True
            