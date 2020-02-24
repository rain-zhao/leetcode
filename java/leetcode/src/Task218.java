import org.junit.jupiter.api.Test;

import java.util.*;

public class Task218 {
    public List<List<Integer>> getSkyline(int[][] buildings) {
        if (buildings.length == 0 || buildings[0].length == 0) {
            return Collections.emptyList();
        }

        int len = buildings.length;
        //pre process
        int[][] queue = new int[len * 2][2];

        for (int i = 0; i < len; i++) {
            int[] building = buildings[i];
            queue[i][0] = building[0];
            queue[i][1] = -building[2];
            queue[i + len][0] = building[1];
            queue[i + len][1] = building[2];
        }

        Arrays.sort(queue, (a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);

        List<List<Integer>> res = new ArrayList<>();

        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);
        pq.offer(0);

        int cur = 0;

        for (int i = 0; i < queue.length; i++) {
            int[] pair = queue[i];
            if (pair[1] < 0) {
                pq.offer(-pair[1]);
            } else {
                pq.remove(pair[1]);
            }
            if (cur != pq.peek()) {
                cur = pq.peek();
                res.add(Arrays.asList(pair[0], cur));
            }

        }

        return res;
    }

    @Test
    void test() {
        int[][] buildings = new int[][]{
                {2, 9, 10},
                {3, 7, 15},
                {5, 12, 12},
                {15, 20, 10},
                {19, 24, 8}
        };
        System.out.println(getSkyline(buildings));
    }
}
