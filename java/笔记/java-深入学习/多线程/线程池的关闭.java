// https://blog.csdn.net/zaozi/article/details/38854561#
public static void main(String[] args) {
 
    ExecutorService pool = Executors.newFixedThreadPool(5);
    final long waitTime = 8 * 1000;
    final long awaitTime = 5 * 1000;
 
    Runnable task1 = new Runnable(){
        public void run(){
            try {
                System.out.println("task1 start");
                Thread.sleep(waitTime);
                System.out.println("task1 end");
            } catch (InterruptedException e) {
                System.out.println("task1 interrupted: " + e);
            }
        }
    };
 
    Runnable task2 = new Runnable(){
        public void run(){
            try {
                System.out.println("  task2 start");
                Thread.sleep(1000);
                System.out.println("  task2 end");
            } catch (InterruptedException e) {
                System.out.println("task2 interrupted: " + e);
            }
        }
    };
    // 让学生解答某个很难的问题
    pool.execute(task1);
 
    // 生学生解答很多问题
    for(int i=0; i<1000; ++i){
        pool.execute(task2);
    }
 
    try {
        // 向学生传达“问题解答完毕后请举手示意！”
        pool.shutdown();
 
        // 向学生传达“XX分之内解答不完的问题全部带回去作为课后作业！”后老师等待学生答题
        // (所有的任务都结束的时候，返回TRUE)
        if(!pool.awaitTermination(awaitTime, TimeUnit.MILLISECONDS)){
            // 超时的时候向线程池中所有的线程发出中断(interrupted)。
            pool.shutdownNow();
        }
    } catch (InterruptedException e) {
        // awaitTermination方法被中断的时候也中止线程池中全部的线程的执行。
        System.out.println("awaitTermination interrupted: " + e);
        pool.shutdownNow();
    }
 
    System.out.println("end");
}