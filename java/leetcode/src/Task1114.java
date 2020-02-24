import org.junit.jupiter.api.Test;

import java.util.concurrent.CountDownLatch;

public class Task1114 {

//    class Foo {
//
//        ReentrantLock lock = new ReentrantLock();
//
//        Condition condition1 = lock.newCondition();
//        Condition condition2 = lock.newCondition();
//
//        int state = 1;
//
//        public Foo() {
//
//        }
//
//        public void first(Runnable printFirst) throws InterruptedException {
//            try {
//                lock.lock();
//                // printFirst.run() outputs "first". Do not change or remove this line.
//                printFirst.run();
//
//                state = 2;
//                condition1.signal();
//            }finally {
//                lock.unlock();
//            }
//
//
//        }
//
//        public void second(Runnable printSecond) throws InterruptedException {
//            try {
//                lock.lock();
//                if(state != 2){
//                    condition1.await();
//                }
//                state = 3;
//                // printSecond.run() outputs "second". Do not change or remove this line.
//                printSecond.run();
//                condition2.signal();
//            }finally {
//                lock.unlock();
//            }
//
//        }
//
//        public void third(Runnable printThird) throws InterruptedException {
//            try {
//                lock.lock();
//                if(state != 3){
//                    condition2.await();
//                }
//                // printThird.run() outputs "third". Do not change or remove this line.
//                printThird.run();
//            }finally {
//                lock.unlock();
//            }
//
//        }
//    }

    class Foo {

        CountDownLatch countDownLatch1;
        CountDownLatch countDownLatch2;

        public Foo() {
            countDownLatch1 = new CountDownLatch(1);
            countDownLatch2 = new CountDownLatch(1);
        }

        public void first(Runnable printFirst) throws InterruptedException {
            // printFirst.run() outputs "first". Do not change or remove this line.
            printFirst.run();
            countDownLatch1.countDown();

        }

        public void second(Runnable printSecond) throws InterruptedException {
                countDownLatch1.await();
                // printSecond.run() outputs "second". Do not change or remove this line.
                printSecond.run();
                countDownLatch2.countDown();
        }

        public void third(Runnable printThird) throws InterruptedException {
            countDownLatch2.await();
            // printThird.run() outputs "third". Do not change or remove this line.
            printThird.run();
        }
    }

    @Test
    void test() throws InterruptedException {
        Foo foo = new Foo();
        new Thread(()-> {
            try {
                foo.third(()->System.out.print("three"));
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }).start();
        new Thread(()-> {
            try {
                foo.second(()->System.out.print("two"));
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }).start();
        new Thread(()-> {
            try {
                foo.first(()->System.out.print("one"));
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }).start();


    }



}
