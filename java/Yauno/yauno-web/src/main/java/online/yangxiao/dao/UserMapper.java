package online.yangxiao.dao;

import tk.mybatis.mapper.common.Mapper;
import online.yangxiao.entity.User;

public interface UserMapper {
    int deleteByPrimaryKey(Integer id);

    void delete(User user);

    int insert(User record);

    int insertSelective(User record);

    User selectByPrimaryKey(Integer id);

    User selectOne(User user);

    int updateByPrimaryKeySelective(User record);

    int updateByPrimaryKey(User record);
}