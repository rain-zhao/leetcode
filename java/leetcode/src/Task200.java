import org.junit.jupiter.api.Test;

public class Task200 {
    //1 flood fill
/*    public int numIslands(char[][] grid) {
        int res = 0;

        for (int i = 0; i < grid.length ; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if(grid[i][j] =='1'){
                    ++res;
                    fill(grid,i,j);
                }
            }
        }

        return res;
    }

    void fill(char[][] grid,int x,int y){
        grid[x][y] = '0';
        if(x !=0 && grid[x-1][y] == '1'){//up
            fill(grid,x-1,y);
        }
        if(x != grid.length-1 && grid[x+1][y] == '1'){//down
            fill(grid,x+1,y);
        }
        if(y != grid[x].length-1 && grid[x][y+1] == '1'){//right
            fill(grid,x,y+1);
        }
        if(y != 0 && grid[x][y-1] == '1'){//left
            fill(grid,x,y-1);
        }
    }*/

//##########################################################

    //union find
    public int numIslands(char[][] grid) {

        if(grid.length ==0){
            return 0;
        }
        int m = grid.length;
        int n = grid[0].length;
        int res = 0;
        QuickUnionUF unionfind = new QuickUnionUF(m*n);

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int p = i*n+j;
                if(grid[i][j] == '1'){
                    ++res;
                    //connect right's '1'
                    if(j != grid[i].length-1 && grid[i][j+1] == '1'){
                        int p2 = p+1;
                        if(!unionfind.connected(p,p2)){
                            unionfind.union(p,p2);
                            --res;
                        }
                    }
                    //connect down's '1'
                    if(i != grid.length-1 && grid[i+1][j] == '1'){
                        int p2 = p+n;
                        if(!unionfind.connected(p,p2)){
                            unionfind.union(p,p2);
                            --res;
                        }
                    }

                }
            }
        }

        return res;
    }



    @Test
    void test(){
        char[][]grid = new char[][]{{'1','1','1'},{'0','1','0'},{'1','1','1'}};
        System.out.println(numIslands(grid));
    }
}
