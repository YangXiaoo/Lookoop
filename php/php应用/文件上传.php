<?php
/**
 * @data(2018-3-24)
 * 成员属性
 * 			文件上传路径
 * 			文件上传后缀
 * 			文件上传mime
 * 			文件上传size
 * 			是否启用随机名
 * 			加上文件前缀
 * 		自定义的错误号码和错误信息
 * 		要保存的文件类型
 * 			文件名
 * 			文件后缀
 * 			文件大小
 * 			文件Mime
 * 			文件临时路径
 * 			文件新名
 *
 * 对外公开方法
 * 		uploadFile()；上传成功返回路径，上传失败返回false
 */
$up = new Upload();
$up->UploadFile('fm');

//检测
var_dump($this->errorNumber);
var_dump($this->errorInfo);


class Upload{
	protected $path = './upload';//文件上传保存路径
	protected $allowSuffix = ['jpg', 'jpeg', 'gif', 'wbmp', 'png'];
	protected $allowMime = ['image/jpeg', 'image/gif', 'image/wbmp', 'image/png'];
	protected $maxSize = 2000000;//2M
	protected $isRandName = true;
	protected $prefix = 'up';

	//自定义的错误号码和错误信息
	protected $errorNumber;
	protected $errorInfo;

	//文件信息
	protected $oldName;
	protected $suffix;
	protected $size;
	protected $mime;
	protected $tempName;
	protected $newName;
	public function __construct($arr = []){
		foreach ($arr as $key => $value) {
			$this->setOption($key, $value);
		}
	}
	protected function setOption($key, $value){
		$keys = array_keys(get_class_vars(__CLASS__));//get_class_vars(__CLASS__)全局属性名称
		//get_class_vars() performed within a class can access any public, protected, and private members.
		if (in_array($key, $keys)) {
			$this->$key = $value;//$var = 2;
		}
	}
	//$key input框中name的属性值文件名称
	public function UploadFile($key){
		//判断有没有设置路径 path
		if (empty($this->path)) {
			$this->setOption('errorNumber', -1);
			return false;
		}
		//判断该路径是否存在，是否可写
		if (!this->check()) {
			$this->setOption('errorNumber',-2);
			return false;
		}
		//判断$_FILES里面的erro信息是否为0，若为0则文件信息在服务器上可以直接获取，提取信息保存到成员属性
		$error = $_FILES[$key]['error'];
		if ($error) {
			$this->setOption('errorNumber', $error);
			return false;
		}else{
			//提取信息并保存到成员属性
			$this->getFileInfo($key);
		}

		//判断文件的大小，Mime,后缀
		if (!$this->checkSize() || !$this->checkMime() || !$this->checkSuffix()) {
			return false;
		}
		
		//得到新的名字
		$this->newName = $this->createNewName();


		//判断是否是上传文件，并且移动上传文件
		if (is_uploaded_file($this->tempName)) {
				if (move_uploaded_file($this->tempName, $this->path.$this->newName)) {
					return $this->path.$this->newName;
				}else{
					$this->setOption('errorNumber', -7);
					return false;
				}
		}else{
			$this->setOption('errorNumber', -6);
			return false;
		}

	}

	protected function check(){
		//文件夹不存在或不是目录，创建文件夹
		if (!file_exists($this->path) || !is_dir($this->path)) {
			return mkdir($this->path, 0777, true);
		}
		if (!is_writable($this->path)) {
			return chmod($this->path, 0777);
		}
		return true;
	}
	protected function getFileInfo($key){
		$this->oldName = $_FILES[$key]['name'];
		$this->mime = $_FILES[$key]['type'];
		$this->tempName = $_FILES[$key]['ymp_name'];
		$this->size = $_FILES[$key]['size'];
		$this->suffix = pathinfo($this->oldName)['extension'];
	}

	protected function checkSize(){
		if ($this->size > $this->maxSize) {
			$this->setOption('errorNumber', -3);
			return false;
		}
		return true;
	}

	protected function checkMime(){
		if (!in_array($this->mime, $this->allowMime)) {
			$this->setOption('errorNumber', -4);
			return false;
		}
		return true;
	}

	protected function checkSuffix(){
		if (!in_array($this->suffix, $this->allowSuffix)) {
			$this->setOption('errorNumber', -5);
			return false;
		}
		return true;
	}

//得到新的名字
	protected function createNewName(){
		if ($this->isRandName) {
			$name = $this->prefix.uniqid().'.'.$this->suffix;
		}else{
			$name = $this->prefix.$this->oldName;
		}
		return $name;
	}

	//获得上传错误信息
	public fucntion __get($name){
		if ($name == 'errorNumber') {
			return $this->errorNumber;
		}else if ($name == 'errorInfo') {
			return $this->getErrorInfo();
		}
	}

	protected function getErrorInfo(){
		switch ($this->errorNumber) {
			case '-1':
				$str = '文件路径没有设置';
				break;
			case '-2':
				$str = '文件路径不是目录或没有权限';
				break;
			case '-3':
				$str = '文件大小超过指定范围';
				break;
			case '-4':
				$str = '文件类型不符合';
				break;
			case '-5':
				$str = '文件后缀不符合';
				break;
			case '-6':
				$str = '不是上传文件';
				break;
			case '-7':
				$str = '文件上传失败';
				break;
			case '1':
				$str = '文件超出php.ini设置大小';
				break;
			case '2':
				$str = '文件超出html设置大小';
				break;
			case '3':
				$str = '文件只上传了一部分';
				break;
			case '4':
				$str = '没有文件上传';
				break;
			case '6':
				$str = '找不到临时文件';
				break;
			case '7':
				$str = '文件写入失败';
				break;
		}
	}
}