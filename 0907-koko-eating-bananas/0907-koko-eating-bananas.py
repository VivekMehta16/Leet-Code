class Solution(object):
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += int(math.ceil(float(p) / k))

            if hours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1

        return res
