import org.junit.jupiter.api.Test;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Task37 {

    Map<Integer,Set<Integer>> cols = new HashMap<>();
    Map<Integer,Set<Integer>> rows = new HashMap<>();
    Map<Integer,Set<Integer>> blocks = new HashMap<>();

    public void solveSudoku(char[][] board) {
        //init
        for (int i = 0; i < 9; i++) {
            cols.put(i,new HashSet<>());
            rows.put(i,new HashSet<>());
            blocks.put(i,new HashSet<>());
        }
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if(board[i][j] != '.'){
                    cols.get(j).add(board[i][j]-'0');
                    rows.get(i).add(board[i][j]-'0');
                    blocks.get(getBlock(i,j)).add(board[i][j]-'0');

                }
            }
        }

        dfs(board,0);

    }

    boolean dfs(char[][] board,int idx){
        if(idx == 81){
            return true;
        }
        int i = idx/9;
        int j = idx%9;

        if(board[i][j] != '.'){
            return dfs(board,idx+1);
        }

        for (int num = 1; num < 10; num++) {
            if(!cols.get(j).contains(num) && !rows.get(i).contains(num) && !blocks.get(getBlock(i,j)).contains(num)){

                board[i][j] = (char) (num + '0');

                cols.get(j).add(num);
                rows.get(i).add(num);
                blocks.get(getBlock(i,j)).add(num);

                if(dfs(board,idx+1)){
                    return true;
                }

                //reverse
                cols.get(j).remove(num);
                rows.get(i).remove(num);
                blocks.get(getBlock(i,j)).remove(num);
                board[i][j] = '.';

            }

        }

        return false;
    }

    int getBlock(int i,int j){
        return i/3*3 +j/3;
    }


    void print(char[][] board){
        for (int i = 0; i < board.length ; i++) {
            String row = "[";
            for (int j = 0; j < board[i].length; j++) {
                row += board[i][j]+",";
            }
            row+="]";
            System.out.println(row);
        }
    }


    @Test
    void test(){
        char[][] board = new char[][]{{'.','.','9','7','4','8','.','.','.'},{'7','.','.','.','.','.','.','.','.'},{'.','2','.','1','.','9','.','.','.'},{'.','.','7','.','.','.','2','4','.'},{'.','6','4','.','1','.','5','9','.'},{'.','9','8','.','.','.','3','.','.'},{'.','.','.','8','.','3','.','2','.'},{'.','.','.','.','.','.','.','.','6'},{'.','.','.','2','7','5','9','.','.'}};
        solveSudoku(board);
        print(board);
    }
}
