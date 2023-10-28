class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        reversed_int = 0
        
        while x != 0:
            pop = x % 10
            x //= 10
            
            # Check for overflow before updating the result
            if reversed_int > INT_MAX // 10 or (reversed_int == INT_MAX // 10 and pop > 7):
                return 0
            if reversed_int < INT_MIN // 10 or (reversed_int == INT_MIN // 10 and pop < -8):
                return 0
            
            reversed_int = reversed_int * 10 + pop
        
        return reversed_int
