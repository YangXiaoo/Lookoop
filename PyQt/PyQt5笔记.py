# 2018-8-17
# 参考书籍： PyQt5


QMainWindow:包含菜单栏，工具栏，状态栏，标题栏。GUI程序的主窗口
QDialog: 对话框的基类，可以是模态也可以是非模态。没有菜单栏工具栏...
QWidget: 主窗口用QMainWindow,对话框用QDialog,如果不确定，或者可能作为顶层窗口(没有父窗口的窗口)，也有可能嵌入到其它窗口，那么就用QWidget
父窗口：一个窗口包含一个或多个窗口，则称该窗口为父窗口。

QMainWindow继承于QWidget,其 比较重要的方法：
addToolBar()
centralWidget() # 返回窗口中心的一个控件
menuBar() # 返回主窗口的菜单栏
setCentralWidget() # 设置窗口的中心控件
setStatusBar() # 设置状态栏
statusBar() # 获得状态栏对象后，通过状态栏对象的showMessage(m,essage, int timeout=0)方法现实状态栏信息。第一个参数状态栏信息，第二个参数为信息停留时间，单位为毫秒，默认为0，表示一直显示
QMainWindow不能设置布局



# 输入框
f = QFormLayout() # 设置行
pNormalLineEdit = QLineEdit( )
f.addRow("Normal", pNormalLineEdit)
pNormalLineEdit.setEchoMode(QLineEdit.Normal)
pNoEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
pPasswordLineEdit.setEchoMode(QLineEdit.Password)
pPasswordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)


#设置验证器
pIntLineEdit.setPlaceholderText("整形");
pDoubleLineEdit.setPlaceholderText("浮点型");
pValidatorLineEdit.setPlaceholderText("字母和数字");

# 整形 范围：[1, 99]
pIntValidator = QIntValidator(self)
pIntValidator.setRange(1, 99)

# 浮点型 范围：[-360, 360] 精度：小数点后2位
pDoubleValidator = QDoubleValidator(self)
pDoubleValidator.setRange(-360, 360)
pDoubleValidator.setNotation(QDoubleValidator.StandardNotation)
pDoubleValidator.setDecimals(2)

# 字符和数字
reg = QRegExp("[a-zA-Z0-9]+$")
pValidator = QRegExpValidator(self)
pValidator.setRegExp(reg)	

# 设置验证器
pIntLineEdit.setValidator(pIntValidator)
pDoubleLineEdit.setValidator(pDoubleValidator)
pValidatorLineEdit.setValidator(pValidator)

from PyQt5.QtCore import Qt
e1.setAlignment( Qt.AlignRight ) # 输入内容靠右