import org.junit.jupiter.api.Test;

public class Task287 {
    public int findDuplicate(int[] nums) {
        if(nums.length == 2){
            return nums[0];
        }

        boolean[] visited = new boolean[nums.length];
        for (int i = 0; i < nums.length; i++) {
            if(visited[nums[i]]){
                return nums[i];
            }
            visited[nums[i]] = true;
        }

        return nums[0];
    }

    public int findDuplicate2(int[] nums) {
        if(nums.length == 2){
            return nums[0];
        }

        //phase 1,find intersect
        int fast = nums[0],slow = nums[0];
        do{
            slow = nums[slow];
            fast = nums[nums[fast]];
        }while(fast != slow);

        //phase 2,find loop start
        slow = nums[0];
        while(slow != fast){
            slow = nums[slow];
            fast = nums[fast];
        }

        return slow;
    }

    @Test
    void test(){
        int[] nums = new int[]{1,3,4,2,2};
        System.out.println(findDuplicate2(nums));
    }
}
