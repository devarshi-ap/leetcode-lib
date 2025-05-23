class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {} # fruitType -> times Seen
        maxL = 0
        start = 0

        for end in range(len(fruits)):
            fruit = fruits[end]
            basket[fruit] = basket.get(fruit, 0) + 1 # new entry or increment

            while len(basket) > 2:
                basket[fruits[start]] -= 1
                if basket[fruits[start]] == 0:
                    del basket[fruits[start]]
                start += 1
            
            maxL = max(maxL, end - start + 1)
        return maxL