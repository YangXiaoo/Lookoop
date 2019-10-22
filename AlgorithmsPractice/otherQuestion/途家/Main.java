import java.util.*;
import java.io.*;

class Node {
    int a;
    int b;
    int c;

    public Node(int a, int b, int c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner cin = new Scanner(System.in);
        while (cin.hasNext()) {
            String[] line1 = cin.nextLine().split(" ");
            int[] lineInt = new int[3];
            for (int i = 0; i < 3; ++i) {
                lineInt[i] = Integer.parseInt(line1[i]);
            }
            String[] line2 = cin.nextLine().split(" ");
            int[] st = new int[3];
            for (int i = 0; i < 3; ++i) {
                st[i] = Integer.parseInt(line2[i]);
            }

            Node[] nodes = new Node[lineInt[1]];
            for (int i = 0; i < lineInt[1]; ++i) {
                String[] tmp = cin.nextLine().split(" ");
                int[] t = new int[3];
                for (int j = 0; j < 3; ++j) {
                    t[i] = Integer.parseInt(tmp[j]);
                }
                nodes[i] = new Node(t[0], t[1], t[2]);
            }

            int ret = solver(lineInt[0], st, nodes);
            System.out.println(ret);   
        }


    }

    public static int solver(int n, int[] st, Node[] nodes) {
         return 3;
    }
}