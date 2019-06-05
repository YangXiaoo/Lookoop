import java.io.Serializable;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.text.MessageFormat;


// https://www.cnblogs.com/xdp-gacl/p/3777987.html

class Person implements Serializable {

    // 序​列​化​的​版​本​号​，凡是实现Serializable接口的类都有一个表示序列化版本标识符的静态变量
    private static final long serialVersionUID = -580978257827294399L;

    private int age;
    private String name;
    private String sex;

    // private String info;    // 新添加一个属性, 如果没有序列化版本号，新添加属性后反序列化原有对象会报错

    public int getAge() {
        return age;
    }

    public String getName() {
        return name;
    }

    public String getSex() {
        return sex;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }
}

public class SerializableDemo {
    private static void serialize(String fileOuputPath) throws FileNotFoundException, IOException {
        Person person = new Person();
        person.setName("bob");
        person.setAge(24);
        person.setSex("male");

        // 序列化
        ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(new File(fileOuputPath)));
        oos.writeObject(person);
        System.out.println("serialize successful!");
        oos.close();
    }

    private static Person deSerialize(String filePath) throws Exception, IOException {
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream(new File(filePath)));

        Person person = (Person) ois.readObject();
        System.out.println("deserialize successful!");
        return person;
    }

    public static void main(String[] args) throws Exception {
        String fileOuputPath = "C:\\Study\\github\\Lookoops\\java\\笔记\\java-深入学习\\序列化\\serializable.txt";

        serialize(fileOuputPath);
        Person person = deSerialize(fileOuputPath);

        System.out.println(MessageFormat.format("name={0}, age={1}, sex={2}.",person.getName(), person.getAge(), person.getSex()));

    }
}