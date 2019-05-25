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
    public int aMethod(){
        static int i = 0;
        i++;
        return i;
    }
public static void main(String args[]){
    Test test = new Test();
    test.aMethod();
    int j = test.aMethod();
    System.out.println(j);
    }
}