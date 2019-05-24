class P {  
	 public static int abc = 123;  
	 static {  
	 	System.out.println("P is init");  
	 }  
}  

class S extends P {  
 	static{  
 		System.out.println("S is init");  
 	}  
}  

public class Test {  
 	public static void main(String[] args) {  
 		System.out.println(Math.round(-7.5) + ", " + Math.round(7.5));
 	}  
}