import org.junit.jupiter.api.Test;

import java.util.*;

public class Task210 {
    //bfs
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int[] inCnt = new int[numCourses];
        List<Integer>[] adjList = new List[numCourses];
        for (int i = 0; i < adjList.length; i++) {
            adjList[i] = new ArrayList<>();
        }
        for (int[] prerequisite : prerequisites) {
            ++inCnt[prerequisite[0]];
            adjList[prerequisite[1]].add(prerequisite[0]);
        }

        int[] res = new int[numCourses];
        int idx = 0;
        Queue<Integer> queue = new LinkedList<>();

        for (int i = 0; i < inCnt.length; i++) {
            if (inCnt[i] == 0) {
                queue.offer(i);
            }
        }

        while (!queue.isEmpty()) {
            Integer cur = queue.poll();
            res[idx++] = cur;
            adjList[cur].forEach(val -> {
                --inCnt[val];
                if (inCnt[val] == 0) {
                    queue.offer(val);
                }
            });

        }

        if (idx != numCourses) {
            return new int[0];
        }

        return res;

    }

    //dfs
    enum Color {
        WHITE,
        GRAY,
        BLACK;
    }

    public int[] findOrder2(int numCourses, int[][] prerequisites) {
        List<Integer>[] adjList = new ArrayList[numCourses];
        Color[] colors = new Color[numCourses];
        for (int i = 0; i < numCourses; i++) {
            adjList[i] = new ArrayList<>();
            colors[i] = Color.WHITE;
        }
        for (int[] prerequisite : prerequisites) {
            adjList[prerequisite[0]].add(prerequisite[1]);
        }

        List<Integer> res = new ArrayList<>(numCourses);

        for (int i = 0; i < numCourses; i++) {
            if (!dfs(adjList, i, colors, res)) {
                return new int[0];
            }
        }

        return res.stream().mapToInt(val -> val).toArray();

    }

    private boolean dfs(List<Integer>[] adjList, int val, Color[] colors, List<Integer> res) {
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
            if (!dfs(adjList, integer, colors, res)) {
                return false;
            }
        }
        colors[val] = Color.BLACK;
        res.add(val);


        return true;
    }

    @Test
    void test() {
        int[][] prerequisites = new int[][]{{1, 0}, {2, 0}, {3, 1}, {3, 2}};
        int numCourses = 4;
        System.out.println(findOrder2(numCourses, prerequisites));
    }
}
