import org.junit.jupiter.api.Test;

import java.util.concurrent.Semaphore;

public class Task1115 {
//    class FooBar {
//        private int n;
//        final Object lock = new Object();
//
//        Integer flag = 0;
//
//        public FooBar(int n) {
//            this.n = n;
//        }
//
//        public void foo(Runnable printFoo) throws InterruptedException {
//            synchronized (lock) {
//                for (int i = 0; i < n; i++) {
//                    while (flag != 0) {
//                        lock.wait();
//                    }
//                    // printFoo.run() outputs "foo". Do not change or remove this line.
//                    printFoo.run();
//                    flag = 1;
//                    lock.notify();
//
//                }
//            }
//        }
//
//        public void bar(Runnable printBar) throws InterruptedException {
//            synchronized (lock) {
//                for (int i = 0; i < n; i++) {
//                    while (flag != 1) {
//                        lock.wait();
//                    }
//                    // printBar.run() outputs "bar". Do not change or remove this line.
//                    printBar.run();
//                    flag = 0;
//
//                    lock.notify();
//
//                }
//
//            }
//        }
//    }

//    class FooBar {
//        private int n;
//
//        ReentrantLock lock = new ReentrantLock();
//
//        Condition condition1 = lock.newCondition();
//        Condition condition2 = lock.newCondition();
//
//        int flag = 0;
//
//        public FooBar(int n) {
//            this.n = n;
//        }
//
//        public void foo(Runnable printFoo) throws InterruptedException {
//            lock.lock();
//            try {
//                for (int i = 0; i < n; i++) {
//                    while (flag != 0) {
//                        condition1.await();
//                    }
//                    // printFoo.run() outputs "foo". Do not change or remove this line.
//                    printFoo.run();
//                    flag = 1;
//                    condition2.signal();
//                }
//            } finally {
//                lock.unlock();
//            }
//        }
//
//
//        public void bar(Runnable printBar) throws InterruptedException {
//            lock.lock();
//            try {
//                for (int i = 0; i < n; i++) {
//                    while (flag != 1) {
//                        condition2.await();
//                    }
//                    // printBar.run() outputs "bar". Do not change or remove this line.
//                    printBar.run();
//                    flag = 0;
//                    condition1.signal();
//                }
//            } finally {
//                lock.unlock();
//            }
//        }
//    }

    class FooBar {
        private int n;

        Semaphore foo = new Semaphore(1);
        Semaphore bar = new Semaphore(0);


        public FooBar(int n) {
            this.n = n;
        }

        public void foo(Runnable printFoo) throws InterruptedException {
            for (int i = 0; i < n; i++) {
                foo.acquire();
                // printFoo.run() outputs "foo". Do not change or remove this line.
                printFoo.run();
                bar.release();
            }

        }


        public void bar(Runnable printBar) throws InterruptedException {
            for (int i = 0; i < n; i++) {
                bar.acquire();
                // printBar.run() outputs "bar". Do not change or remove this line.
                printBar.run();
                foo.release();
            }

        }
    }

    @Test
    void test() {
        FooBar fooBar = new FooBar(5);
        new Thread(() -> {
            try {
                fooBar.foo(() -> System.out.print("foo"));
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }).start();
        new Thread(() -> {
            try {
                fooBar.bar(() -> System.out.print("bar"));
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }).start();
    }
}
