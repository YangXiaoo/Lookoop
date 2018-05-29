#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
CREATE TABLE `dy_count` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `count` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8
'''
import unittest
from selenium import webdriver
from bs4 import BeautifulSoup
import MySQLdb

class douyuSelenium(unittest.TestCase):
    # 初始化方法
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.counts = 0

        db_host = '127.0.0.1'
        db_name = 'ssh'
        user_name = 'root'
        pass_word = 'Ab127000'
        self.tablename = 'dy_count'
        char_set = 'utf8'
        self.db = MySQLdb.connect(db_host, user_name, pass_word, db_name, charset=char_set)
        self.cursor = self.db.cursor()

    #具体的测试用例方法，一定要以test开头
    def testDouyu(self):
        self.driver.get('http://www.douyu.com/directory/all')
        while True:
            soup = BeautifulSoup(self.driver.page_source, 'xml')
            titles = soup.find_all('h3', {'class': 'ellipsis'})
            nums = soup.find_all('span', {'class': 'dy-num fr'})

            # 使用zip()函数来可以把列表合并，并创建一个元组对的列表[(1,2), (3,4)]
            for num, title in zip(nums, titles):
                #sql = ''INSERT INTO dy_count(title,count)VALUES('%s','%s')'' % (title.get_text().strip(),num.get_text())
                try:
                    self.cursor.execute('INSERT INTO dy_count(title,count)VALUES("%s","%s")' % (title.get_text().strip(),num.get_text().strip()))
                    self.db.commit()
                except:
                    self.db.rollback()
                    print 'Something wrong..., please check...'
                print u"观众人数:" + num.get_text().strip(), u"\t房间标题: " + title.get_text().strip()

            # page_source.find()未找到内容则返回-1
            if self.driver.page_source.find('shark-pager-disable-next') != -1:
                break

            # 模拟下一页点击           
            if self.counts <= 5:
                self.counts += 1
                self.driver.find_element_by_class_name('shark-pager-next').click()
            else:
                self.db.close()
                break
            

    # 退出时的清理方法
    def tearDown(self):
        print u"加载完成..."
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
