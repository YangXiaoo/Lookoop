<?php
/**
 * @todo   单例
 * 这个类只能创造一个对象。
 * 
 * 目的：通过类创建的对象永远是一个类，多个new实例化时产生的对象不同。
 * 		 使用单例模式可以避免大量new的操作浪费资源。
 *
 * 步骤： 1. 构造函数需要标记为private
 * 		  2. 保存类实例的静态成员变量
 * 		  3. 获取实例的公共静态方法
 *
 * private,protected,public 自己的,父亲的,大众的
 *由于静态方法不需要通过对象即可调用，所以伪变量 $this 
 *在静态方法中不可用。静态属性不可以由对象通过 -> 操作符来访问
 *
 * 1.static 放在函数内部修饰变量
 * 2.static放在类里修饰属性，或方法
 * 3.static放在类的方法里修饰变量
 * 4.static修饰在全局作用域的变量
 * 
 */
class Dog {
	private function _construct(){
		//静态属性保存单例对象
		static private $instance;
		static public function GetInstance(){
			//判别是否为空
			if (!self::$instance) {
				self::$instance = new self();
			}
			return self::$instance;
		}
	}

	$dog1 = Dog::GetInstance();
	$dog2 = Dog::GetInstance();

	if ($dog1 === $dog2) {
		echo '同一个对象';
	}else{
		echo '不同对象';
	}
}
//输出：“同一个对象”
<?php
class Person {
    var $name;
    var $age;

    //定义一个构造方法初始化赋值
    function __construct($name,  $age) {
        $this->name=$name;
        $this->age=$age;
    }

    function say() {
        echo "我的名字叫：".$this->name."<br />";
		echo "我的年龄是：".$this->age;
    }
}

$p1=new Person("张三", 20);
$p1->say();
?>