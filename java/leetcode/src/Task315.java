import org.junit.jupiter.api.Test;

import java.util.*;
import java.util.stream.Collectors;

public class Task315 {
    //brute force
    public List<Integer> countSmaller(int[] nums) {
        int len = nums.length;
        Integer[] cnts = new Integer[len];
        for (int i = 0; i < len; i++) {
            int cnt = 0;
            for (int j = i + 1; j < len; j++) {
                if (nums[i] > nums[j]) {
                    ++cnt;
                }
            }
            cnts[i] = cnt;
        }
        return Arrays.asList(cnts);
    }

    int[] tmp;

    //merge sort
    public List<Integer> countSmaller2(int[] nums) {
        if (nums.length == 0) {
            return Collections.emptyList();
        }
        int len = nums.length;
        tmp = new int[len];
        int[] cnts = new int[len];
        int[] idxs = new int[len];
        for (int i = 0; i < len; i++) {
            idxs[i] = i;
        }
        mergeSort(nums, cnts, idxs, 0, len - 1);
        return Arrays.stream(cnts).boxed().collect(Collectors.toList());
    }

    private void mergeSort(int[] nums, int[] cnts, int[] idxs, int left, int right) {
        if (left == right) {
            return;
        }
        int mid = (left + right) / 2;
        mergeSort(nums, cnts, idxs, left, mid);
        mergeSort(nums, cnts, idxs, mid + 1, right);
        if (nums[idxs[mid]] > nums[idxs[mid + 1]]) {
            merge(nums, cnts, idxs, left, right);
        }

    }

    private void merge(int[] nums, int[] cnts, int[] idxs, int left, int right) {
        //copy
        for (int i = left; i <= right; i++) {
            tmp[i] = idxs[i];
        }

        int mid = (left + right) / 2;
        int p1 = mid, p2 = right, p3 = right;
        while (p1 >= left && p2 > mid) {
            if (nums[tmp[p1]] <= nums[tmp[p2]]) {
                idxs[p3--] = tmp[p2--];
            } else {
                cnts[idxs[p1]] += p2 - mid;
                idxs[p3--] = tmp[p1--];
            }
        }
        while (p1 >= left) {
            idxs[p3--] = tmp[p1--];
        }
        while (p2 > mid) {
            idxs[p3--] = tmp[p2--];
        }

    }


    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        int cnt;

        TreeNode(int val) {
            this.val = val;
        }
    }

    public List<Integer> countSmaller3(int[] nums) {
        if (nums.length == 0) {
            return Collections.emptyList();
        }
        int len = nums.length;
        int[] cnts = new int[len];
        TreeNode root = null;

        for (int i = len - 1; i >= 0; i--) {
            root = insert(root, i, nums[i], cnts);
        }

        return Arrays.stream(cnts).boxed().collect(Collectors.toList());
    }

    TreeNode insert(TreeNode root, int idx, int val, int[] cnts) {
        if (root == null) {
            return new TreeNode(val);
        } else if (val <= root.val) {
            ++root.cnt;
            root.left = insert(root.left, idx, val, cnts);
        } else {
            cnts[idx] += root.cnt + 1;
            root.right = insert(root.right, idx, val, cnts);
        }
        return root;
    }

    //////////////////////////////////////////////////////////
    class FenwickTree {

        int[] tree;
        int len;

        FenwickTree(int n) {
            len = n;
            tree = new int[n + 1];
        }

        void update(int i, int delta) {
            while (i <= len){
                tree[i] += delta;
                i+=lowBit(i);
            }
        }

        int query(int idx) {
            int sum = 0;
            while (idx > 0) {
                sum += tree[idx];
                idx -= lowBit(idx);
            }
            return sum;
        }

        int lowBit(int idx) {
            return idx & -idx;
        }
    }

    public List<Integer> countSmaller4(int[] nums) {
        if (nums.length == 0) {
            return Collections.emptyList();
        }
        //pre process
        int len = nums.length;
        Integer[] idxs = new Integer[len];
        for (int i = 0; i < len; i++) {
            idxs[i] = i;
        }
        Arrays.sort(idxs, Comparator.comparingInt(i -> nums[i]));
        for (int i = 0; i < len; i++) {
            nums[idxs[i]] = i+1;
        }
        
        List<Integer> res = new ArrayList<>();
        
        FenwickTree tree = new FenwickTree(len);

        for (int i = len-1; i >= 0; i--) {
            tree.update(nums[i],1);
            res.add(tree.query(nums[i]-1));
        }
        Collections.reverse(res);
        return res;
    }
    @Test
    void test() {
        int[] nums = new int[]{5, 2, 6, 1};
        System.out.println(countSmaller4(nums));
    }
}
