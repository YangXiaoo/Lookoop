// ThreadPoolTraverseDirectory.java
// 2019-3-17
// 线程池：https://blog.csdn.net/liujiahan629629/article/details/84454908
import java.io.*;
import java.util.*;
import java.util.concurrent.*;

public class ThreadPoolTraverseDirectory {
	public static void main(String[] args) {
		String directory = "C:\\Study\\github\\Lookoops";
        String keyword = ".java";

        ExecutorService pool = Executors.newCachedThreadPool();
        Matcher matcher = new Matcher(new File(directory), keyword, pool);
        Future<List<File>> result = pool.submit(matcher);

        try {
        	System.out.println("[INFO] results: ");
        	for (File file : result.get()) {
        		System.out.println(file.getPath());
        	}
        	// System.out.println(task.get().toString());
        } catch (ExecutionException e) {
        	e.printStackTrace();
        } catch (InterruptedException e) {
        	e.printStackTrace();
        }

        int largestPoolSize = ((ThreadPoolExecutor) pool).getLargestPoolSize();
        System.out.println("[INFO] largestPoolSize: " + largestPoolSize);
	}
}

/**
 * 继承Callabel，有返回值的异步运行任务
 */
class Matcher implements Callable<List<File>> {
	private File directory;
	private String keyword;
	private ExecutorService pool;

	/**
	 * Matcher构造
	 * @param directory 待遍历目录
	 * @param keyword 查询的关键字
	 */
	public Matcher(File directory, String keyword, ExecutorService pool) {
		this.directory = directory;
		this.keyword = keyword;
		this.pool = pool;
	}

 
	/**
	 * 重写Callable的call()方法
	 * @return 匹配的文件列表
	 */
	public List<File> call() {
		List<File> result = new ArrayList<>();
		try {
			File[] files = directory.listFiles();
			List<Future<List<File>>> results = new ArrayList<>();

			for (File file : files) {
				if (file.isDirectory()) {	// 如果是目录则继续调用Matcher
					Matcher matcher = new Matcher(file, keyword, pool);
			        Future<List<File>> ret = pool.submit(matcher);
			        results.add(ret);
				} else {
					if (patternSearch(file, keyword)) {
						result.add(file);
					}
				}
			}

			for (Future<List<File>> res : results) {
				try {
					result.addAll(res.get());	// 使用addAll, 因为返回的是List<File>
				} catch (ExecutionException e) {
					e.printStackTrace();
				}
			}
		} catch (InterruptedException e) {
			e.printStackTrace();
		}

		return result;
	}

    /**
     * 指定文件名
     * @param file 待匹配文件
     * @param keyword 关键词
     */
    public static boolean patternSearch(File file, String keyword) {
        try {
            String fileName = file.getName();
            if (fileName.contains(keyword)) {
                return true;
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        return false;
    }
}