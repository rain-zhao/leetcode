import org.junit.jupiter.api.Test;

import java.util.HashSet;
import java.util.Set;

public class LCP3 {
    public boolean robot(String command, int[][] obstacles, int x, int y) {
        if (x == 0 && y == 0) {
            return true;
        }
        Set<Long> set = new HashSet<>(obstacles.length);
        for (int[] obstacle : obstacles) {
            set.add((long) obstacle[0] << 32 | obstacle[1]);
        }

        int cx = 0, cy = 0;
        while (true) {
            for (char c : command.toCharArray()) {
                if (c == 'U') {
                    ++cy;
                } else {
                    ++cx;
                }
                if (set.contains((long) cx << 32 | cy)) {
                    return false;
                } else if (cx > x || cy > y) {
                    return false;
                } else if (cx == x && cy == y) {
                    return true;
                }

            }
        }

    }

    public boolean robot2(String command, int[][] obstacles, int x, int y) {
        if (x == 0 && y == 0) {
            return true;
        }
        Set<Long> set = new HashSet<>(obstacles.length);
        set.add(0l);
        int cx = 0, cy = 0;
        for (char c : command.toCharArray()) {
            if (c == 'U') {
                ++cy;
            } else {
                ++cx;
            }
            set.add((long) cx << 32 | cy);
        }

        //dest in the path
        int circle = Math.min(x/cx,y/cy);
        if(!set.contains((long)(x-circle*cx) << 32 | (y-circle*cy))){
            return false;
        }

        // obstacles
        for (int[] obstacle : obstacles) {
            if(obstacle[0] > x || obstacle[1] > y) continue;
            circle = Math.min(obstacle[0]/cx,obstacle[1]/cy);
            if(set.contains((long)(obstacle[0]-circle*cx) << 32 | (obstacle[1]-circle*cy))){
                return false;
            }
        }

        return true;
    }

    @Test
    void test() {
//        String command = "RRU";
//        int[][] obstacles = new int[][]{
//                {5, 5},
//                {9, 4},
//                {9, 7},
//                {6, 4},
//                {7, 0},
//                {9, 5},
//                {10, 7},
//                {1, 1},
//                {7, 5}
//        };
//        int x = 1486;
//        int y = 743;
        String command = "URRURRR";
        int[][] obstacles = new int[0][0];
        int x = 4915;
        int y = 1966;
        System.out.println(robot2(command, obstacles, x, y));

    }
}
