package online.yangxiao.service;

import online.yangxiao.entity.User;

public interface UserService {
    /**
     * 用户注册
     * @param user
     * @return
     */
    int regist(User user);

    /**
     * 根据邮箱登录
     * @param email
     * @param password
     * @return
     */
    User loginByEmail(String email, String password);

    /**
     * 根据邮箱查询用户
     * @param email
     * @return
     */
    User findByEmail(String email);

    /**
     * 根据用户id查询用户
     * @param id
     * @return
     */
    User findById(Integer id);

    /**
     * 根据用户邮箱删除用户
     * @param email
     */
    void deleteByEmail(String email);

    /**
     * 更新用户信息
     * @param user
     */
    void update(User user);
}
