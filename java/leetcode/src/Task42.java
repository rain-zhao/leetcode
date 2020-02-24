import org.junit.jupiter.api.Test;

public class Task42 {
    public int trap(int[] height) {
        if (height.length < 2) {
            return 0;
        }

        int res = 0;

        int left = 0, right = height.length - 1;
        int cur = -1;
        while (left < right - 1) {

            if (height[left] <= height[right]) {
                cur = left + 1;
                while (height[cur] < height[left]) {
                    res += height[left] - height[cur++];
                }
                left = cur;
            } else {
                cur = right - 1;
                while (height[cur] < height[right]) {
                    res += height[right] - height[cur--];
                }
                right = cur;
            }

        }

        return res;
    }

    public int trap2(int[] height) {
        if (height.length < 2) {
            return 0;
        }

        int res = 0;

        int l = height.length;
        int[] max_left = new int[l];
        int[] max_right = new int[l];

        for (int i = 1; i < l; i++) {
            max_left[i] = Math.max(height[i], max_left[i - 1]);
        }

        for (int i = l - 2; i >= 0; i--) {
            max_right[i] = Math.max(height[i], max_right[i + 1]);
        }

        for (int i = 1; i < height.length - 1; i++) {
            res += Math.min(max_left[i], max_right[i]) - height[i];
        }

        return res;
    }

    public int trap3(int[] height) {
        if (height.length < 2) {
            return 0;
        }

        int res = 0;

        int left = 0, right = height.length - 1;
        int leftMax = 0, rightMax = 0;


        while(left < right){
            if(height[left] <= height[right]){
                if(height[left] > leftMax){
                    leftMax = height[left];
                }else{
                    res += leftMax - height[left];
                }
                ++left;
            }else{
                if(height[right] > rightMax){
                    rightMax = height[right];
                }else{
                    res += rightMax - height[right];
                }

                --right;
            }
        }


        return res;
    }


    @Test
    void test() {
        int[] height = new int[]{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
        System.out.println(trap3(height));
    }
}
