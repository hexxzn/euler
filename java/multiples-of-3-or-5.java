// Problem 1
// https://projecteuler.net/problem=1

import java.time.Duration;
import java.time.Instant;

 class Main {
    public static void main(String[] args) {

            Instant startTime = Instant.now();
            multipleSum(1000);
            System.out.println(Duration.between(startTime, Instant.now()).toString());
    }

    public static void multipleSum(int limit) {

        int sum = 0;

        for(int i = 1; i < limit; i++) {
            if(i % 3 == 0) {
                sum += i;
                continue;
            }
            if(i % 5 == 0) {
                sum += i;
            }
        }

        System.out.println(sum);
    }
}

////////////////////
// Answer: 233168 //
// Time: 0:00.000 //
////////////////////

