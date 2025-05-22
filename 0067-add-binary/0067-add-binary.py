class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
            C
         10011
             a
            
           111
             b
        -------
             S
        
        S = a + b + C
        """
        aPtr, bPtr = len(a)-1, len(b)-1
        result = ""
        carry = 0

        # keep running until both Ptr's reach 0 OR if carry = 1 (currSum still possible)
        while aPtr >= 0 or bPtr >= 0 or carry:
            # convert each digit (=0 if digit not indexable)
            digitA = int(a[aPtr]) if aPtr >= 0 else 0
            digitB = int(b[bPtr]) if bPtr >= 0 else 0
            currSum = digitA + digitB + carry
            
            # SUM -> ACTION
            # 0 -> all are 0 (result+="0", carry=0)
            # 1 -> one is 1 (result+="1", carry=0)
            # 2 -> two were 1 (result+="0", carry=1)
            # 3 -> three were 1 (result+="1", carry=1)

            result += str(currSum % 2)
            carry = 1 if currSum >= 2 else 0

            aPtr -= 1
            bPtr -= 1

        return result[::-1]