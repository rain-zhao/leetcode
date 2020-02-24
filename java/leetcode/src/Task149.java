import org.junit.jupiter.api.Test;

public class Task149 {
//    public int maxPoints(int[][] points) {
//        if (points.length < 3) {
//            return points.length;
//        }
//
//        int l = points.length;
//        Map<String, Integer> map = new HashMap<>();
//        int res = 2;
//        //loop
//        for (int i = 0; i < l - 1; i++) {
//            int[] a = points[i];
//            for (int j = i; j < l; j++) {
//                int[] b = points[j];
//                if (a[0] == b[0]) {
//                    String key = "-" + a[0];
//                    map.compute(key, (k, v) -> v == null ? 1 : v + 1);
//                }else{
//
//                }
//
//
//            }
//
//        }
//
//        return res;
//    }
//
//    private int gcd(int dy, int dx) {
//        if (dx == 0) return dy;
//        else return gcd(dx, dy % dx);
//    }

    public int maxPoints(int[][] points) {
        if (points.length < 3) {
            return points.length;
        }

        int l = points.length;
        int res = 2;
        //loop
        for (int i = 0; i < l - res; i++) {
            int[] a = points[i];
            int same = 1;
            for (int j = i + 1; j < l - 1; j++) {
                int[] b = points[j];
                int cnt = 1;
                if (a[0] == b[0] && a[1] == b[1]) {
                    ++same;
                } else {
                    for (int k = j + 1; k < l; k++) {
                        int[] c = points[k];
                        if ((long) (a[1] - b[1]) * (c[0] - a[0]) == (long) (a[0] - b[0]) * (c[1] - a[1])) {
                            ++cnt;
                        }
                    }
                }

                res = Math.max(res, cnt + same);
            }
        }

        return res;
    }

    @Test
    void test() {
        int[][] points = new int[][]{{1, 1}, {1, 1}, {1, 1}};
        System.out.println(maxPoints(points));
    }
}
