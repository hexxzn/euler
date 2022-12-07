public class Algos {
    // Determines whether or not an integer is a prime number
    public static boolean isPrime(int test) {
        if (test < 2) {
            return false;
        }

        for (int i = 2; i <= Math.sqrt(test); i++) {
            if (test % i == 0) {
                return false;
            }
        }

        return true;
    }
}
