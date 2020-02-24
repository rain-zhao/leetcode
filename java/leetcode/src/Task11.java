import org.junit.jupiter.api.Test;

public class Task11 {
    //brute force
    public int maxArea(int[] height) {

        if(height.length < 2){
            return 0;
        }

        int length = height.length;
        int res=0;

        for (int i = 0; i < length-1; i++) {
            for (int j = i+1; j < length; j++) {
                int product = Math.min(height[i],height[j]) * (j-i);
                res = Math.max(res,product);
            }
        }

        return res;
    }

    //double cursor
    public int maxArea2(int[] height) {

        if(height.length < 2){
            return 0;
        }

        int length = height.length;
        int res = 0;

        int left = 0,right = length-1;

        while(left < right){
            int product = Math.min(height[left],height[right]) * (right-left);
            res = Math.max(res,product);
            if(height[left] > height[right]){
                --right;
            }else{
                ++left;
            }
        }

        return res;
    }


    @Test
    void test(){
        int[] height = new int[]{1,8,6,2,5,4,8,3,7};
        System.out.println(maxArea2(height));
    }
}
