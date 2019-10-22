// 不使用加减乘除实现加法
public class Main{
    /**
     * 借助位运算来实现
     * @param n1
     * @param n2
     * @return
     */
    public static int add(int n1, int n2) {
        int sum = 0;
        // 相当于进位
        int carry = 0;
        do {
            // 利用异或，每位相加，此时不考虑进位
            // 比如1+2,0001 + 0011,0001^0011=0010，右起第一位1+1复合二进制进位要求，进位后的结果是0
            sum = n1 ^ n2;
            // 利用按位与，并左移，相当于进位
            // 0001&0011=0001，右起第一位1+1复合二进制进位要求，需向左进一位，所以需要左移
            carry = (n1 & n2) << 1;
            // 将上面的结果重复操作
            // 因为进位后可能还需要再向前进一位
            n1 = sum;
            n2 = carry;
            // 当无需进位时，停止运算
        } while (n2 != 0);
        return sum;
    }
 
    public static void main(String[] args) {
        int result = add(1, 2);
        System.out.println(result);

    }
}