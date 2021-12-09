// Problem 5
// https://projecteuler.net/problem=5

import java.time.Duration;
import java.time.Instant;

class Problem5 {
    public static void main(String[] args) {
        Instant startTime = Instant.now();
        divisibility(20);
        System.out.println(Duration.between(startTime, Instant.now()).toString());
    }

    public static void divisibility(int limit) {
        int answer = 0;
        int number = 2520;
        int increment = 2520;
        while (answer == 0) {
            for (int i = 1; i < limit + 1; i++) {
                if(number % i != 0) {
                    break;
                }
                if(i == limit) {
                    answer = number;
                }
            }
            number += increment;
        }
        System.out.println(answer);
    }
}

///////////////////////
// Answer: 232792560 //
// Time: 0:00.004    //
///////////////////////
