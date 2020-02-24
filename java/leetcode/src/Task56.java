import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class Task56 {
    public int[][] merge(int[][] intervals) {
        if(intervals.length < 2){
            return intervals;
        }

        //sort
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));

        List<int[]> list = new ArrayList<>();
        list.add(intervals[0]);

        for (int[] interval: intervals) {
            //last
            int[] ints = list.get(list.size()-1);
            if(interval[0] <=ints[1]){
                ints[1] = Math.max(ints[1],interval[1]);
            }else{
                list.add(interval);
            }
        }

        return list.toArray(new int[0][]);
    }

    @Test
    void test(){
        int[][] intervals = new int[][]{{1,3},{8,10},{15,18},{2,6}};
        int[][] result = merge(intervals);
        System.out.println(result);
    }
}
