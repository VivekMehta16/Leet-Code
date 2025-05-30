class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        Rows, cols = len(matrix), len(matrix[0])

        top, bot = 0, Rows-1
        while top<=bot:
            row=(top+bot) //2
            if target>matrix[row][-1]:
                top = row +1
            elif target < matrix[row][0]:
                bot = row -1
            else:
                break

        if not (top<=bot):
            return False
        row = (top + bot) //2
        l,r = 0, cols-1
        while l<=r:
            m = (l+r) //2
            if target > matrix[row][m]:
                l = m+1
            elif target < matrix[row][m]:
                r = m-1
            else:
                return True
        return False