class Solution {
    public static boolean isValidSudoku(char[][] board) {
        return (rowsAreValid(board) && colsAreValid(board) && boxesAreValid(board)) ? true : false;
    }
    
    public static boolean rowsAreValid(char[][] board) {
        for (char[] row: board) {
            int[] checklist = {1, 2, 3, 4, 5, 6, 7, 8, 9};
            for (char charDig : row) {
                if (charDig != '.') {
                    int numDig = Integer.parseInt(String.valueOf(charDig));  
                    if (checklist[numDig - 1] == 0) // numDig repeats if already checked off to 0
                        return false;
                    else
                        checklist[numDig - 1] = 0; // check numDig in checklist off to 0
                }
            }
        }
        return true;
    }

    public static boolean colsAreValid(char[][] board) {
        return rowsAreValid(transposeMatrix(board));
    }

    public static boolean boxesAreValid(char[][] board) {
        //check each 3*3 matrix
        for (int block = 0; block < 9; block++) {
            boolean[] m = new boolean[9];
            for (int i = block / 3 * 3; i < block / 3 * 3 + 3; i++) {
                for (int j = block % 3 * 3; j < block % 3 * 3 + 3; j++) {
                    if (board[i][j] != '.') {
                        if (m[(int) (board[i][j] - '1')]) {
                            return false;
                        }
                        m[(int) (board[i][j] - '1')] = true;
                    }
                }
            }
        }
        return true;
    }

    public static char[][] transposeMatrix(char[][] board){
        int m = board.length; // #rows
        int n = board[0].length; // #cols
        char[][] transposedMatrix = new char[n][m];
        for(int x = 0; x < n; x++)
            for(int y = 0; y < m; y++)
                transposedMatrix[x][y] = board[y][x];
        return transposedMatrix;
    }
}