public class Test{
static{
   int x=5;
}
static int x,y;
public static void main(String args[]){
    int i = 0;
    i = i++;
    System.out.println(i);
    i = ++i;
    System.out.println(i);
}
}