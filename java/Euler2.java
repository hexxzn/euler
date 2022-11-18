public class Euler2 {
    // https://projecteuler.net/problem=2
    
    public static void main(String[] args) {
        System.out.printf("The sum of the even-valued terms whose values do not exceed 4,000,000 is %d.", fibonacciSum());
    }

    public static int fibonacciSum() {
        int a = 0, b = 1, c = 2;
        int sum = 0;

        while (b < 4000000) {
            a = b;
            b = c;
            c = a + b;

            if (a % 2 == 0) {
                sum += a;
            }
        }

        return sum;
    }
}