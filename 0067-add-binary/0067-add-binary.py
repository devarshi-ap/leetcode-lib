class Solution:
    def addBinary(self, a: str, b: str) -> str:
        intA, intB = int(a, 2), int(b, 2)
        return str(bin(intA + intB))[2:]