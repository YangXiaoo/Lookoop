public class a_HelloWorld {
    public static void main(String []args) {
        System.out.println("Hello world");
        String[] s = {"3343", "33"};

        for (String x : s) {
	        Integer tmp = 0;
	        for (int i = x.length() - 1; i >= 0; --i) {
	            tmp = tmp * 10;
	            tmp += x.charAt(i) - '0';
	            System.out.println("tmpint: " + tmp);
	        }     	
        }
    }
}