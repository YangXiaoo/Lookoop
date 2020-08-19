# VUE部分
- 打包前在config/index.js中进行打包设置
```javascript
  build: {
    // Template for index.html
    index: path.resolve(__dirname, '../dist/templates/index.html'),	// 更改

    // Paths
    assetsRoot: path.resolve(__dirname, '../dist'),
 	}
````
- 项目打包：npm run build

# springboot
- 使用thymeleaf模板
- 访问静态文件配置
```java
@Configuration
public class MvcConfig extends WebMvcConfigurationSupport {
    @Override
    protected void addResourceHandlers(ResourceHandlerRegistry registry) {
        registry.addResourceHandler("/static/**").addResourceLocations("classpath:/static/");
//        registry.addResourceHandler("/templates/**").addResourceLocations("classpath:/templates/");
    }
}
```
- 将vue/dist中的static和templates目录复制到springboot项目中的resources中
- controller层添加访问`index.html`接口
```java
@Controller
public class IndexController {

    @RequestMapping("/index")
    public String index() {
        return "/index";
    }

}
```