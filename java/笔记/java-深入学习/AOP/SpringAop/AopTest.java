
public class AopTest {

    @Test
    @SuppressWarnings("resource")
    public void testAop() {
        ApplicationContext ac = new ClassPathXmlApplicationContext("spring/aop.xml");
        
        Dao dao = (Dao)ac.getBean("daoImpl");
        dao.insert();
        System.out.println("----------分割线----------");
        dao.delete();
        System.out.println("----------分割线----------");
        dao.update();
    }
    
}