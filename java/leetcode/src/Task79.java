import org.junit.jupiter.api.Test;

public class Task79 {

    int lx=0;
    int ly=0;

    public boolean exist(char[][] board, String word) {

        lx= board.length;
        ly= board[0].length;
        for (int i = 0; i < lx; i++) {
            for (int j = 0; j < ly; j++) {
                if(dfs(board,word,0,i,j)){
                    return true;
                }
            }
        }
        return false;
    }

    boolean dfs(char[][] board, String word,int idx,int x,int y){
        if(x < 0 || x > lx-1||y<0 || y> ly-1){
            return false;
        }

        char c = board[x][y];

        if(c != word.charAt(idx)){
            return false;
        }

        if(idx ==word.length()-1){
            return true;
        }

        board[x][y]='#';
        if(dfs(board,word,idx+1,x-1,y)
                ||dfs(board,word,idx+1,x+1,y)
                ||dfs(board,word,idx+1,x,y-1)
                || dfs(board,word,idx+1,x,y+1)){
            return true;
        }
        board[x][y]='c';
        return false;
    }

    @Test
    void test(){
        char[][] board ={{'a','b'}};
        String word = "ba";

        System.out.println(exist(board,word));
    }
}
