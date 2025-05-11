class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        pre = [1] * n
        post = [1] * n
        res = [0] * n

        for i in range(1,n):
            pre[i] = pre[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            post[i] = post[i+1] * nums[i+1]

        for i in range(n):
            res[i] = pre[i] * post[i]

        return res