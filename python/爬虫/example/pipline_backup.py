pipline_backup.py# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import json
from scrapy.conf import settings

class MyscrapyPipeline(object):
	def __init__(self):
		db_host = settings['MYSQL_HOST']
		db_name = settings['MYSQL_DB']
		user_name = settings['MYSQL_USER']
		pass_word = settings['MYSQL_PASSWD']
		self.tablename = settings['MYSQL_TABLENAME']
		char_set = settings['MYSQL_CHARSET']
		self.dbpool = adbapi.ConnectionPool(
			"MySQLdb",
			host = db_host,
			db = db_name,
			user = user_name,
			passwd = pass_word,
			cursorclass = MySQLdb.cursors.DictCursor,
			charset = char_set,
			use_unicode = False
			)
		self.file = codecs.open('movie.json','w',encoding='utf8')

	def process_item(self, item, spider):
		#写入数据库
		res = self.dbpool.runInteraction(self.insert_into_table,item)
		#写入文件
		content = json.dumps(dict(item), ensure_ascii=False) + "\n"
		self.file.write(content)
		return item

	def insert_into_table(self, conn, item):
		conn.execute('insert into db_movie(title,content,score,ratetotal,info)values(%s,%s,%s,%s,%s)',(item['title'],item['content'],item['score'],item['ratetotal'],item['info']))



