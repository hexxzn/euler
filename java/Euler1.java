public class Euler1 {
    // https://projecteuler.net/problem=1
    
    public static void main(String[] args) {
        int sum = 0;

        for (int n = 0; n < 1000; n++) {
            if (n % 3 == 0 || n % 5 == 0) {
                sum += n;
            }
        }

        System.out.print(sum);
    }
}
