import java.util.PriorityQueue;

public class Task215 {
    //堆实现
    public int findKthLargest(int[] nums, int k) {

        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for(int num:nums){
            if(pq.size() < k){
                pq.offer(num);
            }else if(num > pq.peek()){
                pq.poll();
                pq.offer(num);
            }
        }

        return pq.peek();

    }
    //快递查找实现
    public static int findKthLargest2(int[] nums, int k) {
        int i=0,j=nums.length-1;

        int target = nums.length - k;

        int pivot = quickSelect2(nums,i,j);

        while(pivot != target){
            if(pivot > target){
                j= pivot-1;
                pivot = quickSelect2(nums,i,j);
            }else{
                i=pivot+1;
                pivot = quickSelect2(nums,i,j);
            }
        }

        return nums[pivot];



    }

    /**
     *
     * @param nums
     * @param i
     * @param j
     * @return return the pivot index
     */
    public static int quickSelect(int[] nums,int i,int j){
        while(i < j){
            int pivot = nums[i];
            while(pivot < nums[j]){
                --j;
            }
            swap(nums,i,j);

            pivot = nums[j];
            ++i;
            while(nums[i] <= pivot && i != nums.length-1){
                ++i;
            }
            swap(nums,i,j);
        }
        swap(nums,i,j);

        return j;
    }

    public static int quickSelect2(int[] nums,int i,int j){
        int pivotIndex = i;
        for(;i<j;++i){
            if(nums[i] < nums[j]){
                swap(nums,i,pivotIndex++);
            }
        }
        swap(nums,pivotIndex,j);

        return pivotIndex;
    }

    private static void swap(int[] nums,int i,int j){
        if(i==j){
            return;
        }
        nums[i] = nums[i]^nums[j];
        nums[j] = nums[i]^nums[j];
        nums[i] = nums[i]^nums[j];
    }

    public static void main(String[] args) {
        int[] nums = new int[]{3,2,3,1,2,4,5,5,6};
        int k = 4;
        System.out.println(findKthLargest2(nums,k));
    }
}
