from ui import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon
import sys
import time
import datetime
#from serial_man import read_serial

#chute state: 1 , 0 

class Main():
    def __init__(self):
        self.mainwin = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.mainwin)
        self.control_dialog = ControlDialog()
        self.mainwin.setWindowIcon(QIcon("resources/patch.png"))
        self.mainwin.setWindowTitle("Ground Control!! Sonus Go BRRR")
        self.control_dialog.show()
        self.chutes = 0
        global counter_running 
        global el_state
        el_state = 0
        self.elapsed_count =0
        counter_running = False

    def main(self):
        self.t1 = update_thread()
        self.t1.recieved.connect(self.update_text)
        self.t1.start()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.show_elapsed)
        self.timer.start(10)
 
        self.control_dialog.counter_button.clicked.connect(lambda: self.start_counter())

    def show_elapsed(self):
        if el_state == 1:
            self.elapsed_count += 1
        elif el_state == 0:
            self.elapsed_count = 0
        self.ui.elapsed.setText("<html><head/><body><p>&nbsp; Elapsed: <span style=\" color:#55ffff;\">"+ str((self.elapsed_count)/100) +" s</span></p></body></html>" )

    def start_counter(self):
        global counter_running
        if counter_running == False:
            if self.control_dialog.time_edit.text() == '':
                pass    
            else:
                self.t2 = counter_thread(int(float(self.control_dialog.time_edit.text()))*-1)
                self.t2.count_time.connect(self.update_counter)
                counter_running = True
                self.t2.start()
                self.control_dialog.counter_button.setText("Pause Counter")
        else:
            counter_running = False
            self.t2.exit()
            self.t2.quit()
            self.control_dialog.counter_button.setText("Start Counter")



    def update_counter(self,data):
        self.ui.counter.setText("T" + data)
        self.control_dialog.counter.setText("T" + data)

    def update_text(self,data):

        try:
            if el_state == 1:
                self.ui.state.setText("Ascent")
            elif el_state == 0:
                if data[3] == 1:
                    self.chutes = 1
                    self.ui.state.setText("Under Chutes")
                else:
                    self.ui.state.setText("Idle")
            self.ui.altitude.setText("<html><head/><body><p>&nbsp; altitude: <span style=\" color:#55ffff;\">"+ str(round(float(data[0]))) +" m</span></p></body></html>" )
            self.ui.lat.setText("<html><head/><body><p>&nbsp; latitude: <span style=\" color:#55ffff;\">"+ str(round(float(data[1]))) +" deg</span></p></body></html>" )
            self.ui.accel.setText( "<html><head/><body><p>&nbsp; acceleration: <span style=\" color:#55ffff;\">0 m/s2</span></p></body></html>")
            self.ui.lon.setText("MainWindow", "<html><head/><body><p>&nbsp; longitude: <span style=\" color:#55ffff;\">0 deg</span></p></body></html>")

            self.control_dialog.altitude.setText("altitude:" + str(round(float(data[0]))))
            self.control_dialog.accel.setText("Pressure: "+ str(round(float(data[1]))))
        
        except: 
            if el_state == 1:
                self.ui.state.setText("Ascent")
            elif el_state == 0:
                if self.chutes ==1:
                    self.ui.state.setText("Under Chutes")
                else: 
                    self.ui.state.setText("Idle")



class counter_thread(QtCore.QThread):
    global counter_running

    count_time = QtCore.pyqtSignal(str)
    def __init__(self,counter):
        super().__init__()
        self.counter = counter
    def run(self):
        while counter_running:
            global el_state
            if self.counter > 0:
                self.count_time.emit(" + "+ str(datetime.timedelta(seconds=(self.counter))))
            else:
                self.count_time.emit(" - "+ str(datetime.timedelta(seconds=abs(self.counter))))  
            if self.counter == 0:
                el_state = 1
            elif self.counter < 0:
                el_state = 0
            time.sleep(1)  
            self.counter += 1

class update_thread(QtCore.QThread):
    recieved = QtCore.pyqtSignal(list)
    def __init__(self):
        super().__init__()
    
    def run(self):
        while True:
            data = [0] #read_serial()
            self.recieved.emit(data)
            time.sleep(0.01)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gcs = Main()
    gcs.mainwin.show()
    gcs.main()
    sys.exit(app.exec_())