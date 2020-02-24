import org.junit.jupiter.api.Test;

public class Task4 {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] a, b;
        if (nums1.length > nums2.length) {
            a = nums2;
            b = nums1;
        } else {
            a = nums1;
            b = nums2;
        }

        int m = a.length;
        int n = b.length;
        int helf = (m + n + 1) / 2;


        int left = 0, right = m;
        while (left <= right) {
            int i = left + (right - left) / 2;
            int j = helf - i;
            if (i > 0 && a[i - 1] > b[j]) {
                right = i - 1;
            } else if (i < m && b[j - 1] > a[i]) {
                left = i + 1;
            } else {
                int maxLeft;
                maxLeft = i == 0 ? b[j - 1] : j == 0 ? a[i-1] : Math.max(a[i-1], b[j - 1]);

                if (((m + n) & 1) == 1) {
                    return maxLeft;
                }

                int minRight;
                minRight = i == m ? b[j] : j == n ? a[i] : Math.min(a[i], b[j]);

                return (minRight+maxLeft)/2.0;

            }
        }

        return 0.0;
    }

    @Test
    void test(){
        int[] nums1 = new int[]{1, 3};
        int[] nums2 = new int[]{2};
        System.out.println(findMedianSortedArrays(nums1,nums2));
    }


}
