public class Euler3 {
    // https://projecteuler.net/problem=3
    
    public static void main(String[] args) {
        long dividend = 600851475143L;
        long divisor = 1L;

        while (divisor < dividend) {
            if (dividend % divisor == 0) {
                dividend /= divisor;
            }

            divisor += 1;
        }

        System.out.print(dividend);
    }
}
