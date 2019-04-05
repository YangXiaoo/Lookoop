package online.yangxiao.dao;

import online.yangxiao.entity.Upvote;

public interface UpvoteMapper {
    int deleteByPrimaryKey(Integer id);

    int insert(Upvote record);

    int insertSelective(Upvote record);

    Upvote selectByPrimaryKey(Integer id);

    int updateByPrimaryKeySelective(Upvote record);

    int updateByPrimaryKey(Upvote record);
}