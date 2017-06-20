import sys
import os
from PyQt5 import QtWidgets
from Scripts.APIScripts.Competition.ApplyMatch import *


class ScriptGUI(QtWidgets.QWidget):
    def __init__(self):
        super(ScriptGUI, self).__init__()  # 类ScriptGUI继承父类的全部属性
        self.init_GUI()

    def init_GUI(self):
        self.setWindowTitle("报名比赛")
        self.resize(500, 400)
        self.center()

        self.match_id_GUI()
        self.parameter_file_GUI()
        self.data_GUI()
        self.buttons_GUI()

        main_layout = QtWidgets.QVBoxLayout()
        hBoxLayout = QtWidgets.QVBoxLayout()

        hBoxLayout.addWidget(self.match_id_layout)  # 将控件加入图层
        hBoxLayout.addWidget(self.parameter_file_layout)
        hBoxLayout.addWidget(self.data_layout)
        hBoxLayout.addWidget(self.buttons_layout)

        main_layout.addLayout(hBoxLayout)  # 将图层加入窗口
        self.setLayout(main_layout)

    def center(self):
        """
        窗口居中
        :return: 
        """
        qt = self.frameGeometry()
        center_point = QtWidgets.QDesktopWidget().availableGeometry().center()
        qt.moveCenter(center_point)
        self.move(qt.topLeft())

    def match_id_GUI(self):
        self.match_id_layout = QtWidgets.QGroupBox("参数")

        layout = QtWidgets.QGridLayout()  # 网格布局；QHBoxLayout水平布局；QVBoxLayout垂直布局；QFormLayout窗体布局

        match_id_label = QtWidgets.QLabel("赛事ID：")  # 新建标签
        match_id_lineEdit = QtWidgets.QLineEdit()  # 新增文本输入框

        layout.addWidget(match_id_label, 0, 0)  # 在布局中插入标签控件
        layout.addWidget(match_id_lineEdit, 0, 1)  # 在布局中插入输入框控件

        layout.setColumnStretch(1, 10)
        layout.setSpacing(10)  # 设置网格间距为10
        self.match_id_layout.setLayout(layout)

        return match_id_lineEdit.text()

    def parameter_file_GUI(self):
        self.parameter_file_layout = QtWidgets.QGroupBox("用户文件")

        layout = QtWidgets.QHBoxLayout()

        self.parameter_file_button = QtWidgets.QPushButton("选择文件")
        self.parameter_file_lineEdit = QtWidgets.QLineEdit()

        self.parameter_file_button.setObjectName("parameter_file_button")
        self.parameter_file_button.clicked.connect(lambda: self.get_file())  # signal（信号，即clicked方法）与slot（槽）绑定

        layout.addWidget(self.parameter_file_button)
        layout.addWidget(self.parameter_file_lineEdit)
        self.parameter_file_layout.setLayout(layout)

    def get_file(self):
        """
        选择文件，并将文件的绝对路径填入文本框
        :return: 
        """
        file_path = QtWidgets.QFileDialog.getOpenFileName(self)
        self.parameter_file_lineEdit.setText(str(file_path[0]))
        return str(file_path[0])

    def data_GUI(self):
        self.data_layout = QtWidgets.QGroupBox("报名进度")

        layout = QtWidgets.QGridLayout()

        self.process = QtWidgets.QProgressBar()
        self.process.setMinimum(0)
        self.process.setMaximum(self.test_data())

        layout.addWidget(self.process)

        self.data_layout.setLayout(layout)

    def buttons_GUI(self):
        self.buttons_layout = QtWidgets.QGroupBox()
        layout = QtWidgets.QHBoxLayout()
        self.button_start = QtWidgets.QPushButton("开始报名")
        self.button_pause = QtWidgets.QPushButton("暂停报名")
        layout.addWidget(self.button_start)
        layout.addWidget(self.button_pause)
        self.buttons_layout.setLayout(layout)

    def test_data(self):
        num = 0
        for i in range(100):
            i =+1
            return i


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # QT窗口必须在QApplication方法中使用
    t = ScriptGUI()
    t.show()
    sys.exit((app.exec_()))
