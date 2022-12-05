public class Euler5 {
    // https://projecteuler.net/problem=5

    public static void main(String[] args) {
        int dividend = 0;
        boolean solution = false;

        while (solution == false) {
            dividend += 1;

            for (int x = 1; x <= 20; x++) {
                if (dividend % x != 0) {
                    break;
                }
                if (x == 20) {
                    solution = true;
                }
            }
        }

        System.out.print(dividend);
    }
}
