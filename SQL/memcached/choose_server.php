<?php
 interface hash{
 	function _hash($str);
 }
 interface distribution{
 	public function lookup($key);
 }

 class Moder implements hash,distribution {
 	protected $_ser = [];
 	protected $_num = 0;

 	public function _hash($str){
 		$number = sprintf('%u', crc32($str));
 		return $number;
 	}

 	public function lookup($key){
 		$index = $this->_hash($key) % $this->_num;
 		return $this->_ser[$index];
 	}

 	public function addServer($server){
 		$this->_ser[] = $server;
 		$this->_num += 1;
 	}

 	public function deleServer($server){
 		foreach ($this->_ser as $k => $v) {
 			if ($v == $server) {
 				unset($this->_ser[$k]);
 			}
 		}

 		$this->_num -= 1;
 		$this->_ser = array_merge($this->_ser);
 	}
 }

$moder = new Moder();
$moder->addServer('a');
$moder->addServer('b');
$moder->addServer('c');
$moder->addServer('d');

for($i=1; $i <= 100; $i++){
	$key = 'key_'.$i;
	echo $key,'--->',$moder->lookup($key),"\n","<br>";
}

<?php
/**
 * date(2018-4-4)
 * @author yangxiao
 * @todo  一致性哈希的实现
 */
 interface hash{
 	function _hash($str);
 }
 interface distribution{
 	public function lookup($key);
 }

class Cons implements hasher,distribution{
	protected $nodes = [];  //节点
	protected $points = []; //对应虚拟节点
	protected $_mul = 64;   //每个节点对应的虚拟节点
 	public function _hash($str){
 		$number = sprintf('%u', crc32($str));
 		return $number;
 	}

 	public function lookup($key){
 		$position = $this->_hash($key); //算出键在圆环上的位置
 		$needle = key($this->points);
 		foreach ($this->points as $p) {
 			if ($p >= $position) {
 				$needle = $p;
 				break;
 			}
 		}
 		return $this->points[$needle];
 	}	

 	public function addNode($node){
 		$this->nodes[$node] = [];
 		for($i = 0; $i < $this->_mul; $i++){
 			$point = $node.'_'.$i; //每个节点的虚拟点,可修改此处增加随机性
 			$point = $this->_hash($point);  //虚拟节点转成数字
 			$this->points[$point] = $node;  //虚拟节点指向实际节点
 			$this->nodes[$node][] = $point; //实际节点指向虚拟节点

 			ksort($this->points); //对虚拟节点排序
 		}
 	}

 	public function delNode($node){
 		foreach ($this->nodes[$node] as $v) {
 			unset($this->points[$v]); //删除虚拟节点对应实际节点
 		}
 		unset($this->nodes[$node]);  //删除实际节点
 	}
}

$cons = new Cons();
$cons->addNode('A');
$cons->addNode('B');
$cons->addNode('C');
$cons->addNode('D');

print_r($cons);