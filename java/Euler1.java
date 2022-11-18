public class Euler1 {
    // https://projecteuler.net/problem=1
    
    public static void main(String[] args) {
        System.out.println("The sum of all multiples of 3 or 5 below 1000 is " + multipleSum() + ".");
    }

    public static int multipleSum() {
        int sum = 0;

        for (int n = 0; n < 1000; n++) {
            if (n % 3 == 0 || n % 5 == 0) {
                sum += n;
            }
        }
        
        return sum;
     }
}
