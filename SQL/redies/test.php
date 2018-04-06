<?php
/**
 * @todo redis连接测试
 * @date( 2018-4-6)
 * @author  yangxiao 
 */
$redis = new Redis(); 
$redis->connect('localhost','6379');
$redis->select(0);

$redis->set('test','ok');
if (!empty($redis->get('test'))) {
    echo 'yes it works!!!',"<br>";
}           
echo "下面为Reids的常量和方法<br>";
$ref = new ReflectionClass('Redis');

//返回所有常量名和值
$consts = $ref->getConstants(); 
echo "----------------consts:---------------<br>";
foreach ($consts as $key => $val)
{
  echo "$key : $val" ,"<br>";
}

//返回类中所有方法
$methods = $ref->getMethods();   
echo "-----------------methods,total",sizeof($methods),":---------------<br>";
foreach ($methods as $method)
{
  echo $method->getName(),"<br>";
}
?>
