import org.junit.jupiter.api.Test;

public class Task12 {
    public String intToRoman(int num) {
        if(num == 0){
            return "";
        }
        StringBuilder sb = new StringBuilder();
        while(num >= 1000){
            num-=1000;
            sb.append("M");
        }
        if(num >= 900){
            num-=900;
            sb.append("CM");
        }else if(num >= 500){
            num-=500;
            sb.append("D");
        }else if(num >= 400){
            num-=400;
            sb.append("CD");
        }
        while(num >= 100){
            num-=100;
            sb.append("C");
        }
        if(num >= 90){
            num-=90;
            sb.append("XC");
        }else if(num >= 50){
            num-=50;
            sb.append("L");
        }else if(num >= 40){
            num-=40;
            sb.append("XL");
        }
        while(num >= 10){
            num-=10;
            sb.append("X");
        }
        if(num >= 9){
            num-=9;
            sb.append("IX");
        }else if(num >= 5){
            num-=5;
            sb.append("V");
        }else if(num >= 4){
            num-=4;
            sb.append("IV");
        }
        while(num >= 1){
            num-=1;
            sb.append("I");
        }

        return sb.toString();
    }

    public String intToRoman2(int num) {
        if(num == 0){
            return "";
        }
        int[] vals = new int[]{1000,900,500,400,100,90,50,40,10,9,5,4,1};
        String[] roms = new String[]{"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};

        int idx = 0;
        StringBuilder sb = new StringBuilder();

        while(num > 0){
            while(num < vals[idx]){
                ++idx;
            }
            num -=vals[idx];
            sb.append(roms[idx]);
        }

        return sb.toString();
    }


    @Test
    void test(){
        int num = 1994;
        System.out.println(intToRoman2(num));
    }
}
