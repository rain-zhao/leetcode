import org.junit.jupiter.api.Test;

public class Task108 {
    public TreeNode sortedArrayToBST(int[] nums) {
        if(nums.length == 0){
            return null;
        }
        return sortedArrayToBST(nums,0,nums.length-1);
    }

    private TreeNode sortedArrayToBST(int[] nums, int left, int right) {
        if(left > right){
            return null;
        }
        int mid = left + (right-left)/2;

        TreeNode root = new TreeNode(nums[mid]);
        root.left = sortedArrayToBST(nums,left,mid-1);
        root.right = sortedArrayToBST(nums,mid+1,right);

        return root;
    }

    @Test
    void test(){
        int[] nums = new int[]{-10,-3,0,5,9};
        TreeNode root = sortedArrayToBST(nums);
        System.out.println(root);
    }
}
