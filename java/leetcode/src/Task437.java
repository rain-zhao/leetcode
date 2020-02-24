import org.junit.jupiter.api.Test;

import java.util.HashMap;
import java.util.Map;

public class Task437 {
    int cnt = 0;
    public int pathSum(TreeNode root, int sum) {
        if(root == null){
            return 0;
        }
        int pathSum = 0;
        Map<Integer,Integer> map = new HashMap<>();
        map.put(0,1);

        dfs(root,sum,map,pathSum);

        return cnt;
    }

    private void dfs(TreeNode root, int sum, Map<Integer, Integer> map, int pathSum) {
        if(root == null){
            return;
        }
        pathSum +=root.val;

        cnt +=map.getOrDefault(pathSum-sum,0);

        map.put(pathSum,map.getOrDefault(pathSum,0)+1);

        dfs(root.left,sum,map,pathSum);
        dfs(root.right,sum,map,pathSum);

        map.put(pathSum,map.get(pathSum)-1);

    }


    @Test
    void test(){
        TreeNode root = new TreeNode(5).left(4).right(8);
        root.left.left(11);
        root.right.left(13).right(4);
        root.left.left.left(7).right(2);
        root.right.left.left(5).right(1);
        int sum = 22;
        System.out.println(pathSum(root,sum));
    }

}
