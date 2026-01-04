class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r: # haven't overlapped yet
            currSum = numbers[l] + numbers[r]
            print(currSum)
            if currSum > target: # too hi = <-R
                r -= 1
            elif currSum < target: # too lo = L->
                l += 1
            else:
                return [l+1, r+1]
        