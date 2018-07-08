import java.io.*;

public class Test {
    public static void main(String []args) throws IOException {
        System.out.println("文件流操作");

        File f = new File("test.txt");

        // 构建FileOutputStream对象，文件不存在会自动创建
        FileOutputStream fout = new FileOutputStream(f);

        // 构建OutputStreamWriter对象，参数可以指定编码，默认操作系统编码，windows上市gbk
        OutputStreamWriter writer = new OutputStreamWriter(fout, "UTF-8");

        // 写入到文件
        writer.append("中文输入保存到文件test.txt中");
        writer.append("\r\n");
        writer.append("English");

        // 关闭写入流
        writer.close();

        // 关闭输出流
        fout.close();

        FileInputStream fin = new FileInputStream(f);
        InputStreamReader reader = new InputStreamReader(fin, "UTF-8");

        StringBuffer sb = new StringBuffer();
        while (reader.ready()) {
        	// 转换成char加入到StringBuffer对象中
        	sb.append((char) reader.read());
        }

        System.out.println(sb.toString());

        reader.close();
        fin.close();
    }
}