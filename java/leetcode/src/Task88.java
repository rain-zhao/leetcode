import org.junit.jupiter.api.Test;

public class Task88 {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int cur1 =0,cur2=0;

        while(cur1 < m+cur2 && cur2 < n){
            if(nums1[cur1] <= nums2[cur2]){
                ++cur1;
            }else{
                for (int i = m+cur2; i >cur1; --i) {
                    nums1[i] = nums1[i-1];
                }
                nums1[cur1] = nums2[cur2];

                ++cur1;
                ++cur2;
            }
        }

        while(cur2 < n){
            nums1[cur1] = nums2[cur2];
            ++cur1;
            ++cur2;
        }
    }

    @Test
    void test(){
        int[] nums1 = new int[]{1,2,3,0,0,0};
        int m = 3;
        int[] nums2 = new int[]{2,5,6};
        int n = 3;
        merge(nums1,m,nums2,n);
        System.out.println(nums1);
    }
}
