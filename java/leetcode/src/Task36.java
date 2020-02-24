import org.junit.jupiter.api.Test;

public class Task36 {


    public boolean isValidSudoku(char[][] board) {

        int[] rows = new int[9];
        int[] cols = new int[9];
        int[] blks = new int[9];

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    continue;
                }
                int bit = 1 << board[i][j] - '0';
                if ((bit & (rows[i] | cols[j] | blks[getBlock(i, j)])) == bit) {
                    return false;
                }

                rows[i] |= bit;
                cols[j] |= bit;
                blks[getBlock(i, j)] |= bit;

            }
        }

        return true;
    }


    int getBlock(int i, int j) {
        return i / 3 * 3 + j / 3;
    }

    @Test
    void test() {
        char[][] board = new char[][]{{'.', '8', '7', '6', '5', '4', '3', '2', '1'}, {'2', '2', '.', '.', '.', '.', '.', '.', '.'}, {'3', '.', '.', '.', '.', '.', '.', '.', '.'}, {'4', '.', '.', '.', '.', '.', '.', '.', '.'}, {'5', '.', '.', '.', '.', '.', '.', '.', '.'}, {'6', '.', '.', '.', '.', '.', '.', '.', '.'}, {'7', '.', '.', '.', '.', '.', '.', '.', '.'}, {'8', '.', '.', '.', '.', '.', '.', '.', '.'}, {'9', '.', '.', '.', '.', '.', '.', '.', '.'}};
        System.out.println(isValidSudoku(board));
    }

}
