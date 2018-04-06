<?php 
/**
 * 初始化数据
 * @date(2018-4-5)
 * @author yangxiao
 */
require('./config.php');
require('./interface.php');
require('./modulo.php');
require('./cons.php');

$diser = new $cons;
$mem = new Memcached();

foreach ($ser as $s => $v) {
    $diser->addNode($s);
}
for ($i = 1; $i <= 1000; $i++){
	$key = 'key_'.$i;
	$val = 'val_'.$i;
	$num = $diser->lookup($key); 
	$mem->addServer($ser[$num]['host'],$ser[$num]['port']);
	$mem->add($key, $val);
	$mem->quit();
}
echo "ok;<br>";