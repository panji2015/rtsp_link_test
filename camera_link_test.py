import socket
import cv2
from PySide2.QtCore import QThread
from PySide2.QtCore import Signal as pyqtSignal
# from PySide2.QtCore import Slot as pyqtSlot


class CameraLinkTest(QThread):
    test_signal = pyqtSignal(str)  # 括号里填写信号传递的参数

    def __init__(self, video_url, ip, port):
        QThread.__init__(self)
        self.video_url = video_url
        self.ip = ip
        self.port = port

    def run(self):
        print("in video_link_test")
        if not self.test_ip_port():
            msg = "连接不通"
        else:
            msg = "请检查账号和密码"
            cap = cv2.VideoCapture(self.video_url)
            if cap.isOpened():
                msg = "连接成功"
            cap.release()
        self.test_signal.emit(msg)

    def test_ip_port(self):
        ip_port_ok = False
        try:
            if self.video_url == "" or self.ip == "" or self.port == "":
                return
            sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sk.settimeout(1)
            try:
                sk.connect((self.ip, int(self.port)))
                print('Server port OK!')
                print((self.ip, int(self.port)))
                ip_port_ok = True
            except Exception as e:
                print("!!! error test_ip_port, e = ", str(e))
                print('Server port not connect!')
            sk.close()
        finally:
            return ip_port_ok