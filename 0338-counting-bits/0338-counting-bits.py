class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for x in range(n+1):
            result.append(bin(x)[2:].count("1"))
        return result
