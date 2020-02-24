import org.junit.jupiter.api.Test;

import java.util.Stack;

public class Task84 {


    public int largestRectangleArea(int[] heights) {
        if (heights.length == 0) {
            return 0;
        }
        if (heights.length == 1) {
            return heights[0];
        }

        int res = 0;

        for (int i = 0; i < heights.length; i++) {

            int minHeight = Integer.MAX_VALUE;

            for (int j = i; j >= 0; j--) {
                minHeight = Math.min(minHeight, heights[j]);
                res = Math.max(res, (i - j + 1) * minHeight);
            }
        }

        return res;
    }

    public int largestRectangleArea2(int[] heights) {
        if (heights.length == 0) {
            return 0;
        }
        if (heights.length == 1) {
            return heights[0];
        }

        return calculate(heights, 0, heights.length - 1);
    }

    private int calculate(int[] heights, int beg, int end) {
        if(beg > end){
            return 0;
        }

        int minIdx = beg;
        for (int i = beg + 1; i <= end; i++) {
            minIdx = heights[minIdx] < heights[i] ? minIdx : i;
        }
        int area = (end-beg+1)* heights[minIdx];

        area = Math.max(area,calculate(heights,beg,minIdx-1));//left
        area = Math.max(area,calculate(heights,minIdx+1,end));//right


        return area;
    }

    public int largestRectangleArea3(int[] heights) {
        if (heights.length == 0) {
            return 0;
        }
        if (heights.length == 1) {
            return heights[0];
        }

        int res = 0;

        Stack<Integer> stack = new Stack<>();

        stack.push(-1);

        for (int i = 0; i < heights.length; i++) {

            while(stack.peek() != -1 && heights[i] < heights[stack.peek()]){
                res = Math.max(res,heights[stack.pop()]*(i-stack.peek()-1));
            }
            stack.push(i);

        }

        while(stack.peek() != -1){
            res = Math.max(res,heights[stack.pop()]*(heights.length-stack.peek()-1));
        }

        return res;
    }


    @Test
    void test() {
        int[] heights = new int[]{2,1,2};
        System.out.println(largestRectangleArea3(heights));
    }

}
