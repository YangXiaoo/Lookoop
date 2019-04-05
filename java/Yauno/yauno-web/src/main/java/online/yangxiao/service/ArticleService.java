package online.yangxiao.service;

import online.yangxiao.entity.Article;
import online.yangxiao.entity.Comment;
import online.yangxiao.common.PageHelper;

import java.util.List;

public interface ArticleService {
    /**
     * 查询所有Content并分页
     * @param content
     * @param pageNum
     * @param pageSize
     * @return
     */
    PageHelper.Page<Article>  findAll(Article content, Integer pageNum, Integer pageSize);
    PageHelper.Page<Article>  findAll(Article content, Comment comment, Integer pageNum, Integer pageSize);
    PageHelper.Page<Article>  findAllByUpvote(Article content, Integer pageNum, Integer pageSize);
}
