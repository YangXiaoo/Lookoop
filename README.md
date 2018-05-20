
<?php
/**
*@todo introduction
*@date 2018-3-18
*@method 观察者模式
*/
class YangXiao
{
  protected $You = [];
  function addYou($You)
  {
    $this->You[] = $You;
  }
    function delYou($You)
  {
    $key = array_search($You, $this->You);
    array_splice($this->You, $key, 1);
  }
  function  StudyPhp()
  {
    echo 'php学习笔记';
  }
  function StudyLinux ()
  {
    echo 'Linux学习笔记';
  }
  function StudyJavaScript ()
  {
    echo 'JavaScript学习笔记';
  }
  foreach ($this->You as Chinese)
  {
    $Chinese->study();
  }
}
class Others
{
  function study()
  {
    echo '来看看吧'；
  }
}

$yangxiaoo = new YangXiao();
$SomeOne = new Others();

$yangxiao0->addYou($SomeOne);
$yangxia0o->StudyPhp();
$yangxiao0->StudyLinux();
$yangxiaoo->StudyJavaScript();

if(You_are_going_to_leave)
{
  $yangxiaoo->delYou($SomeOne);
} 
?>
 
