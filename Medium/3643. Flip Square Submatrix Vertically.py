class Solution:
    def reverseSubmatrix(self, grid, r, c, k):
        # flip vertically inside k x k square
        for i in range(k // 2):
            for j in range(k):
                grid[r + i][c + j], grid[r + k - 1 - i][c + j] = \
                grid[r + k - 1 - i][c + j], grid[r + i][c + j]
        
        return grid
