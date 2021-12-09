// Problem 41
// https://projecteuler.net/problem=4

import java.time.Duration;
import java.time.Instant;

class problem4 {
    public static void main(String[] args) {
        Instant startTime = Instant.now();
        largestPalindrome(3);
        System.out.println(Duration.between(startTime, Instant.now()).toString());
    }
    public static void largestPalindrome(int length) {
        String strLimit = "";
        for(int i = 0; i < length; i++) {
            strLimit += "9";
        }
        int palindrome = 0;
        int limit = Integer.parseInt(strLimit);
        for(int x = 0; x < limit; x++) {
            for(int y = 0; y < limit; y++) {
                int result = x * y;
                String strResult = Integer.toString(result);
                String strReverse = "";
                for (int i = 0; i < strResult.length(); i++) {   // reverse string
                    char ch = strResult.charAt(i);
                    strReverse = ch + strReverse;
                }
                if(Integer.parseInt(strReverse) == Integer.parseInt(strResult) && result > palindrome) {   // if result is palindrome and result is larger than largest palindrome, palindrome = result
                    palindrome = result;
                }
            }
        }
        System.out.println(palindrome);
    }
}

////////////////////
// Answer: 906609 //
// Time: 0:00.280 //
////////////////////
