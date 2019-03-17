// WriteAndReadTest.java
// 2019-3-17

import java.io.*;
import java.util.*;
// import online.yangxiao.util.*;

// https://www.cnblogs.com/zhaoyanjun/p/6376996.html
public class WriteAndReadTest {
    public static void main(String[] args) {

        String fileName = "test.txt";
        File file = new File(fileName);
        FileOutputStream fout = null;
        OutputStreamWriter writer = null;

        FileInputStream fin = null;
        InputStreamReader reader = null;

        // write
        System.out.println("[INFO] writing...");
        try {
            
            if (!file.exists()) {
                System.out.printf("[Warning] %s not exist, now creating it.\n", file.getName());
                file.createNewFile();
                fout = new FileOutputStream(file);
            } else {
                // append
                fout = new FileOutputStream(file, true); 
            }
            writer = new OutputStreamWriter(fout, "UTF-8");

            writer.append("中文输入保存到文件test.txt中");
            writer.append("\r\n");
            writer.append("English\n");

            writer.flush(); // force to write
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            // close stream
            if (writer != null) {
                try{
                    writer.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if (fout != null) {
                try{
                    fout.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }      
            }
        }

        // read
        System.out.println("[INFO] reading...");
        try {
            fin = new FileInputStream(file);
            reader = new InputStreamReader(fin, "UTF-8");
            StringBuffer sb = new StringBuffer();
            while (reader.ready()) {
                sb.append((char)reader.read());
            }
            System.out.println(sb.toString());
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (reader != null) {
                try{
                    reader.close();
                } catch (IOException e) {
                    e.printStackTrace();
                } 
            }
            if (fin != null) {
                try{
                    fin.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }     
            }
        }
        
    }
}
