<?php 
/**
 * 测试数据
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
$i = 0;
while(true){
	$i += 1;
	$key = ($i % 1000) + 1;//1-1000之间

	$key = 'key_'.$key;
	$num = $diser->lookup($key);

	$mem->addServer($ser[$num]['host'],$ser[$num]['port']); 
	if (! $mem->get($key)) {
		$mem->add($key, 'val_'.$i);
	}
	$mem->quit();
	usleep(20000);
}