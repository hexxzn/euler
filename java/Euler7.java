public class Euler7 {
    // https://projecteuler.net/problem=7
    public static void main(String[] args) {
        int count = 0;
        int test = 0;

        while (true) {
            if (Algos.isPrime(test)) {
                count++;
            }

            if (count == 10001) {
                break;
            }

            test++;
        }

        System.out.print(test);
    }
}
