class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if matrix == '' or rows <= 0 or cols <= 0 or path == '':
            return False
        #记录路径是否走过
        flag = [0]*len(matrix)
        for i in range(rows):
            for j in range(cols):
                #如果有一个路径满足，则返回True
                if self.finPath(matrix, rows, cols, i, j, path, flag, 0):
                    return True

        del flag
        return False
    def finPath(self, matrix, rows, cols, i, j, path, flag, k):
        index = i * cols + j
        if i < 0 or j < 0 or i >= rows or j >= cols or k > len(path)-1 or path[k] != matrix[index]  or flag[index] == 1:
            return False
        #走到最后一位返回True
        if k == len(path)-1:
            return True
        flag[index] = 1
        #上下左右
        if  self.finPath(matrix, rows, cols, i+1, j,   path, flag, k+1) or \
            self.finPath(matrix, rows, cols, i-1, j,   path, flag, k+1) or \
            self.finPath(matrix, rows, cols, i,   j+1, path, flag, k+1) or \
            self.finPath(matrix, rows, cols, i,   j-1, path, flag, k+1):
            return True
        #出栈重置
        flag[index] = 0
        #完全出栈还没有返回值，说明不存在这条路径
        return False

so = Solution()
matrix = 'ABCESFCSADEE'
matrix = ''.join(matrix)
path = 'ABCB'
path = ''.join(path)
print(so.hasPath(matrix, 3, 4, path))