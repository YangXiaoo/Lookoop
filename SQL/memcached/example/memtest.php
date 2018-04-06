<?php
$dbhost = 'localhost:3306';  // mysql服务器主机地址
$dbuser = 'root';            // mysql用户名
$dbpass = 'Ab127000';          // mysql用户名密码
$conn = mysqli_connect($dbhost, $dbuser, $dbpass);
if(! $conn )
{
    die('Could not connect: ' . mysqli_error());
}
echo '数据库连接成功！<br>';
mysqli_select_db($conn,'test');					
mysqli_query("set names utf8");

$mem = new Memcached();  
$mem->addServer('localhost', '11211'); 

$goods = $mem->get('goods');
if (empty($goods)) {
	$sql = mysqli_query($conn,"select * from my_goods");
    $goods = mysqli_fetch_array($sql, MYSQLI_ASSOC);
    $mem->set('goods', $goods,10); //10s缓存时间
    echo "data from mysql;<br>";
}else{
	echo "data from memcached;<br>";
}
print_r($goods);
mysqli_close($conn);
$mem->quit();
?>

