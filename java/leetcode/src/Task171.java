public class Task171 {
    public int titleToNumber(String s) {
        int number = 0;
        for (char c : s.toCharArray()) {
            number = number*26+c-'A'+1;
        }
        return number;
    }

    public static void main(String[] args) {
        String s = "AB";
        Task171 task = new Task171();
        System.out.println(task.titleToNumber(s));
    }
}
