class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        copy = x
        result = 0 
        while x != 0:
            rem = x%10
            result = result*10 + rem
            x //= 10
        return copy == result
