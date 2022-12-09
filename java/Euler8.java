import java.util.stream.Collectors;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.FileReader;

public class Euler8 {
    // https://projecteuler.net/problem=8
    public static void main(String[] args)
        throws IOException {

        BufferedReader reader = new BufferedReader(new FileReader("Input/thousand_digit_number.txt"));
        String thousandDigitNumber = reader.lines().collect(Collectors.joining());

        int[] intArray = new int[thousandDigitNumber.length()];
        long greatestProduct = 0;
        int digits = 13;

        // Isolate characters
        for (int i = 0; i < thousandDigitNumber.length(); i++) {
            intArray[i] = Integer.valueOf(thousandDigitNumber.charAt(i) - '0');
        }

        // Iterate characters
        for (int i = 0; i <= thousandDigitNumber.length() - digits; i++) {
            long product = 1;

            // Find product
            for (int j = i; j < i + digits; j++) {
                product *= intArray[j];
            }

            // Find greatest product
            if (product > greatestProduct) {
                greatestProduct = product;
            }
        }

        System.out.print(greatestProduct);
        reader.close();
    }
}
