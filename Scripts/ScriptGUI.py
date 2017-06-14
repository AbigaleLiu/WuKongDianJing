import sys
from PyQt5 import QtWidgets


class ScriptGUI(QtWidgets.QWidget):
    def __init__(self):
        super(ScriptGUI, self).__init__()  # 类ScriptGUI继承父类的全部属性
        self.apply_match_GUI()

    def init_GUI(self):
        self.match_id_GUI()
        main_layout = QtWidgets.QVBoxLayout()  # 窗口
        layout_11 = QtWidgets.QVBoxLayout()  # 第一个一级图层
        layout_12 = QtWidgets.QVBoxLayout()  # 第二个一级图层


    def match_id_GUI(self):
        self.setWindowTitle("报名比赛")  # 窗口标题
        self.setGeometry(500, 400, 500, 400)  # 设置窗口显示位置及大小，相当于resize()+move()

        self.button = QtWidgets.QPushButton("报名", self)  # 新增按钮
        self.button.move(200, 350)  # 设置按钮位置

        self.label = QtWidgets.QLabel("赛事ID：")  # 新建标签
        self.lineEdit = QtWidgets.QLineEdit()  # 新增文本输入框
        self.grid = QtWidgets.QGridLayout()  # 网格布局；QHBoxLayout水平布局；QVBoxLayout垂直布局；QFormLayout窗体布局
        self.grid.setSpacing(10)  # 设置网格间距为10
        self.grid.addWidget(self.label, 0, 0)  # 在布局中插入标签控件
        self.grid.addWidget(self.lineEdit, 0, 1)  # 在布局中插入输入框控件
        self.setLayout(self.grid)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # QT窗口必须在QApplication方法中使用
    t = ScriptGUI()
    t.show()
    sys.exit((app.exec_()))