class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # monotonic stack = stack that's strictly increasing OR decreasing order
        finalPrices = [x for x in prices] # don't = prices (both vars will point to same list)
        stack = [] # indices, values in increasing order (monotonic increasing stack)

        for i, p in enumerate(prices):
            # if stack not empty and current p can apply discounts to stack (p > prev_p in stack)
            print(i, p)
            print(stack)
            while stack and (p <= prices[stack[-1]]):
                print(">",stack)
                # apply discount to popped item
                prev_i = stack.pop()
                print("->", finalPrices, prev_i)
                finalPrices[prev_i] -= p
            stack.append(i)
        
        return finalPrices