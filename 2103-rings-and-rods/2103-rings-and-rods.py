class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        ringCount = [""]*10
        for i in range(0, len(rings) - 1, 2): ringCount[int(rings[i+1])] += rings[i]
        sum = 0
        for r in ringCount: sum += 1 if "B" in r and "G" in r and "R" in r else 0
        return sum