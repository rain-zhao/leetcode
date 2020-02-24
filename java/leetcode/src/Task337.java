import org.junit.jupiter.api.Test;

import java.util.HashMap;
import java.util.Map;

public class Task337 {
    public int rob(TreeNode root) {
        if (root == null) {
            return 0;
        }
        Map<TreeNode, Integer> map0 = new HashMap<>();
        Map<TreeNode, Integer> map1 = new HashMap<>();
        dfs(root, map0, map1);

        return Math.max(map0.getOrDefault(root, 0), map1.getOrDefault(root, 0));
    }

    void dfs(TreeNode root, Map<TreeNode, Integer> map0, Map<TreeNode, Integer> map1) {
        if (root.left == null && root.right == null) {
            map0.put(root, 0);
            map1.put(root, root.val);
            return;
        }
        //drill down
        if (root.left != null) {
            dfs(root.left, map0, map1);
        }
        if (root.right != null) {
            dfs(root.right, map0, map1);
        }

        int left, right;
        //choose
        left = root.left == null ? 0 : map0.get(root.left);
        right = root.right == null ? 0 : map0.get(root.right);
        map1.put(root, left + right + root.val);

        //no choose
        left = root.left == null ? 0 : Math.max(map0.get(root.left), map1.get(root.left));
        right = root.right == null ? 0 : Math.max(map0.get(root.right), map1.get(root.right));

        map0.put(root, left + right);
    }

    public int rob2(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int[] res = dfs(root);
        return Math.max(res[0], res[1]);
    }

    int[] dfs(TreeNode root) {
        int[] res = new int[2];
        if (root == null) {
            return res;
        }
        //drill down
        int[] l = dfs(root.left);

        int[] r = dfs(root.right);

        //choose
        res[1] = l[0] + r[0] + root.val;
        //no choose
        res[0] = Math.max(l[0], l[1]) + Math.max(r[0], r[1]);

        return res;
    }

    @Test
    void test() {
        TreeNode root = new TreeNode(3);
        root.left(2).right(3);
        root.left.right(3);
        root.right.right(1);

        System.out.println(rob2(root));
    }
}
