import java.util.concurrent.Semaphore;

public class Task1117 {
    class H2O {

        Semaphore oxygen = new Semaphore(2);
        Semaphore hydrogen = new Semaphore(0);

        public H2O() {


        }

        public void hydrogen(Runnable releaseHydrogen) throws InterruptedException {
            hydrogen.acquire();
            // releaseHydrogen.run() outputs "H". Do not change or remove this line.
            releaseHydrogen.run();
            oxygen.release();
        }

        public void oxygen(Runnable releaseOxygen) throws InterruptedException {
            oxygen.acquire(2);
            // releaseOxygen.run() outputs "H". Do not change or remove this line.
            releaseOxygen.run();
            hydrogen.release(2);


        }
    }
}
