import java.io.*;
import java.util.*;

import java.io.*; 
public class Main{ 
public static void readFile(String sourceFilePath, String encode) throws IOException
{ 
	File file = new File(sourceFilePath); 
	BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(file), encode)); 
	StringBuilder strBuilder = new StringBuilder(); 
	String sLine = null; 
	while((sLine = br.readLine()) != null) { 
		strBuilder.append(sLine); 
		strBuilder.append("\r\n"); 
	} 
	br.close(); 
	System.out.println(strBuilder.toString()); 
} 
public static String[] getFileNames(String path){ 
	File dirFile = new File(path); 
	if(dirFile.isDirectory()){ 
		File[] files = dirFile.listFiles(); 
		String[] fileNames = new String[files.length]; 
		for(int i=0;i<files.length;i++){ 
			fileNames[i] = files[i].getAbsolutePath(); 
		} 

	return fileNames; 
}else{ return null; } } public static void main(String[] args) throws Exception{ //读取单个文件 String path = "\\\\ant.amazon.com\\Dept-AS\\pek02\\CN-Trans\\User\\XXX\\sql\\sql1.txt"; readFile(path, "utf-8"); //读取某个目录下所有文件 String[] fileNames = getFileNames("\\\\ant.amazon.com\\Dept-AS\\pek02\\CN-Trans\\User\\XXX"); String encode = "utf-8"; for(String fileName : fileNames){ try { readFile(fileName, encode); } catch (IOException e) { } } } }
 