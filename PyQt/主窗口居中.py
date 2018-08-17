# -*- coding: utf-8
# 2018-8-17
# 创建主窗口 + 关闭主窗口
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QHBoxLayout, QPushButton, QWidget 
from PyQt5.QtGui import QIcon

class Winform(QMainWindow):
	"""docstring for Winform"""
	def __init__(self, parent=None):
		super(Winform, self).__init__(parent)

		self.setWindowTitle("test")
		self.button1 = QPushButton("click to close")
		self.button1.move(10,10)
		self.button1.clicked.connect(self.onclick) # onclik() 函数被称为槽函数

		layout = QHBoxLayout()
		layout.addWidget(self.button1)

		main_fram = QWidget()
		main_fram.setLayout(layout)
		self.setCentralWidget(main_fram)
		self.resize(370, 250)
		# self.center()

	def center(self):
		screen = QDesktopWidget().screenGeometry()
		size = self.geometry() # 继承于QMainWindow
		# print(size, screen.width(), screen.height()) # (0, 0, 370, 250) 1920 1080
		self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

	def onclick(self):
		sender = self.sender() # 发送信号对象
		print(sender.text(),"clicked")
		ap = QApplication.instance()
		ap.quit()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = Winform()
	win.show()
	sys.exit(app.exec_())
