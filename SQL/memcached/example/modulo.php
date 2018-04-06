<?php
/**
 * 取模算法
 * @date(2018-4-5)
 */

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

 	public function addNode($server){
 		$this->_ser[] = $server;
 		$this->_num += 1;
 	}

 	public function deleNode($server){
 		foreach ($this->_ser as $k => $v) {
 			if ($v == $server) {
 				unset($this->_ser[$k]);
 			}
 		}

 		$this->_num -= 1;
 		$this->_ser = array_merge($this->_ser); //保持键的连续
 	}
 }
/*
$moder = new Moder();
$moder->addNode('a');
$moder->addNode('b');
$moder->addNode('c');
$moder->addNode('d');
echo '<h2>取模算法</h2>';
for($i=1; $i <= 100; $i++){
	$key = 'key_'.$i;
	echo $key,'--->',$moder->lookup($key),"\n","<br>";
}
*/
