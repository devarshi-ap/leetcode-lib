class Solution:
    def reverse(self, x: int) -> int:
        sign = "+" if x >= 0 else "-"
        rev_abs = str(abs(x))[::-1]
        built_num = int(sign + rev_abs)
        
        if -2**31 <= built_num <= 2**31 - 1:
            return built_num
        else:
            return 0