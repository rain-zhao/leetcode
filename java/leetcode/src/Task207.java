import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Task207 {
    //bfs
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] inCnt = new int[numCourses];
        List<Integer>[] adjList =  new List[numCourses];
        for (int i = 0; i < adjList.length; i++) {
            adjList[i] = new ArrayList<>();
        }
        for (int[] prerequisite : prerequisites) {
            ++inCnt[prerequisite[0]];
            adjList[prerequisite[1]].add(prerequisite[0]);
        }

        int cnt = 0;
        Queue<Integer> queue = new LinkedList<>();

        for (int i = 0; i < inCnt.length; i++) {
            if(inCnt[i] == 0){
                queue.offer(i);
            }
        }

        while (!queue.isEmpty()){
            Integer cur = queue.poll();
            ++cnt;
            adjList[cur].forEach(val->{
                --inCnt[val];
                if(inCnt[val] == 0){
                    queue.offer(val);
                }
            });

        }

        return cnt == numCourses;
    }

    //dfs
    enum Color {
        WHITE,
        GRAY,
        BLACK;
    }
    public boolean canFinish2(int numCourses, int[][] prerequisites) {
        List<Integer>[] adjList = new ArrayList[numCourses];
        Color[] colors = new Color[numCourses];
        for (int i = 0; i < numCourses; i++) {
            adjList[i] = new ArrayList<>();
            colors[i] = Color.WHITE;
        }
        for (int[] prerequisite : prerequisites) {
            adjList[prerequisite[0]].add(prerequisite[1]);
        }


        for (int i = 0; i < numCourses; i++) {
            if (!dfs(adjList, i, colors)) {
                return false;
            }
        }

        return true;

    }

    private boolean dfs(List<Integer>[] adjList, int val, Color[] colors) {
        //terminator
        if (colors[val] == Color.GRAY) {
            return false;
        }
        if (colors[val] == Color.BLACK) {
            return true;
        }
        //process
        //change color into gray
        colors[val] = Color.GRAY;

        //drill down
        for (Integer integer : adjList[val]) {
            if (!dfs(adjList, integer, colors)) {
                return false;
            }
        }
        colors[val] = Color.BLACK;

        return true;
    }

}
