// 2019-4-30

RequestParam
	// get或post请求链接后面带参数如:www.yangxiao.online?id=3
	@RequestParam(name="id", required=false, defaultValue="0")	// required 参数不一定永远存在
																// defaultValue 可以省略

// #################################
Model model
	model.addAttribute("error", "something error!");	// 向模板中的error添加值
	return "../index";	// 带参数返回模板

// ################################# 
@ResponseBody   
    // @responseBody注解的作用是将controller的方法返回的对象通过适当的转换器转换为指定的格式之后，写入到response对象的body区，通常用来返回JSON数据或者是XML

// ################################# 
@Autowired
	// https://www.cnblogs.com/caoyc/p/5626365.html

// ################################
mysql生成dao,entity实体
// https://blog.csdn.net/qq_26755717/article/details/82254429

// ###############################\
过滤器和拦截器
// https://www.cnblogs.com/junzi2099/p/8022058.html 

// ####################
// 自己写SQL语句
import org.apache.ibatis.annotations.*;
public interface CategoryMapper extends Mapper<Category>{
	String TABLE_NAME = "category";

	// 删除
	@Delete({"DELETE FROM",TABLE_NAME, "WHERE id=#{cid}"})
	int deleteCateById(@Param("cid") Integer cid);
}


// ###########
MyBaits配置
// https://www.cnblogs.com/kaiwen/p/6440793.html

// ################
Session // https://blog.csdn.net/z_xuewen/article/details/77985897
Cookie // https://blog.csdn.net/u011848397/article/details/52201339

@ContextConfiguration: 加载配置文件 

// 启动redis