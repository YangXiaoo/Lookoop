<?php
/**
 * @todo  工厂
 *
 * 创建对象参数传递的可变性
 */
interface Skill{
	function guitar();
	function ANSYS();
}

class HE implements Skill{
	function guitar(){
		echo '我会弹吉他';
	}
	function ANSYS(){
		echo '我会ANSYS WORKBENCH';
	}
}

class Young implements Skill{
	function guitar(){
		echo '我Bu会弹吉他';
	}
	function ANSYS(){
		echo '我Bu会ANSYS WORKBENCH';
	}
}

class Factory{
	static function Who($type){
		swith ($type){
			case 'HE':
				return new Person();
			break;
			case 'Young':
				return new Young();
			break;
		}
	}
}

$me = Factory::Who('HE');
$other = Factory::Who('Young');