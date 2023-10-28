class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        reversed_str = str(x)
        if x < 0:
            reversed_str = reversed_str[0] + reversed_str[:0:-1]
        else:
            reversed_str = reversed_str[::-1]
        
        reversed_int = int(reversed_str)
        
        # Handle overflow (32-bit signed integer range)
        if reversed_int < INT_MIN or reversed_int > INT_MAX:
            return 0
        
        return reversed_int
