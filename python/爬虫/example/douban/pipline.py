# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import json


class MyscrapyPipeline(object):
	def __init__(self):
		db_host = '127.0.0.1'
		db_name = 'scrapy'
		user_name = 'root'
		pass_word = 'Ab127000'
		self.tablename = 'db_movie'
		char_set = 'utf8'

		self.db = MySQLdb.connect(db_host, user_name, pass_word, db_name,charset=char_set)
		self.cursor = db.cursor()

		self.file = codecs.open('movie.json','w',encoding='utf8')

	def process_item(self, item, spider):
		#写入数据库
		self.cursor.execute('insert into db_movie(title,content,score,ratetotal,info)values(%s,%s,%s,%s,%s)',(item['title'],item['content'],item['score'],item['ratetotal'],item['info']))
		#写入文件
		content = json.dumps(dict(item), ensure_ascii=False) + "\n"
		self.file.write(content)
		return item

