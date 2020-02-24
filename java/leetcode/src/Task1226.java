import java.util.concurrent.Semaphore;

public class Task1226 {
    class DiningPhilosophers {

        Semaphore[] forks = new Semaphore[5];

        public DiningPhilosophers() {
            for (int i = 0; i < 5; i++) {
                forks[i] = new Semaphore(1);
            }

        }

        // call the run() method of any runnable to execute its code
        public void wantsToEat(int philosopher,
                               Runnable pickLeftFork,
                               Runnable pickRightFork,
                               Runnable eat,
                               Runnable putLeftFork,
                               Runnable putRightFork) throws InterruptedException {
                if((philosopher & 1) == 0){
                    forks[philosopher].acquire();
                    forks[(philosopher+1)%5].acquire();
                }else{
                    forks[philosopher+1].acquire();
                    forks[philosopher].acquire();
                }

                pickLeftFork.run();
                pickRightFork.run();
                eat.run();
                putLeftFork.run();
                putRightFork.run();

                forks[philosopher].release();
                forks[(philosopher+1)%5].release();


        }
    }
}
