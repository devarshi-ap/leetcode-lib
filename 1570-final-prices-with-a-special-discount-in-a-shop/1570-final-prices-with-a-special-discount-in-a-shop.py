class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # monotonic stack = stack that's strictly increasing OR decreasing order
        finalPrices = [x for x in prices] # don't = prices (both vars will point to same list)
        stack = [] # indices, values in increasing order (monotonic increasing stack)

        for i, p in enumerate(prices):
            # if stack not empty and current p can apply discounts to stack (current_p <= prev_p in stack)
            while stack and (p <= prices[stack[-1]]):
                # apply discount to popped item
                prev_i = stack.pop()
                finalPrices[prev_i] -= p
            # add current_i to help find discount in next iteration
            stack.append(i)
        
        return finalPrices

        # WATCH: https://www.youtube.com/watch?v=3_BAIugNaLw