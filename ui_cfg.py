# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_ConfigWindow(object):
    def setupUi(self, ConfigWindow):
        ConfigWindow.setObjectName("ConfigWindow")
        ConfigWindow.resize(600, 400)

        self.centralwidget = QtWidgets.QWidget(ConfigWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ip设置ui
        self.vLayoutIpWidget = QtWidgets.QWidget(self.centralwidget)
        self.vLayoutIpWidget.setGeometry(QtCore.QRect(50, 50, 450, 271))
        self.vLayoutIpWidget.setObjectName("vLayoutIpWidget")
        self.vLayoutIpView = QtWidgets.QVBoxLayout(self.vLayoutIpWidget)
        self.vLayoutIpView.setContentsMargins(0, 0, 0, 0)
        self.vLayoutIpView.setObjectName("vLayoutIpView")

        self.hLayoutIpInput = QtWidgets.QHBoxLayout()
        self.hLayoutIpInput.setContentsMargins(0, 0, 0, 0)
        self.hLayoutIpInput.setObjectName("hLayoutIpInput")
        self.radioIp = QtWidgets.QRadioButton(self.vLayoutIpWidget)
        self.radioIp.setMinimumSize(QtCore.QSize(80, 0))
        self.radioIp.setMaximumSize(QtCore.QSize(80, 1280))
        self.radioIp.setObjectName("radioIp")
        self.hLayoutIpInput.addWidget(self.radioIp)
        self.vLayoutIpEdit = QtWidgets.QVBoxLayout()
        self.vLayoutIpEdit.setSpacing(0)
        self.vLayoutIpEdit.setObjectName("vLayoutIpEdit")
        self.hLayoutIpEdit = QtWidgets.QHBoxLayout()
        self.hLayoutIpEdit.setObjectName("hLayoutIpEdit")
        self.labelIp = QtWidgets.QLabel(self.vLayoutIpWidget)
        self.labelIp.setFixedWidth(50)
        self.labelIp.setObjectName("labelIp")
        self.hLayoutIpEdit.addWidget(self.labelIp)
        self.lineEditIp = QtWidgets.QLineEdit(self.vLayoutIpWidget)
        self.lineEditIp.setObjectName("lineEditIp")
        self.hLayoutIpEdit.addWidget(self.lineEditIp)

        self.labelMaoHao = QtWidgets.QLabel(self.vLayoutIpWidget)
        self.labelMaoHao.setObjectName("labelMaoHao")
        self.hLayoutIpEdit.addWidget(self.labelMaoHao)

        self.lineEditPort = QtWidgets.QLineEdit(self.vLayoutIpWidget)
        self.lineEditPort.setObjectName("lineEditPort")
        self.lineEditPort.setFixedWidth(50)
        self.hLayoutIpEdit.addWidget(self.lineEditPort)

        self.vLayoutIpEdit.addLayout(self.hLayoutIpEdit)
        spacerItemIp1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vLayoutIpEdit.addItem(spacerItemIp1)
        self.hLayoutLoginname = QtWidgets.QHBoxLayout()
        self.hLayoutLoginname.setObjectName("hLayoutLoginname")
        self.labelLoginname = QtWidgets.QLabel(self.vLayoutIpWidget)
        self.labelLoginname.setFixedWidth(50)
        self.labelLoginname.setObjectName("labelLoginname")
        self.hLayoutLoginname.addWidget(self.labelLoginname)
        self.lineEditLoginname = QtWidgets.QLineEdit(self.vLayoutIpWidget)
        self.lineEditLoginname.setObjectName("lineEditLoginname")
        self.hLayoutLoginname.addWidget(self.lineEditLoginname)
        self.vLayoutIpEdit.addLayout(self.hLayoutLoginname)
        spacerItemIp2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vLayoutIpEdit.addItem(spacerItemIp2)
        self.hLayoutPasswd = QtWidgets.QHBoxLayout()
        self.hLayoutPasswd.setObjectName("hLayoutPasswd")
        self.labelPasswd = QtWidgets.QLabel(self.vLayoutIpWidget)
        self.labelPasswd.setFixedWidth(50)
        self.labelPasswd.setObjectName("labelPasswd")
        self.hLayoutPasswd.addWidget(self.labelPasswd)
        self.lineEditPasswd = QtWidgets.QLineEdit(self.vLayoutIpWidget)
        self.lineEditPasswd.setObjectName("lineEditPasswd")
        self.hLayoutPasswd.addWidget(self.lineEditPasswd)
        self.vLayoutIpEdit.addLayout(self.hLayoutPasswd)
        self.hLayoutIpInput.addLayout(self.vLayoutIpEdit)
        spacerItemIp3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.hLayoutIpInput.addItem(spacerItemIp3)
        self.btnTestLink = QtWidgets.QPushButton(self.vLayoutIpWidget)
        self.btnTestLink.setMinimumSize(QtCore.QSize(80, 30))
        self.btnTestLink.setMaximumSize(QtCore.QSize(80, 30))
        self.btnTestLink.setObjectName("btnTestLink")
        self.hLayoutIpInput.addWidget(self.btnTestLink)
        self.vLayoutIpView.addLayout(self.hLayoutIpInput)
        # 布局结束
        ConfigWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(ConfigWindow)
        QtCore.QMetaObject.connectSlotsByName(ConfigWindow)

    def retranslateUi(self, ConfigWindow):
        _translate = QtCore.QCoreApplication.translate
        ConfigWindow.setWindowTitle(_translate("ConfigWindow", "配置"))

        self.radioIp.setText(_translate("ConfigWindow", "ip输入"))
        self.labelIp.setText(_translate("ConfigWindow", "地址"))
        self.labelMaoHao.setText(_translate("ConfigWindow", ":"))
        self.labelLoginname.setText(_translate("ConfigWindow", "账号"))
        self.labelPasswd.setText(_translate("ConfigWindow", "密码"))
        self.btnTestLink.setText(_translate("ConfigWindow", "连接测试"))


