class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        left = 0
        maxFruits = 0

        # window = [left, right]
        # window expands by right++, shrinks by left++
        for right in range(len(fruits)):
            # new-map/increment current fruit @ idx=right -> dict
            currFruit = fruits[right]
            basket[currFruit] = basket.get(currFruit, 0) + 1

            # if dict gets 3rd fruit entry, shrink window from left
            while len(basket) > 2:
                leftFruit = fruits[left]
                basket[leftFruit] -= 1
                if basket[leftFruit] == 0: # no more leftFruit in either basket, remove entry
                    del basket[leftFruit]
                left += 1
            
            # update max
            maxFruits = max(maxFruits, right - left + 1)
        return maxFruits

                