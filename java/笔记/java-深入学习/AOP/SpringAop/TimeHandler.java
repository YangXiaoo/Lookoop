
public class TimeHandler {
    
    public void printTime(ProceedingJoinPoint pjp) {
        Signature signature = pjp.getSignature();
        if (signature instanceof MethodSignature) {
            MethodSignature methodSignature = (MethodSignature)signature;
            Method method = methodSignature.getMethod();
            System.out.println(method.getName() + "()方法开始时间：" + System.currentTimeMillis());
            
            try {
                pjp.proceed();
                System.out.println(method.getName() + "()方法结束时间：" + System.currentTimeMillis());
            } catch (Throwable e) {
                
            }
        }
    }
    
}