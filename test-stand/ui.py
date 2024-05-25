from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(393, 1080)
        #MainWindow.setFixedSize(393,1080)
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color:#00ff00;\n"
"color:white;")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(375, 900))
        self.frame.setMaximumSize(QtCore.QSize(375, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_2.setStyleSheet("#frame_2{\n"
"border: 2px solid cyan;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Orbitron Black")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color:cyan;")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Orbitron ExtraBold")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_3.setStyleSheet("#frame_3{\n"
"border:2px solid cyan;\n"
"\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Orbitron Black")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:none;\n"
"")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.counter = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.counter.sizePolicy().hasHeightForWidth())
        self.counter.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Orbitron ExtraBold")
        font.setPointSize(25)
        self.counter.setFont(font)
        self.counter.setStyleSheet("color:white;\n"
"background-color:none;")
        self.counter.setObjectName("counter")
        self.verticalLayout_3.addWidget(self.counter, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 120))
        self.frame_5.setStyleSheet("#frame_5{\n"
"border: 2px solid cyan;\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_12 = QtWidgets.QLabel(self.frame_5)
        self.label_12.setMinimumSize(QtCore.QSize(0, 0))
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 49))
        font = QtGui.QFont()
        font.setFamily("Orbitron Black")
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_5.addWidget(self.label_12)
        self.state = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Orbitron ExtraBold")
        font.setPointSize(18)
        self.state.setFont(font)
        self.state.setObjectName("state")
        self.verticalLayout_5.addWidget(self.state, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet("#frame_4{\n"
"border:2px solid cyan;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 49))
        font = QtGui.QFont()
        font.setFamily("Orbitron Black")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.thrust = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Orbitron ExtraBold")
        font.setPointSize(14)
        self.thrust.setFont(font)
        self.thrust.setObjectName("thrust")
        self.verticalLayout_4.addWidget(self.thrust)
        self.pressure = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Orbitron ExtraBold")
        font.setPointSize(14)
        self.pressure.setFont(font)
        self.pressure.setObjectName("pressure")
        self.verticalLayout_4.addWidget(self.pressure)
        self.burn_time = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Orbitron ExtraBold")
        font.setPointSize(14)
        self.burn_time.setFont(font)
        self.burn_time.setObjectName("burn_time")
        self.verticalLayout_4.addWidget(self.burn_time)
        self.impulse = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Orbitron ExtraBold")
        font.setPointSize(14)
        self.impulse.setFont(font)
        self.impulse.setObjectName("impulse")
        self.verticalLayout_4.addWidget(self.impulse)
        self.motor_desg = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Orbitron ExtraBold")
        font.setPointSize(14)
        self.motor_desg.setFont(font)
        self.motor_desg.setObjectName("motor_desg")
        self.verticalLayout_4.addWidget(self.motor_desg)
        self.rssi_val = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Orbitron ExtraBold")
        font.setPointSize(14)
        self.rssi_val.setFont(font)
        self.rssi_val.setObjectName("rssi_val")
        self.verticalLayout_4.addWidget(self.rssi_val)
        self.verticalLayout.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Mission"))
        self.label_2.setText(_translate("MainWindow", "L class static fire"))
        self.label_3.setText(_translate("MainWindow", " CountDown"))
        self.counter.setText(_translate("MainWindow", "T - 0"))
        self.label_12.setText(_translate("MainWindow", " State"))
        self.state.setText(_translate("MainWindow", "Idle"))
        self.label_5.setText(_translate("MainWindow", " Telemetry"))
        self.thrust.setText(_translate("MainWindow", "<html><head/><body><p>&nbsp; Thrust: <span style=\" color:#55ffff;\">0 N</span></p></body></html>"))
        self.pressure.setText(_translate("MainWindow", "<html><head/><body><p>&nbsp; Pressure: <span style=\" color:#55ffff;\">0 psi</span></p></body></html>"))
        self.burn_time.setText(_translate("MainWindow", "<html><head/><body><p>&nbsp; Burn Time: <span style=\" color:#55ffff;\">0 s</span></p></body></html>"))
        self.impulse.setText(_translate("MainWindow", "<html><head/><body><p>&nbsp; Impulse: <span style=\" color:#55ffff;\">0 Ns</span></p></body></html>"))
        self.motor_desg.setText(_translate("MainWindow", "<html><head/><body><p>&nbsp; Motor Desg: <span style=\" color:#55ffff;\">0</span></p></body></html>"))
        self.rssi_val.setText(_translate("MainWindow", "<html><head/><body><p>&nbsp; RSSI Val: <span style=\" color:#55ffff;\">0 dB</span></p></body></html>"))

class ControlDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.layout_panel= QtWidgets.QVBoxLayout()
        self.ignition_button = QtWidgets.QPushButton(self)
        self.ignition_button.setText("Start ignition sequence")
        self.time_edit = QtWidgets.QLineEdit()
        self.time_edit.setValidator(QtGui.QIntValidator())
        font = QtGui.QFont()
        font.setPointSize(22)
        self.time_edit.setFont(font)
        self.counter_button = QtWidgets.QPushButton()
        self.counter_button.setText("start counter")

        font2 = QtGui.QFont()
        font2.setPointSize(18)

        self.thrust = QtWidgets.QLabel()
        self.thrust.setFont(font2)
        self.thrust.setText("thrust: 0")
        self.pressure = QtWidgets.QLabel()
        self.pressure.setFont(font2)
        self.pressure.setText("pressure: 0")
        self.burn = QtWidgets.QLabel()
        self.burn.setFont(font2)
        self.burn.setText("burn time: 0")
        self.impulse = QtWidgets.QLabel()
        self.impulse.setFont(font2)
        self.impulse.setText("impulse: 0")
        self.desg = QtWidgets.QLabel()
        self.desg.setFont(font2)
        self.desg.setText("desg: 0")
        self.rssi = QtWidgets.QLabel()
        self.rssi.setFont(font2)
        self.rssi.setText("rssi: 0")
        self.counter = QtWidgets.QLabel()
        self.counter.setFont(font2)
        self.counter.setText("T - 0")
        

        self.spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding) 

        self.layout_panel.addWidget(self.ignition_button)
        self.layout_panel.addWidget(self.thrust)
        self.layout_panel.addWidget(self.pressure)        
        self.layout_panel.addWidget(self.burn)       
        self.layout_panel.addWidget(self.impulse)
        self.layout_panel.addWidget(self.desg)
        self.layout_panel.addWidget(self.rssi)   
        self.layout_panel.addItem(self.spacer)    
        self.layout_panel.addWidget(self.time_edit)
        self.layout_panel.addWidget(self.counter_button)
        self.layout_panel.addWidget(self.counter)

        self.setLayout(self.layout_panel)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    dialog = ControlDialog()
    dialog.show()
    MainWindow.show()
    sys.exit(app.exec_())
