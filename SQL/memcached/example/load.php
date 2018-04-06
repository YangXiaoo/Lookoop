<?php
/** 
 * 获取服务池信息
 */

require('./config.php');

$get = 0;
$hits = 0;
$mem = new Memcached();

foreach ($ser as $s) {
    $mem->addServer($s['host'],$s['port']);
    $info = $mem->getStats();
    //$info打印出来一个端口有多个服务池信息，原因暂时未找到
    foreach ($info as $k => $v) {
    $get += $v['cmd_set'];
    $hits += $v['get_hits']; 
	}
    $mem->quit();
}
if ($get == 0) {
	echo 1;
}else{
	echo $hits/$get;
}