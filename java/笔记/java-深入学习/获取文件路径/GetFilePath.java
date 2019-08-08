import java.util.List;
import java.util.ArrayList;
import java.io.*;

/* 
 * 使用递归获取文件路径
 */
public class GetFilePath {
	private List<File> fileList = new ArrayList<>();

	public void getFiles(File path) {
		if (path.exists()) {
			if (path.isDirectory()) {
				File[] files = path.listFiles();
				for (File f : files) {
					getFiles(f);
				}
			} else {
				fileList.add(path);
			}
		}
	}

	public void printFileList() {
		// 打印
		for (File file : fileList) {
			System.out.println(file.getPath());
		}
	}

	public static void testGetFiles() {
		GetFilePath test = new GetFilePath();
		File file = new File("C:\\Study\\github\\Lookoops\\java");
		test.getFiles(file);
		test.printFileList();
	}
	public static void main(String[] args) {
		testGetFiles();
	}
}