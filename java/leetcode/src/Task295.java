import org.junit.jupiter.api.Test;

import java.util.PriorityQueue;

public class Task295 {
    class MedianFinder {
        PriorityQueue<Integer> lo = new PriorityQueue<>((a, b) -> b - a);
        PriorityQueue<Integer> hi = new PriorityQueue<>();

        /**
         * initialize your data structure here.
         */
        public MedianFinder() {

        }

        public void addNum(int num) {
            lo.offer(num);
            hi.offer(lo.poll());
            if (lo.size() != hi.size()) {
                lo.offer(hi.poll());
            }
        }

        public double findMedian() {
            return lo.size() == hi.size() ? (lo.peek() + hi.peek()) * .5 : lo.peek();
        }
    }



    @Test
    void test() {
        MedianFinder finder = new MedianFinder();
        finder.addNum(1);
        finder.addNum(2);
        System.out.println(finder.findMedian());
        finder.addNum(3);
        System.out.println(finder.findMedian());
    }
}
