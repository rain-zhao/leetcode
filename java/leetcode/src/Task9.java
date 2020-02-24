public class Task9 {
    public boolean isPalindrome(int x) {
        if(x < 0){
            return false;
        }
        if(x == 0){
            return true;
        }

        int reverse = 0;
        int num = x;
        while(num != 0){
            reverse = reverse*10 + num%10;
            if(reverse <= 0){
                return false;
            }
            num /=10;
        }

        return reverse - x == 0;
    }
}
