// Problem 21
// https://projecteuler.net/problem=2

import java.time.Duration;
import java.time.Instant;
import java.util.*;

class Problem2 {
    public static void main(String[] args) {
        Instant startTime = Instant.now();
        evenSum(4000000);
        System.out.println(Duration.between(startTime, Instant.now()).toString());
    }

    public static void evenSum(int limit) {
        List<Integer> sequence=new ArrayList<Integer>();
        sequence.add(1);
        sequence.add(2);
        int sum = 0;
        while (sequence.get(sequence.size()-1) < limit) {
            sequence.add(sequence.get(sequence.size()-1) + sequence.get(sequence.size()-2));
        }
        if (sequence.get(sequence.size()-1) > limit) {
            sequence.remove(sequence.size()-1);
        }
        for (int i = 0; i < sequence.size(); i++) {
            if (sequence.get(i) % 2 == 0) {
                sum += sequence.get(i);
            }
        }
        System.out.println(sum);
    }
}

/////////////////////
// Answer: 4613732 //
// Time: 0:00.001  //
/////////////////////
