<?php
$mem = new Memcached;            
$mem->connect('localhost', 11211) or die ("Could not connect memcached"); 

$conn = mysql_connect("localhost","root","Ab127000");	
mysql_select_db("test",$conn);					
mysql_query("set names utf8");


$goods = $mem->get('goods')
if (!$goods) {
	$search = "select * from my_goods";
	$sql = mysql_query($search, $conn);
    $result = mysql_fetch_array($sql);
    $mem->set('goods', $result);
    echo "form mysql";
}else{
	echo "from memcached";
}
?>
