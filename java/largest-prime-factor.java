// Problem 3
// https://projecteuler.net/problem=3

import java.time.Duration;
import java.time.Instant;

class Problem3 {
    public static void main(String[] args) {
        Instant startTime = Instant.now();
        long number = 600851475143L;
        factor(number);
        System.out.println(Duration.between(startTime, Instant.now()).toString());
    }

    public static void factor(long number) {
        int dividend = 1;
        while (dividend < number) {
            if (number % dividend == 0) {
                number = number / dividend;
            }
            dividend += 1;
        }
        System.out.println(number);
    }
}

/////////////////////
// Answer: 6857   ///
// Time: 0:00.001 ///
/////////////////////
