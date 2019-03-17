import java.io.*;
import java.util.*;
import java.util.concurrent.*;

public class ForkJoinThreadPoolDemo extends RecursiveTask<Long> {
 
    private static final int THRESHOLD = 10000;
    private long start;
    private long end;
 
    public ForkJoinThreadPoolDemo(long start, long end) {
        this.start = start;
        this.end = end;
    }
 
    @Override
    protected Long compute() {
        long sum = 0;
        boolean canCompute = (end - start) < THRESHOLD;
        if (canCompute) {
            for (long i = start; i < end; i++) {
                sum += i;
            }
        } else {
            //分成100份进行处理
            long step = (start + end) / 50;
            ArrayList<ForkJoinThreadPoolDemo> subTasks = new ArrayList<>();
            long pos = start;
            for (int i = 0; i < 50; i++) {
                long lastOne = pos + step;
                if (lastOne > end) {
                    lastOne = end;
                }
                ForkJoinThreadPoolDemo subTask = new ForkJoinThreadPoolDemo(pos, lastOne);
                pos += step;
                subTasks.add(subTask);
                subTask.fork();
            }
            for (ForkJoinThreadPoolDemo t : subTasks) {
                sum += t.join();
            }
        }
        return sum;
    }
 
    //结果199990000
    public static void main(String[] args) {
        ForkJoinPool forkJoinPool = new ForkJoinPool();
        ForkJoinThreadPoolDemo task = new ForkJoinThreadPoolDemo(0, 20000);
        ForkJoinTask<Long> result = forkJoinPool.submit(task);
 
        try {
            long res = result.get();
            System.out.println("结果" + res);
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (ExecutionException e) {
            e.printStackTrace();
        }
 
    }
}