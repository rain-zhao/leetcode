import org.junit.jupiter.api.Test;

import java.util.Comparator;
import java.util.PriorityQueue;

public class Task378 {
    //merge
    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;

        PriorityQueue<Integer> pq = new PriorityQueue<>(n, Comparator.comparingInt(a -> matrix[a / n][a % n]));

        for (int i = 0; i < n; i++) {
            pq.offer(i * n);
        }

        while (k > 1) {
            int pos = pq.poll();
            if (pos % n != n - 1) {
                pq.offer(++pos);
            }

            --k;
        }

        return matrix[pq.peek() / n][pq.peek() % n];

    }

    int n;

    public int kthSmallest2(int[][] matrix, int k) {

        n = matrix.length;

        int left = matrix[0][0];
        int right = matrix[n - 1][n - 1];

        while (left <= right) {
            int mid = left + (right - left) / 2;

            int cnt = countlte(matrix, mid);
            if (cnt < k) {
                left = mid+1;
            } else {
                right = mid;
            }
        }

        return right;
    }

    private int countlte(int[][] matrix, int mid) {
        int i = n - 1;
        int j = 0;
        int cnt = 0;
        while (i >= 0 && j < n) {
            if (matrix[i][j] <= mid) {
                cnt +=i+1;
                ++j;
            } else {
                --i;
            }
        }
        return cnt;
    }

    @Test
    void test() {
        int[][] matrix = new int[][]{
                {1, 5, 9},
                {10, 11, 13},
                {12, 13, 15}
        };
        int k = 8;
        System.out.println(kthSmallest2(matrix, 8));
    }
}
