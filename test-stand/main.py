from ui import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon
import sys
import time
import datetime
from serial_man import read_serial, send_serial

class Main():
    def __init__(self):
        self.mainwin = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.mainwin)
        self.count_dialog = EditDialog()
        self.mainwin.setWindowIcon(QIcon("resources/patch.png"))
        self.mainwin.setWindowTitle("Ground Control!! Sonus Go BRRR")
        global counter_running 

    def main(self):
        self.t1 = update_thread()
        self.t1.recieved.connect(self.update_text)
        self.t1.start()

        self.ui.start_counter_button.clicked.connect(lambda: self.count_dialog.show())
        self.count_dialog.counter_button.clicked.connect(lambda: self.start_counter())
        self.count_dialog.exit_button.clicked.connect(lambda: self.count_dialog.accept())

    def start_counter(self):
        global counter_running
        if counter_running == False:
            if self.count_dialog.time_edit.text() == '':
                pass    
            else:
                self.t2 = counter_thread(int(float(self.count_dialog.time_edit.text()))*-1)
                self.t2.count_time.connect(self.update_counter)
                counter_running = True
                self.t2.start()
                self.ui.start_counter_button.setText(" Pause Counter")
        else:
            counter_running = False
            self.t2.exit()
            self.t2.quit()
            self.ui.start_counter_button.setText(" Start Counter")


        self.count_dialog.accept()

    def update_counter(self,data):
        self.ui.counter.setText("T" + data)

    def update_text(self,data):
        self.ui.thrust.setText("<html><head/><body><p>Thrust: <span style=\" color:#55ffff;\">"+ str(round(float(data[1]))) +" m/s</span></p></body></html>" )
        self.ui.pressure.setText("<html><head/><body><p>Pressure: <span style=\" color:#55ffff;\">"+ str(round(float(data[2]))) +" m/s</span></p></body></html>" )
        self.ui.impulse.setText("<html><head/><body><p>Impulse: <span style=\" color:#55ffff;\">"+ str(round(float(data[3]))) +" m/s</span></p></body></html>" )
        self.ui.pyro_status.setText("<html><head/><body><p>Pyro status: <span style=\" color:#55ffff;\">"+ str(data[4]) +" m/s</span></p></body></html>" )
        self.ui.burn_time.setText("<html><head/><body><p>Burn time: <span style=\" color:#55ffff;\">"+ str(round(float(data[5]))) +" m</span></p></body></html>" )
        self.ui.burn_time.setText("<html><head/><body><p>Motor Desg: <span style=\" color:#55ffff;\">"+ str(data[6]) +" m</span></p></body></html>" )
        self.ui.burn_time.setText("<html><head/><body><p>RSSI val: <span style=\" color:#55ffff;\">"+ str(round(float(data[7]))) +" m</span></p></body></html>" )
        self.ui.state.setText(str(data[8]))


class counter_thread(QtCore.QThread):
    global counter_running
    count_time = QtCore.pyqtSignal(str)
    def __init__(self,counter):
        super().__init__()
        self.counter = counter

    def run(self):
        while counter_running:
            if self.counter > 0:
                self.count_time.emit(" + "+ str(datetime.timedelta(seconds=(self.counter))))
            else:
                self.count_time.emit(" - "+ str(datetime.timedelta(seconds=abs(self.counter))))  
            time.sleep(1)            
            self.counter += 1

class update_thread(QtCore.QThread):
    recieved = QtCore.pyqtSignal(str)
    def __init__(self):
        super().__init__()
    
    def run(self):
        while True:
            data = read_serial()
            self.recieved.emit(data)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gcs = Main()
    gcs.mainwin.showMaximized()
    gcs.main()
    sys.exit(app.exec_())