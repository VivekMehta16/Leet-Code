class Solution(object):
    def isPalindrome(self, x):
        # Negative numbers and numbers ending in 0 (except 0 itself) can't be palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        # Reverse the second half of the number
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # A number is a palindrome if the first half is equal to the second half
        return x == reversed_half or x == reversed_half // 10