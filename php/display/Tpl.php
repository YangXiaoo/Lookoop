<?php
/**
 * 正则替换
 * 			preg_replace($patten, $replace, $str);
 * 			preg_quote：定界符,原子，元字符，模式修正符
 * 			preg_repalce_callback($patten, callback, $str);
 * include
 * 			(include xxx.html)
 * 			<?php include xxx.php; ?>
 */
class Tpl
{
	//模板文件的路径
	protected $viewDir = './view';
	//生成缓存文件的路径
	protected $cacheDir = './cache/';
	//过期时间
	protected $lifeTime = 3600;
	//用来存放显示变量的数组
	protected $vsrs = [];
	//有成员变量就要有构造方法
	function _construct($viewDir = null, $cacheDir = null, $lifeTime = null){
		//若为空使用默认值，若不为空设置
		if (!empty($viewDir)) {
			//判断路径是否正确
			if ($this->checkDir($viewDir)) {
				$this->viewDir = $viewDir;
			}
		}
		if (!empty($cacheDir)) {
			if ($this->checkDir($cacheDir)) {
				$this->cacheDir = $cacheDir;
			}
		}
		if (!empty($lifeTime)) {
			$this->lifeTime = $lifeTime;
		}
	}

/**
 * @todo 判断目录路径是否正确
 */
	protected function checkDir($dirPath){
		if (!file_exists($dirPath) || is_dir($dirPath)) {
			return mkdir($dirPath, 0755, true);
		}
		//判断目录是否可读写
		if (!is_writable($dirPath) || !is_readable($dirPath)) {
			return chmod($dirPath, 0755);
		}
	}


	//需要对外公开的方法
	//1.分配变量的方法
	//$title = 'yangxiao'; $tpl->assign('title', $title);
	function assign($name, $value){
		$this->vars[$name] = $value;
	}
	//2.展示缓存文件的方法
	//$isInclude：模板文件是仅仅需要编译还是先编译再包含 
	//$uri：index.php?page=1,为了让缓存的文件名不重复，将文件名和uri拼接起来再md5一下，生成缓存的文件名
	function dispaly($viewName, $isInclude = true, $uri = null){
		//拼接模板文件的全路径
		//rtrim() 函数移除字符串右侧的空白字符或其他预定义字符
		$viewPath = rtrim($this->viewDir,'/').'/'.$viewName;
		if (!file_exists($viewPath)) {
			die('模板文件不存在');
		}
		//拼接缓存文件的全路径
		$cacheName = md5($viewName.$uri).'.php';
		$cachePath = rtrim($this->cacheDir,'/').'/'.$cacheName;
		if (!file_exists($cachePath)) {
			//编译模板文件
			$php = $this->compile($viewPath);
			//写入文件，生成缓存文件
			file_put_contents($cachePath, $php);
		}else{
		//根据缓存文件全路径，判断缓存文件是否存在
		//若缓存文件不存在，编译模板文件生成缓存文件
		//若缓存文件存在，第一，判断缓存文件是否过期，第二，判断模板文件是否被修改过，如果模板文件被修改过，缓存文件需要重新生成
		$isTimeout = (filectime($cachePath) + $this->lifeTime) > time() ? false:true;//filectime()函数返回文件上次 inode 被修改的时间。如果出错则返回 false。时间以 Unix 时间戳的方式返回
		$isChange = filemtime($viewPath) > filemtime($cachePath) ? true : false;//filemtime() 函数返回文件内容上次的修改时间。
		//缓存文件重新生成
		if ($isTimeout || $isChange) {
			$php = $this->compile($viewPath);
			file_put_contents($cachePath, $php);
		}
		}

		//判断缓存文件是否需要包含进来
		if ($isInclude) {
			//将变量解析出来
			extract($this->vars);
			include $cachePath;
		}
	}
}