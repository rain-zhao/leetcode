import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class Task406 {
    public int[][] reconstructQueue(int[][] people) {
        if (people.length < 2){
            return people;
        }
        int[][] res = new int[people.length][2];
        //init
        for (int[] node : res) {
            node[0]=-1;
        }

        Arrays.sort(people, Comparator.comparingInt(a -> a[0]));

        for (int i = 0; i < people.length; i++) {
            int[] node = people[i];
            int j = 0,empty=0;
            while(empty != node[1]+1){
                if(res[j][0] == -1 || res[j][0] == node[0]){
                    ++empty;
                }
                ++j;
            }
            res[j-1] = node;

        }

        return res;

    }

    public int[][] reconstructQueue2(int[][] people) {
        if (people.length < 2){
            return people;
        }


        List<int[]> res = new ArrayList<>();

        Arrays.sort(people, (a,b)-> a[0] == b[0]? a[1]-b[1] : b[0]-a[0]);

        for (int[] person : people) {
            res.add(person[1],person);
        }

        return res.toArray(new int[people.length][2]);

    }
    @Test
    void test(){
        int[][] people = new int[][]{{7,0}, {4,4}, {7,1}, {5,0}, {6,1}, {5,2}};
        int[][] res = reconstructQueue2(people);
    }

}
