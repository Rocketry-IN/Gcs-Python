# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gcs_final.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1913, 1070)
        MainWindow.setStyleSheet("background-color:black;\n"
"color:white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(22)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("#frame{\n"
"border:2px solid grey;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.thrust = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(22)
        self.thrust.setFont(font)
        self.thrust.setObjectName("thrust")
        self.verticalLayout_2.addWidget(self.thrust)
        self.pressure = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(22)
        self.pressure.setFont(font)
        self.pressure.setObjectName("pressure")
        self.verticalLayout_2.addWidget(self.pressure)
        self.impulse = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(22)
        self.impulse.setFont(font)
        self.impulse.setObjectName("impulse")
        self.verticalLayout_2.addWidget(self.impulse)
        self.pyro_status = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(22)
        self.pyro_status.setFont(font)
        self.pyro_status.setObjectName("pyro_status")
        self.verticalLayout_2.addWidget(self.pyro_status)
        self.burn_time = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(22)
        self.burn_time.setFont(font)
        self.burn_time.setObjectName("burn_time")
        self.verticalLayout_2.addWidget(self.burn_time)
        self.desg = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(22)
        self.desg.setFont(font)
        self.desg.setObjectName("desg")
        self.verticalLayout_2.addWidget(self.desg)
        self.rssi_val = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(22)
        self.rssi_val.setFont(font)
        self.rssi_val.setObjectName("rssi_val")
        self.verticalLayout_2.addWidget(self.rssi_val)
        spacerItem = QtWidgets.QSpacerItem(20, 300, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 72))
        self.label_2.setPixmap(QtGui.QPixmap("resources/gcs.png").scaled(360, 72, transformMode=QtCore.Qt.SmoothTransformation))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(64)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setStyleSheet("#frame_4{\n"
"border:2px solid grey;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Medium")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:darkgrey;")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(16)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet("border:2px solid grey;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setStyleSheet("#frame_6{\n"
"border:2px solid grey;\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.frame_6)
        self.label_8.setMaximumSize(QtCore.QSize(140, 140))
        self.label_8.setStyleSheet("border-image: url(resources/patch.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_12 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Orbitron Medium")
        font.setPointSize(18)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_4.addWidget(self.label_12, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.counter = QtWidgets.QLabel(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.counter.sizePolicy().hasHeightForWidth())
        self.counter.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(40)
        self.counter.setFont(font)
        self.counter.setStyleSheet("color:red;")
        self.counter.setObjectName("counter")
        self.verticalLayout_4.addWidget(self.counter, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.label_10 = QtWidgets.QLabel(self.frame_6)
        self.label_10.setMaximumSize(QtCore.QSize(140, 140))
        self.label_10.setStyleSheet("border-image: url(resources/logo.webp);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.verticalLayout.addWidget(self.frame_6)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(22)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet("#frame_3{\n"
"border:2px solid grey;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_5.addItem(spacerItem2)
        self.start_counter_button = QtWidgets.QPushButton(self.frame_3)
        self.start_counter_button.setIconSize(QtCore.QSize(26,26))
        self.start_counter_button.setIcon(QtGui.QIcon("resources/arrow.png"))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(20)
        self.start_counter_button.setFont(font)
        self.start_counter_button.setObjectName("start_counter_button")
        self.verticalLayout_5.addWidget(self.start_counter_button, 0, QtCore.Qt.AlignLeft)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_5.addItem(spacerItem3)
        self.start_ignition = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(20)
        self.start_ignition.setIconSize(QtCore.QSize(26,26))
        self.start_ignition.setIcon(QtGui.QIcon("resources/arrow.png"))
        self.start_ignition.setFont(font)
        self.start_ignition.setObjectName("start_ignition")
        self.verticalLayout_5.addWidget(self.start_ignition, 0, QtCore.Qt.AlignLeft)
        self.graph_1 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.graph_1.sizePolicy().hasHeightForWidth())
        self.graph_1.setSizePolicy(sizePolicy)
        self.graph_1.setText("")
        self.graph_1.setObjectName("graph_1")
        self.verticalLayout_5.addWidget(self.graph_1)
        self.graph_2 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.graph_2.sizePolicy().hasHeightForWidth())
        self.graph_2.setSizePolicy(sizePolicy)
        self.graph_2.setText("")
        self.graph_2.setObjectName("graph_2")
        self.verticalLayout_5.addWidget(self.graph_2)
        self.state = QtWidgets.QLabel(self.frame_3)
        self.state.setMinimumSize(QtCore.QSize(325, 80))
        self.state.setMaximumSize(QtCore.QSize(325, 80))
        font = QtGui.QFont()
        font.setFamily("Orbitron Medium")
        font.setPointSize(28)
        self.state.setFont(font)
        self.state.setStyleSheet("border:2px solid cyan;\n"
"border-radius:20px;")
        self.state.setAlignment(QtCore.Qt.AlignCenter)
        self.state.setObjectName("state")
        self.verticalLayout_5.addWidget(self.state, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem4 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_5.addItem(spacerItem4)
        self.horizontalLayout.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.thrust.setText(_translate("MainWindow", "<html><head/><body><p>Thrust: <span style=\" color:#55ffff;\">0 N</span></p></body></html>"))
        self.pressure.setText(_translate("MainWindow", "<html><head/><body><p>Pressure: <span style=\" color:#55ffff;\">0 psi</span></p></body></html>"))
        self.impulse.setText(_translate("MainWindow", "<html><head/><body><p>Impulse: <span style=\" color:#55ffff;\">0 Ns</span></p></body></html>"))
        self.pyro_status.setText(_translate("MainWindow", "<html><head/><body><p>Pyro status: <span style=\" color:#55ffff;\">0</span></p></body></html>"))
        self.burn_time.setText(_translate("MainWindow", "<html><head/><body><p>Burn time: <span style=\" color:#55ffff;\">0 s</span></p></body></html>"))
        self.desg.setText(_translate("MainWindow", "<html><head/><body><p>Motor Desg: <span style=\" color:#55ffff;\">0</span></p></body></html>"))
        self.rssi_val.setText(_translate("MainWindow", "<html><head/><body><p>RSSI val: <span style=\" color:#55ffff;\">0 db</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "motor characterization testing"))
        self.label_6.setText(_translate("MainWindow", "Rocketry-IN"))
        self.label_12.setText(_translate("MainWindow", "CountDown"))
        self.counter.setText(_translate("MainWindow", "T - 0"))
        self.start_counter_button.setText(_translate("MainWindow", " Start Counter"))
        self.start_ignition.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#55ffff;\">&gt;</span> Chute</p></body></html>"))
        self.start_ignition.setText(_translate("MainWindow", " Start Ignition Sequence"))
        self.state.setText(_translate("MainWindow", " Idle"))

class EditDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit Counter")
        self.resize(300,150)
        self.layout = QtWidgets.QVBoxLayout()
        self.time_edit = QtWidgets.QLineEdit()
        self.time_edit.setValidator(QtGui.QIntValidator())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        self.time_edit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(22)
        self.time_edit.setStyleSheet("color:red;")
        self.time_edit.setFont(font)
        self.layout.addWidget(self.time_edit)
        self.counter_button = QtWidgets.QPushButton()
        self.counter_button.setText("start counter")
        self.layout.addWidget(self.counter_button)
        self.exit_button = QtWidgets.QPushButton()
        self.exit_button.setText("Exit")
        self.layout.addWidget(self.exit_button)
        self.setLayout(self.layout)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    dialog = EditDialog()
    dialog.show()
    MainWindow.showMaximized()
    sys.exit(app.exec_())