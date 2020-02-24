import org.junit.jupiter.api.Test;

import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;
import java.util.function.IntConsumer;

public class Task1195 {
    class FizzBuzz {
        private final int n;
        ReentrantLock lock = new ReentrantLock();
        Condition number = lock.newCondition();
        Condition fizz = lock.newCondition();
        Condition buzz = lock.newCondition();
        Condition fizzbuzz = lock.newCondition();

        public FizzBuzz(int n) {
            this.n = n;
        }

        // printFizz.run() outputs "fizz".
        public void fizz(Runnable printFizz) throws InterruptedException {
            lock.lock();
            try {
                fizz.await();
                int cnt = n / 3 - n / 15;
                for (int i = 0; i < cnt; i++) {
                    printFizz.run();
                    number.signal();
                    fizz.await();
                }
            } finally {
                lock.unlock();
            }
        }

        // printBuzz.run() outputs "buzz".
        public void buzz(Runnable printBuzz) throws InterruptedException {
            lock.lock();
            try {
                buzz.await();
                int cnt = n / 5 - n / 15;
                for (int i = 0; i < cnt; i++) {
                    printBuzz.run();
                    number.signal();
                    buzz.await();
                }
            } finally {
                lock.unlock();
            }
        }

        // printFizzBuzz.run() outputs "fizzbuzz".
        public void fizzbuzz(Runnable printFizzBuzz) throws InterruptedException {
            lock.lock();
            try {
                fizzbuzz.await();
                for (int i = 0; i < n / 15; i++) {
                    printFizzBuzz.run();
                    number.signal();
                    fizzbuzz.await();
                }
            } finally {
                lock.unlock();
            }
        }

        // printNumber.accept(x) outputs "x", where x is an integer.
        public void number(IntConsumer printNumber) throws InterruptedException {
            lock.lock();
            try {
                for (int i = 1; i <= n; i++) {
                    if (i % 15 == 0) {
                        fizzbuzz.signal();
                        number.await();
                    } else if (i % 3 == 0) {
                        fizz.signal();
                        number.await();
                    } else if (i % 5 == 0) {
                        buzz.signal();
                        number.await();
                    } else {
                        printNumber.accept(i);
                    }
                }
                buzz.signal();
                fizz.signal();
                fizzbuzz.signal();
            } finally {
                lock.unlock();
            }
        }
    }

    @Test
    void test() throws InterruptedException {
        FizzBuzz cls = new FizzBuzz(15);
        new Thread(() -> {
            try {
                cls.fizz(() -> {
                    System.out.println("fizz");
                });
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }).start();
        new Thread(() -> {
            try {
                cls.buzz(() -> {
                    System.out.println("buzz");
                });
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }).start();
        new Thread(() -> {
            try {
                cls.fizzbuzz(() -> {
                    System.out.println("fizzbuzz");
                });
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }).start();
        new Thread(() -> {
            try {
                cls.number(val -> {
                    System.out.println(val);
                });
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }).start();
    }

}
