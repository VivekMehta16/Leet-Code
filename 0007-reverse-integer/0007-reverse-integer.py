class Solution(object):
    def reverse(self, x):
        ReverseNumber = 0
        sign = -1 if x < 0 else 1
        x = abs(x)  # Work with absolute value
        
        while x > 0:
            LastDigit = x % 10
            x = x // 10
            ReverseNumber = (ReverseNumber * 10) + LastDigit
        
        ReverseNumber *= sign  # Restore original sign
        
        # Handling 32-bit integer overflow case
        if ReverseNumber < -2**31 or ReverseNumber > 2**31 - 1:
            return 0
        
        return ReverseNumber
