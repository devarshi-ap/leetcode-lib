class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        The key to this problem is recognizing that each valid arrangement of cards we can choose is equivalent to removing n - k cards from the middle of the array, where n is the length of the array

        1 2 3 4 5 | k=2

        All valid arrangements of k-cards:
        - - 3 4 5
        1 - - 4 5
        1 2 - - 5
        1 2 3 - -
        """
        totalSum = sum(cardPoints)
        
        if k >= len(cardPoints):
            return totalSum

        currSum = maxPts = l = r = 0

        while r < len(cardPoints):
            currSum += cardPoints[r]

            if r - l + 1 == len(cardPoints) - k:
                maxPts = max(maxPts, totalSum - currSum)
                currSum -= cardPoints[l]
                l += 1
            r += 1
        
        return maxPts