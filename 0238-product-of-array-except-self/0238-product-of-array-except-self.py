class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [1] * n

        # Build prefix in result array
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # Multiply with postfix on the fly
        postfix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result