public class Task50 {
//    public static double myPow(double x, int n) {
//        if(n == 0){
//            return 1.0;
//        }
//
//        if(n < 0){
//            return 1.0/(x*myPow(x,-n-1));
//        }
//
//        double factor = n%2 == 1 ? x:1;
//
//        return myPow(x*x,n/2) * factor;
//
//    }

    public static double myPow(double x, int n) {

        if(n == Integer.MIN_VALUE){
            n = -(n/2);
            x =1/(x*x);
        }else if(n < 0 ){
            n = -n;
            x =1/x;
        }

        double pow = 1;
        while(n != 0){
            if(n%2 == 1){
                pow *=x;
            }
            x *= x;
            n >>=1;

        }
        return pow;
    }

    public static void main(String[] args) {
        double x = 1.00000;
        int n = -2147483648;

        System.out.println(myPow(x,n));
    }
}
