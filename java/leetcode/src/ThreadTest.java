import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class ThreadTest {
    Lock lock = new ReentrantLock();
    Condition condition1 = lock.newCondition();
    Condition condition2 = lock.newCondition();
    Thread a = new Thread(()->{
        String[] array = new String[]{"1","2","3"};
        for (int i = 0; i < array.length ; i++) {
                lock.lock();
                System.out.println(array[i]);
                condition2.signal();
                try {
                    condition1.await();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                lock.unlock();

        }
    });

    Thread b = new Thread(()->{
        String[] array = new String[]{"a","b","c"};
        for (int i = 0; i < array.length ; i++) {
            lock.lock();
            System.out.println(array[i]);
            condition1.signal();
            try {
                condition2.await();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            lock.unlock();
        }


    });

    public static void main(String[] args) throws InterruptedException {
        ThreadTest test = new ThreadTest();
        test.a.start();
        Thread.sleep(1000);
        test.b.start();
    }
}
