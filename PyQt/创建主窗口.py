# 2018-8-17
# 创建主窗口
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon, QFont # 富文本

class MainWindow(QMainWindow):
	def __init__(self,parent=None):
		super(MainWindow,self).__init__(parent)
		self.resize(400, 200)
		self.status = self.statusBar()
		self.status.showMessage("this is status bar")
		self.setWindowTitle("MainWindow test!")
		self.initui()

	def initui(self):
		QToolTip.setFont(QFont('sansSerif', 10))
		self.setToolTip("这是一个<b>气泡</b>提示")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	app.setWindowIcon(QIcon("yx.png"))
	form = MainWindow()
	form.show() # 显示该窗口
	sys.exit(app.exec_())