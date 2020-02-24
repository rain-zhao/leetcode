import org.junit.jupiter.api.Test;

import java.util.Comparator;
import java.util.PriorityQueue;

public class Task407 {
    class Node{
        int x;
        int y;
        int val;
        public Node(int x, int y, int val) {
            this.x = x;
            this.y = y;
            this.val = val;
        }
    }
    int[][] direct = new int[][]{{-1,0},{1,0},{0,-1},{0,1}};
    public int trapRainWater(int[][] heightMap) {
        if (heightMap.length < 3 || heightMap[0].length < 3) {
            return 0;
        }

        int m = heightMap.length;
        int n = heightMap[0].length;

        int res =0;

        PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a.val));

        boolean[][] visited = new boolean[m][n];

        //put outer node into pq
        for (int i = 0; i < n; i++) {
           pq.offer(new Node(0,i,heightMap[0][i]));
           visited[0][i]=true;
           pq.offer(new Node(m-1,i,heightMap[m-1][i]));
           visited[m-1][i]=true;
        }
        for (int i = 1; i < m-1; i++) {
            pq.offer(new Node(i,0,heightMap[i][0]));
            visited[i][0]=true;
            pq.offer(new Node(i,n-1,heightMap[i][n-1]));
            visited[i][n-1]=true;
        }

        while(!pq.isEmpty()){
            Node node = pq.poll();

            for (int i = 0; i < direct.length; i++) {
                int x = node.x + direct[i][0];
                int y = node.y + direct[i][1];
                if(x>=0 && x < m && y >=0 && y < n && !visited[x][y]){
                    visited[x][y] = true;
                    int val = heightMap[x][y];
                    if(heightMap[x][y] < node.val){
                        res += node.val-heightMap[x][y];
                        val = node.val;
                    }
                    pq.offer(new Node(x,y,val));
                }
            }

        }


        return res;
    }


    @Test
    void test() {
        int[][] heightMap = new int[][]{{12,13,1,12},{13,4,13,12},{13,8,10,12},{12,13,12,12},{13,13,13,13}};

        int res = trapRainWater(heightMap);

        System.out.println(res);

    }

}
