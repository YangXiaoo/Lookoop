<?php 
/**
 * 接口
 */
 interface hash{
 	function _hash($str);
 }
 interface distribution{
 	public function lookup($key);
 }