import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
 
/*实现JDBC连接MySql
 * 步骤：
 * 1.加载数据驱动
 * 2.获取数据库的连接
 * 3.创建语句对象
 * 4.获得数据集
 * 5.遍历数据集
 * 6.关闭数据，释放资源
 * 
 * */
public class JDBCMySql {
    public static void main(String[] args) {
        //1.加载驱动
        Connection conn = null;     //连接对象
        Statement stmt = null;      //语句对象
        ResultSet result = null;    //结果集（数据集）对象
        String url = "jdbc:mysql://localhost:3306/bbs?useUnicode=true&characterEncoding=UTF-8";
        String username = "root";       //数据库用户名
        String password = "Ab127000";   //数据库密码
        String driver = "com.mysql.jdbc.Driver";
        try {
            Class.forName(driver);
            //2.获得数据库连接
            conn = DriverManager.getConnection(url,username,password);
            //3.创建语句对象
            stmt = conn.createStatement();
            String sql = "select * from user";
            //4.获取数据集
            result = stmt.executeQuery(sql);
            //5.遍历数据集
            while(result.next()){
                System.out.println(result.getInt("id")+"-"+result.getString("name")+"-"+result.getString("password")+"-"+result.getInt("age")+"-"+result.getString("address"));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }finally{
            //6.释放资源
            try {
                if(result != null){
                    result.close();
                    result = null;
                }
                if(stmt != null){
                    stmt.close();
                    stmt = null;
                }
                if(conn != null){
                    conn.close();
                    conn = null;
                }
            } catch (Exception e2) {
                e2.printStackTrace();
            }
        }
    }
}