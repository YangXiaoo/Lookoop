/**
 * @author "shihuc"
 * @date   2017年1月17日
 */
package bucketSort;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

/**
 * @author shihuc
 * 
 * 桶排序的实现过程，算法中考虑到了元素的重复性
 */
public class BucketSortDemo {
    
    /**
     * @param args
     */
    public static void main(String[] args) {
        File file = new File("./src/bucketSort/sample.txt");
        Scanner sc = null;
        try {
            sc = new Scanner(file);
            //获取测试例的个数
            int T = sc.nextInt();
            for(int i=0; i<T; i++){
                //获取每个测试例的元素个数
                int N = sc.nextInt();
                //获取桶的个数
                int M = sc.nextInt();                                
                int A[] = new int[N];
                for(int j=0; j<N; j++){
                    A[j] = sc.nextInt();
                }    
                bucketSort(A, M);
                printResult(i, A);
            }
        } catch (FileNotFoundException e) {            
            e.printStackTrace();
        } finally {
            if(sc != null){
                sc.close();
            }
        }
    }
    
    /**
     * 计算输入元素经过桶的个数（M）求商运算后，存入那个桶中，得到桶的下标索引。
     * 步骤1
     * 注意：
     * 这个方法，其实就是桶排序中的相对核心的部分，也就是常说的待排序数组与桶之间的映射规则f（x）的定义部分。 
     * 这个映射规则，对于桶排序算法的不同实现版本，规则函数不同。
     * 
     * @param elem 原始输入数组中的元素值
     * @param m 桶的商数（影响桶的个数）
     * @return 桶的索引号（编号）
     */
    private static int getBucketIndex(int elem, int m){        
        return elem / m;
    }
    
    private static void bucketSort(int src[], int m){
        //定义一个初步排序的桶与原始数据大小的映射关系
        HashMap<Integer, ArrayList<Integer>> buckets = new HashMap<Integer, ArrayList<Integer>>();
        
        //规划数据入桶  【步骤2】              
        programBuckets(src, m, buckets);
        
        //对桶基于桶的标号进行排序（序号可能是负数）【步骤3】
        Integer bkIdx[] = new Integer[buckets.keySet().size()];
        buckets.keySet().toArray(bkIdx);
        quickSort(bkIdx, 0, bkIdx.length - 1);
        
        //计算每个桶对应于输出数组空间的其实位置
        HashMap<Integer, Integer> bucketIdxPosMap = new HashMap<Integer, Integer>();
        int startPos = 0;
        for(Integer idx: bkIdx){
            bucketIdxPosMap.put(idx, startPos);
            startPos += buckets.get(idx).size();
        }
        
        //对桶内的数据采取快速排序,并将排序后的结果映射到原始数组中作为输出
        for(Integer bId : buckets.keySet()){
            ArrayList<Integer> bk = buckets.get(bId);
            Integer[] org = new Integer[bk.size()];
            bk.toArray(org);            
            quickSort(org, 0, bk.size() - 1); //对桶内数据进行排序 【步骤4】
            //将排序后的数据映射到原始数组中作为输出 【步骤5】
            int stPos = bucketIdxPosMap.get(bId); 
            for(int i=0; i<org.length; i++){
                src[stPos++] = org[i];
            }
        }        
    }
    
    /**
     * 基于原始数据和桶的个数，对数据进行入桶规划。
     * 
     * 这个过程，就体现了divide-and-conquer的思想
     * 
     * @param src
     * @param m
     * @param buckets
     */
    private static void programBuckets(int[] src, int m, HashMap<Integer, ArrayList<Integer>> buckets) {
        for(int i=0; i<src.length; i++){
            int bucketIdx = getBucketIndex(src[i], m);
            
            ArrayList<Integer> bucket = buckets.get(bucketIdx);
            if(bucket == null){
                //定义桶，用来存放初步划分好的原始数据
                bucket = new ArrayList<Integer>();
                buckets.put(bucketIdx, bucket);
            }
            bucket.add(src[i]);
        }
    }
    
    /**
     * 采用类似两边夹逼的方式，向输入数组的中间某个位置夹逼，将原输入数组进行分割成两部分，左边的部分全都小于某个值，
     * 右边的部分全都大于某个值。
     * 
     * 快排算法的核心部分。
     * 
     * @param src 待排序数组
     * @param start 数组的起点索引
     * @param end 数组的终点索引
     * @return 中值索引
     */
    private static int middle(Integer src[], int start, int end){
        int middleValue = src[start];
        while(start < end){
            //找到右半部分都比middleValue大的分界点
            while(src[end] >= middleValue && start < end){
                end--;
            }
            //当遇到比middleValue小的时候或者start不再小于end，将比较的起点值替换为新的最小值起点            
            src[start] = src[end];            
            //找到左半部分都比middleValue小的分界点
            while(src[start] <= middleValue && start < end){
                start++;
            }
            //当遇到比middleValue大的时候或者start不再小于end，将比较的起点值替换为新的终值起点
            src[end] = src[start];            
        }
        //当找到了分界点后，将比较的中值进行交换，将中值放在start与end之间的分界点上，完成一次对原数组分解，左边都小于middleValue，右边都大于middleValue
        src[start] = middleValue;
        return start;
    }
    
    /**
     * 通过递归的方式，对原始输入数组，进行快速排序。
     * 
     * @param src 待排序的数组
     * @param st 数组的起点索引
     * @param nd 数组的终点索引
     */
    public static void quickSort(Integer src[], int st, int nd){
        
        if(st > nd){
            return;
        }
        int middleIdx = middle(src, st, nd);
        //将分隔后的数组左边部分进行快排
        quickSort(src, st, middleIdx - 1);
        //将分隔后的数组右半部分进行快排
        quickSort(src, middleIdx + 1, nd);
    }

    /**
     * 打印最终的输出结果
     * 
     * @param idx 测试例的编号
     * @param B 待输出数组
     */
    private static void printResult(int idx, int B[]){
        System.out.print(idx + "--> ");
        for(int i=0; i<B.length; i++){
            System.out.print(B[i] + "  ");
        }
        System.out.println();
    }
}