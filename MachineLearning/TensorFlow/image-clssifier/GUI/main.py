# coding:utf-8
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Main(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("骨龄预测")
		self.resize(700, 500)
		bar = self.menuBar()
		file = bar.addMenu("File")
		file.addAction("New")
		save = QAction("Save",self)
		save.setShortcut("Ctrl+S")
		file.addAction(save)
		edit = file.addMenu("Edit")
		edit.addAction("copy")
		edit.addAction("paste")
		quit = QAction("Quit",self)
		file.addAction(quit)
		file.triggered[QAction].connect(self.processtrigger) 
		
		self.initMainWindow()

	def initMainWindow(self):
		widget = QWidget()

		hlayout =  QHBoxLayout(self)
		vlayout =  QVBoxLayout(self)
		glayout = QGridLayout(self)

		self.compute = QPushButton("计算")
		self.reset = QPushButton("重置")
		hlayout.addWidget(self.compute)
		hlayout.addWidget(self.reset)

		self.loadPic = QPushButton("加载图片")
		self.loadPic.clicked.connect(self.getfile)
		hlayout.addWidget(self.loadPic)
		self.showPic = QLabel("")

		glayout.addWidget(self.loadPic, 0, 0)
		glayout.addWidget(self.compute, 1, 0)
		glayout.addWidget(self.reset, 1, 1)

		glayout.addWidget(self.showPic, 0, 2)

		widget.setLayout(glayout)
		self.setCentralWidget(widget)


		
	def processtrigger(self,q):
		print( q.text()+" is triggered" )

	def getfile(self):
		fname, _  = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg *.gif)")
		self.showPic.setPixmap(QPixmap(fname))

if __name__ == '__main__':
	app = QApplication(sys.argv)
	main = Main()
	main.show()
	sys.exit(app.exec_())
