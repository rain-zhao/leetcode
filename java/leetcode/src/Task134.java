import org.junit.jupiter.api.Test;

public class Task134 {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int min = 0;
        int[] minus = new int[gas.length + 1];

        for (int i = 0; i < gas.length; i++) {
            minus[i + 1] = minus[i] + gas[i] - cost[i];
            if (minus[min] > minus[i + 1]) {
                min = i + 1;
            }
        }

        if (minus[gas.length] < 0) {
            return -1;
        }

        return min % gas.length;

    }

    @Test
    void test() {
        int[] gas = new int[]{1, 2, 3, 4, 5};
        int[] cost = new int[]{3, 4, 5, 1, 2};
        System.out.println(canCompleteCircuit(gas,cost));
    }

}
