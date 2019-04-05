package online.yangxiao.service.impl;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import online.yangxiao.dao.UserMapper;
import online.yangxiao.entity.User;
import online.yangxiao.service.UserService;

// 2019-4-5
@Service
public class UserServiceImpl implements UserService{
    @Autowired
    private UserMapper userMapper;

    @Transactional
    public int regist(User user) {
        int i = userMapper.insert(user);
        // i = i / 0;  // 测试事物回滚效果
        return i;
    }

    public User loginByEmail(String email, String password) {
        User user = new User();
        user.setEmail(email);
        return userMapper.selectOne(user);
    }

    public User findByEmail(String email) {
        User user = new User();
        user.setEmail(email);
        return userMapper.selectOne(user);
    }

    @Override
    public User findById(Integer id) {
        User user = new User();
        user.setId(id);
        return userMapper.selectOne(user);
    }

    public User findById(String id) {
        User user = new User();
        Integer uid = Integer.parseInt(id);
        user.setId(uid);
        return userMapper.selectOne(user);
    }

    @Transactional
    public void deleteByEmail(String email) {
        User user = new User();
        user.setEmail(email);
        userMapper.delete(user);
    }

    @Transactional
    public void deleteByEmailAndFalse(String email) {
        User user = new User();
        user.setEmail(email);
        userMapper.delete(user);
    }

    @Transactional
    public void update(User user) {
        userMapper.updateByPrimaryKeySelective(user);
    }
}
