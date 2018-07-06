public class HelloWorld {
    public static void main(String []args) {
        System.out.println("Hello world");
        try
        {
        	Thread.currentThread().sleep(5 * 1000);
        }
        catch(InterruptedException e)
        {
        }
    }
}