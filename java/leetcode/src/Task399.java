import org.junit.jupiter.api.Test;

import java.util.*;

public class Task399 {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {

        Map<String, Map<String, Double>> map = new HashMap<>();

        for (int i = 0; i < equations.size(); i++) {
            List<String> list = equations.get(i);
            double value = values[i];

            Map<String, Double> map1;
            if (!map.containsKey(list.get(0))) {
                map1 = new HashMap<>();
                map.put(list.get(0), map1);
            } else {
                map1 = map.get(list.get(0));
            }
            map1.put(list.get(1), value);
            map1.put(list.get(0), 1.0);

            Map<String, Double> map2;
            if (!map.containsKey(list.get(1))) {
                map2 = new HashMap<>();
                map.put(list.get(1), map2);
            } else {
                map2 = map.get(list.get(1));
            }
            map2.put(list.get(0), 1.0 / value);
            map2.put(list.get(1), 1.0);
        }


        double[] res = new double[queries.size()];
        Arrays.fill(res, -1.0);

        for (int i = 0; i < queries.size(); i++) {
            List<String> query = queries.get(i);

            res[i] = dfs(map, query.get(0), query.get(1), new HashSet<String>());

        }

        return res;
    }

    private double dfs(Map<String, Map<String, Double>> map, String x, String y, Set<String> visited) {
        if (!map.containsKey(x)) {
            return -1;
        }
        Map<String, Double> pairs = map.get(x);
        if (pairs.containsKey(y)) {
            return pairs.get(y);
        } else {
            visited.add(x);
            for (Map.Entry<String, Double> pair : pairs.entrySet()) {
                if (visited.contains(pair.getKey())) {
                    continue;
                }
                double result = dfs(map, pair.getKey(), y, visited);
                if (result != -1) {
                    map.get(pair.getKey()).put(y, result);
                    result *= pair.getValue();
                    return result;
                }
            }
            visited.remove(x);
        }

        return -1;

    }

    // dp
    public double[] calcEquation2(List<List<String>> equations, double[] values, List<List<String>> queries) {
        Map<String, Integer> map = new HashMap<>();
        int idx = 0;
        for (List<String> equation : equations) {
            if (!map.containsKey(equation.get(0))) {
                map.put(equation.get(0), idx++);
            }
            if (!map.containsKey(equation.get(1))) {
                map.put(equation.get(1), idx++);
            }
        }
        //define
        double[][] dp = new double[map.size()][map.size()];
        //init
        for (double[] doubles : dp) {
            Arrays.fill(doubles, -1.0);
        }
        for (int i = 0; i < equations.size(); i++) {
            List<String> equation = equations.get(i);
            double value = values[i];

            int x = map.get(equation.get(0));
            int y = map.get(equation.get(1));
            dp[x][x] = 1;
            dp[y][y] = 1;
            dp[x][y] = value;
            dp[y][x] = 1.0 / value;
        }

        //iter
        for (int k = 0; k < dp.length; k++) {
            for (int i = 0; i < dp.length; i++) {
                if (dp[i][k] == -1.0) {
                    continue;
                }
                for (int j = 0; j < dp.length; j++) {
                    if (dp[k][j] == -1.0 || dp[i][j] != -1.0) {
                        continue;
                    }
                    dp[i][j] = dp[i][k] * dp[k][j];

                }
            }
        }


        double[] res = new double[queries.size()];


        for (int i = 0; i < queries.size(); i++) {
            List<String> query = queries.get(i);
            int x = map.getOrDefault(query.get(0), -1);
            int y = map.getOrDefault(query.get(1), -1);
            res[i] = x == -1 || y == -1 ? -1 : dp[x][y];
        }

        return res;
    }

    @Test
    void test() {
        List<List<String>> equations = Arrays.asList(
                Arrays.asList("x1", "x2"),
                Arrays.asList("x2", "x3"),
                Arrays.asList("x3", "x4"),
                Arrays.asList("x4", "x5")
        );
        double[] values = new double[]{3.0, 4.0, 5.0, 6.0};
        List<List<String>> queries = Arrays.asList(
                Arrays.asList("x1", "x5"),
                Arrays.asList("x5", "x2"),
                Arrays.asList("x2", "x4"),
                Arrays.asList("x2", "x2"),
                Arrays.asList("x2", "x9"),
                Arrays.asList("x9", "x9")
        );

        double[] res = calcEquation2(equations, values, queries);

    }
}
