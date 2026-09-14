class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        
        while top <= bottom and left <= right: # while there is space to move
            # Traverse top row (l->r)
            for col in range(left, right+1):
                res.append(matrix[top][col])
            top += 1 # shift TOP down

            # Traverse right column (tâb)
            for row in range(top, bottom+1):
                res.append(matrix[row][right])
            right -= 1 # shift RIGHT in

            # Traverse bottom row (l<-r) (if rows remain)
            if top <= bottom:
                for col in range(right, left-1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1 # shift BOTTOM up

            # Traverse left column (bât) (if columns remain)
            if left <= right:
                for row in range(bottom, top-1, -1):
                    res.append(matrix[row][left])
                left += 1 # shift LEFT in
            
        return res
            
