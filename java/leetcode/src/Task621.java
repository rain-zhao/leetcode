import org.junit.jupiter.api.Test;

public class Task621 {
    public int leastInterval(char[] tasks, int n) {
        if (tasks.length < 2) {
            return tasks.length;
        }

        int[] map = new int[26];

        for (char task : tasks) {
           ++map[task-'A'];
        }

        int res = 0;


        int max = 0;
        int maxCnt = 0;

        for (int cnt : map) {
            if(cnt > max){
                max = cnt;
                maxCnt = 1;
            }else if(cnt == max){
                ++maxCnt;
            }
        }

        res = (max-1)*(n+1)+maxCnt;
        res = Math.max(res,tasks.length);

        return res;
    }

    @Test
    void test() {
        char[] tasks = new char[]{'A','A','A','A','A','A','B','C','D','E','F','G'};
        int n = 2;
        System.out.println(leastInterval(tasks, n));
    }
}
