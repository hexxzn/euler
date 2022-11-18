public class Euler4 {
    // https://projecteuler.net/problem=4
    
    public static void main(String[] args) {
        System.out.printf("The largest palindrome made from the product of two 3-digit numbers is %d.", largestPalindrome());
    }

    public static int largestPalindrome() {
        int largestPalindrome = 0;
        
        for (int x = 100; x < 1000; x++) {
            for (int y = 100; y < 1000; y++) {
                int product = x * y;

                String forward = Integer.toString(product);
                String reverse = new StringBuilder(forward).reverse().toString();
                
                if (forward.equals(reverse) && product > largestPalindrome) {
                    largestPalindrome = product;
                }
            }
        }

        return largestPalindrome;
    }
}
