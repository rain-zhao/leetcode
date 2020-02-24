public class Task26 {
    public int removeDuplicates(int[] nums) {
        if(nums.length < 2){
            return nums.length;
        }

        int cur = 0;
        for (int i = 1; i < nums.length; i++) {
            if(nums[i] != nums[cur]){
                nums[++cur] = nums[i];
            }
        }

        return cur+1;
    }


    void test(){
        int[] nums = new int[]{0,0,1,1,1,2,2,3,3,4};
        int res = removeDuplicates(nums);
        System.out.println(res);
        System.out.println(nums);
    }
}
