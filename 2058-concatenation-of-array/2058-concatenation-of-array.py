class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # creates new list
        # return nums + nums

        # modifies existing list (more efficient)
        nums.extend(nums)
        return nums