import org.junit.jupiter.api.Test;

import java.util.Arrays;

public class Task324 {
    public void wiggleSort(int[] nums) {
        if (nums.length < 2) {
            return;
        }
        int[] tmp = nums.clone();
        Arrays.sort(tmp);
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            nums[(2 * i + 1) % (n | 1)] = tmp[n - 1 - i];
        }

    }

    public void wiggleSort2(int[] nums) {
        if (nums.length < 2) {
            return;
        }
        int n = nums.length;
        int k = n / 2;

        int i = 0, j = n - 1;
        int pivot = quickSelect(nums, i, j);
        while (pivot != k) {
            if (pivot > k) {
                j=pivot-1;
            } else {
                i=pivot+1;
            }
            pivot = quickSelect(nums,i,j);
        }
        int mid = nums[pivot];

        i=j=0;
        k=n-1;
        while(j<=k){
            if(nums[(2 * j + 1) % (n | 1)] > mid){
                swap(nums,(2 * j + 1) % (n | 1),(2 * i + 1) % (n | 1));
                ++i;
                ++j;
            }else if(nums[(2 * j + 1) % (n | 1)] < mid){
                swap(nums,(2 * j + 1) % (n | 1),(2 * k + 1) % (n | 1));
                --k;
            }else{
                ++j;
            }
        }


    }

    int quickSelect(int[] nums, int i, int j) {
        int pivotIndex = i;
        for (; i < j; ++i) {
            if (nums[i] < nums[j]) {
                swap(nums, i, pivotIndex++);
            }
        }
        swap(nums, pivotIndex, j);

        return pivotIndex;
    }

    void swap(int[] nums, int i, int j) {
        if (i == j) {
            return;
        }
        nums[i] = nums[i] ^ nums[j];
        nums[j] = nums[i] ^ nums[j];
        nums[i] = nums[i] ^ nums[j];
    }

    @Test
    void test() {
        int[] nums = new int[]{1, 5, 1, 1, 6, 4};
        wiggleSort2(nums);
        System.out.println(nums);
    }


}
