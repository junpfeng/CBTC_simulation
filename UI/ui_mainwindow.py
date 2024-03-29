# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(948, 568)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(120, 240))
        self.frame.setMaximumSize(QtCore.QSize(120, 1000))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.button_track = QtWidgets.QPushButton(self.frame)
        self.button_track.setObjectName("button_track")
        self.verticalLayout.addWidget(self.button_track)
        self.button_scene = QtWidgets.QPushButton(self.frame)
        self.button_scene.setObjectName("button_scene")
        self.verticalLayout.addWidget(self.button_scene)
        self.button_ap = QtWidgets.QPushButton(self.frame)
        self.button_ap.setObjectName("button_ap")
        self.verticalLayout.addWidget(self.button_ap)
        self.button_rec = QtWidgets.QPushButton(self.frame)
        self.button_rec.setObjectName("button_rec")
        self.verticalLayout.addWidget(self.button_rec)
        self.button_interf = QtWidgets.QPushButton(self.frame)
        self.button_interf.setObjectName("button_interf")
        self.verticalLayout.addWidget(self.button_interf)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMinimumSize(QtCore.QSize(500, 500))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mainGraph = GraphicsLayoutWidget(self.frame_3)
        self.mainGraph.setMinimumSize(QtCore.QSize(495, 495))
        self.mainGraph.setAutoFillBackground(False)
        self.mainGraph.setObjectName("mainGraph")
        self.gridLayout_2.addWidget(self.mainGraph, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_3, 0, 1, 2, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(120, 220))
        self.frame_2.setMaximumSize(QtCore.QSize(120, 1000))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setMaximumSize(QtCore.QSize(100, 26))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.textEdit_disp = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_disp.setMinimumSize(QtCore.QSize(100, 100))
        self.textEdit_disp.setMaximumSize(QtCore.QSize(100, 100))
        self.textEdit_disp.setObjectName("textEdit_disp")
        self.verticalLayout_2.addWidget(self.textEdit_disp)
        self.button_reset = QtWidgets.QPushButton(self.frame_2)
        self.button_reset.setObjectName("button_reset")
        self.verticalLayout_2.addWidget(self.button_reset)
        self.button_import = QtWidgets.QPushButton(self.frame_2)
        self.button_import.setObjectName("button_import")
        self.verticalLayout_2.addWidget(self.button_import)
        self.button_run = QtWidgets.QPushButton(self.frame_2)
        self.button_run.setObjectName("button_run")
        self.verticalLayout_2.addWidget(self.button_run)
        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 948, 28))
        self.menubar.setObjectName("menubar")
        self.menuconfigure = QtWidgets.QMenu(self.menubar)
        self.menuconfigure.setObjectName("menuconfigure")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionnew = QtWidgets.QAction(MainWindow)
        self.actionnew.setObjectName("actionnew")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionsave_as = QtWidgets.QAction(MainWindow)
        self.actionsave_as.setObjectName("actionsave_as")
        self.actionrun = QtWidgets.QAction(MainWindow)
        self.actionrun.setObjectName("actionrun")
        self.actiongo = QtWidgets.QAction(MainWindow)
        self.actiongo.setObjectName("actiongo")
        self.actionstop = QtWidgets.QAction(MainWindow)
        self.actionstop.setObjectName("actionstop")
        self.actionpause = QtWidgets.QAction(MainWindow)
        self.actionpause.setObjectName("actionpause")
        self.actionAP = QtWidgets.QAction(MainWindow)
        self.actionAP.setObjectName("actionAP")
        self.menuconfigure.addAction(self.actionAP)
        self.menubar.addAction(self.menuconfigure.menuAction())
        self.label.setBuddy(self.button_track)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "参数设置"))
        self.button_track.setText(_translate("MainWindow", "轨道配置"))
        self.button_scene.setText(_translate("MainWindow", "场景选择"))
        self.button_ap.setText(_translate("MainWindow", "AP参数"))
        self.button_rec.setText(_translate("MainWindow", "接收机参数"))
        self.button_interf.setText(_translate("MainWindow", "干扰基站"))
        self.label_2.setText(_translate("MainWindow", "控制台"))
        self.button_reset.setText(_translate("MainWindow", "reset"))
        self.button_import.setText(_translate("MainWindow", "确认配置"))
        self.button_run.setText(_translate("MainWindow", "开始仿真"))
        self.menuconfigure.setTitle(_translate("MainWindow", "configure"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionnew.setText(_translate("MainWindow", "new"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionsave_as.setText(_translate("MainWindow", "save as ..."))
        self.actionrun.setText(_translate("MainWindow", "run"))
        self.actiongo.setText(_translate("MainWindow", "go"))
        self.actionstop.setText(_translate("MainWindow", "stop"))
        self.actionpause.setText(_translate("MainWindow", "pause"))
        self.actionAP.setText(_translate("MainWindow", "轨道测试点间隔"))


from pyqtgraph import GraphicsLayoutWidget
