public class Euler6 {
    // https://projecteuler.net/problem=6

    public static void main(String[] args) {
        int sumSquares = 0;
        double squareSum = 0;

        for (int n = 1; n <= 100; n++) {
            double square = Math.pow(n, 2);
            sumSquares += square;
            squareSum += n;
        }

        squareSum = Math.pow(squareSum, 2);

        System.out.print((int)(squareSum - sumSquares));
    }
}
