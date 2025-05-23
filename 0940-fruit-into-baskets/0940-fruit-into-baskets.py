class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {} # fruitType -> times Seen
        maxL = 0
        start = 0

        for end in range(len(fruits)):
            fruit = fruits[end]
            basket[fruit] = basket.get(fruit, 0) + 1 # new entry or increment

            while len(basket) > 2:
                leftFruit = fruits[start]
                basket[leftFruit] -= 1
                if basket[leftFruit] == 0:
                    del basket[leftFruit]
                start += 1
            
            maxL = max(maxL, end - start + 1)
        return maxL