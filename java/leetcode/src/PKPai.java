import org.junit.jupiter.api.Test;

public class PKPai {
    public int[] pkPai(int[] nums) {
        if(nums.length == 0) return null;


        recursion(nums,nums.length-1);

        return nums;
    }

    void recursion(int[] array,int right){
        //terminator
        if(right==0){
            return;
        }

        //process
        int mid = (right-1)/2;
        //recursion
        recursion(array,mid);

        int[] tmp = new int[right+1];
        int l1=0,l2=mid+1,i=right;
        if((right & 1) == 0){
            tmp[right] = array[l2++];
            --i;
        }

        for (; i >= 0; i=i-2) {
            tmp[i]= array[l1++];
            tmp[i-1]= array[l2++];
        }

        //put into array

        for (int j = 0; j < tmp.length; j++) {
            array[j]=tmp[j];
        }

    }

    @Test
    void test(){
        int[] nums = new int[]{2, 4, 5, 3, 1};
        System.out.println(pkPai(nums));
    }
}
