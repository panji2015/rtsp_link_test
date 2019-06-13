import sys

from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QMainWindow, QMessageBox

from camera_link_test import CameraLinkTest
from ui_cfg import Ui_ConfigWindow


class ConfigWindow(QMainWindow, Ui_ConfigWindow):
    def __init__(self):
        super(ConfigWindow, self).__init__()
        self.setupUi(self)

        self.btnTestLink.clicked.connect(self.on_click_test_link)

        # ip 设置输入规则
        reg_exp = QtCore.QRegExp('^((2[0-4]\d|25[0-5]|[1-9]?\d|1\d{2})\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?):\d{1,5}$')
        self.lineEditIp.setValidator(QtGui.QRegExpValidator(reg_exp, self))

    def on_click_test_link(self):
        self.btnTestLink.setEnabled(False)
        ip = self.lineEditIp.text()
        port = self.lineEditPort.text()
        loginname = self.lineEditLoginname.text()
        passwd = self.lineEditPasswd.text()
        video_url = "rtsp://%s:%s@%s:%s" % (loginname, passwd, ip, port)

        self.btnTestLink.setText("正在尝试连接")
        self.camera_test = CameraLinkTest(video_url, ip, port)
        self.camera_test.test_signal.connect(self.show_about_box)
        self.camera_test.start()

    def show_about_box(self, msg):
        QMessageBox.about(self, "连接测试", msg)
        self.btnTestLink.setEnabled(True)
        self.btnTestLink.setText("连接测试")


app = QtWidgets.QApplication(sys.argv)
window = ConfigWindow()
window.show()
sys.exit(app.exec_())
