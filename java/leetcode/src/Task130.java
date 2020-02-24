import org.junit.jupiter.api.Test;

import java.util.HashSet;

public class Task130 {
    int[] dx = new int[]{-1, 1, 0, 0};
    int[] dy = new int[]{0, 0, -1, 1};

    public void solve(char[][] board) {
        if (board.length == 0 || board[0].length == 0) {
            return;
        }

        int m = board.length;
        int n = board[0].length;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if(board[i][j] == 'O'){
                    HashSet<Integer> visited = new HashSet<Integer>();
                    if(valid(board, i, j, visited)){
                        visited.forEach(val->{
                            int x = val/n;
                            int y = val%n;
                            board[x][y]='X';
                        });
                    }

                }
            }
        }
    }

    private boolean valid(char[][] board, int i, int j, HashSet<Integer> visited) {
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length) {
            return false;
        }

        if (board[i][j] == 'X'||visited.contains(i*board[0].length+j)) {
            return true;
        }

        visited.add(i*board[0].length+j);

        for (int k = 0; k < 4; k++) {
            if(!valid(board,i+dx[k],j+dy[k],visited)){
                return false;
            }
        }

//        board[i][j] = 'X';
        return true;

    }


    public void solve2(char[][] board) {
        if (board.length == 0 || board[0].length == 0) {
            return;
        }

        int m = board.length;
        int n = board[0].length;

        for (int i = 0; i < n; i++) {
            color(board,0,i);
            color(board,m-1,i);
        }

        for (int i = 1; i < m-1; i++) {
            color(board,i,0);
            color(board,i,n-1);
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if(board[i][j] == '#'){
                    board[i][j] = 'O';
                }else if(board[i][j] == 'O'){
                    board[i][j] = 'X';
                }
            }
        }

    }


    private void color(char[][] board, int i, int j) {
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length || board[i][j] != 'O') {
            return;
        }
        board[i][j] = '#';

        for (int k = 0; k < 4; k++) {
            color(board,i+dx[k],j+dy[k]);
        }
    }

    @Test
    void test(){
        char[][] board = new char[][]{
                {'X','O','X','X'},
                {'O','X','O','X'},
                {'X','O','X','O'},
                {'O','X','O','X'},
                {'X','O','X','O'},
                {'O','X','O','X'}
        };
        solve2(board);
    }
}
