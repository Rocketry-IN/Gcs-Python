from ui import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon
import sys
import time
import datetime
from serial_man import read_serial

class Main():
    def __init__(self):
        self.mainwin = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.mainwin)
        self.control_dialog = ControlDialog()
        self.mainwin.setWindowIcon(QIcon("resources/patch.png"))
        self.mainwin.setWindowTitle("Ground Control!! Sonus Go BRRR")
        self.control_dialog.show()
        global counter_running 
        global state
        state = "Idle"
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
        if state == "Burn":
            self.elapsed_count += 1
        elif state == "Idle":
            self.elapsed_count = 0
        self.ui.rssi_val.setText("<html><head/><body><p>&nbsp; Elapsed: <span style=\" color:#55ffff;\">"+ str((self.elapsed_count)/100) +" s</span></p></body></html>" )

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
            self.ui.state.setText(state)
            self.ui.thrust.setText("<html><head/><body><p>&nbsp; Thrust: <span style=\" color:#55ffff;\">"+ str(round(float(data[0]))) +" N</span></p></body></html>" )
            self.ui.pressure.setText("<html><head/><body><p>&nbsp; Pressure: <span style=\" color:#55ffff;\">"+ str(round(float(data[1]))) +" psi</span></p></body></html>" )
            

            self.control_dialog.thrust.setText("<html><head/><body><p>Thrust: <span style=\" color:#55ffff;\">"+ str(round(float(data[0]))) +" N</span></p></body></html>" )
            self.control_dialog.pressure.setText("<html><head/><body><p>Pressure: <span style=\" color:#55ffff;\">"+ str(round(float(data[1]))) +" psi</span></p></body></html>" )
        
        except: 
            self.ui.state.setText(state)



class counter_thread(QtCore.QThread):
    global counter_running

    count_time = QtCore.pyqtSignal(str)
    def __init__(self,counter):
        super().__init__()
        self.counter = counter
    def run(self):
        while counter_running:
            global state
            if self.counter > 0:
                self.count_time.emit(" + "+ str(datetime.timedelta(seconds=(self.counter))))
            else:
                self.count_time.emit(" - "+ str(datetime.timedelta(seconds=abs(self.counter))))  
            if self.counter == 0:
                state = "Burn"
            elif self.counter < 0:
                state = "Idle"
            time.sleep(1)  
            self.counter += 1

class update_thread(QtCore.QThread):
    recieved = QtCore.pyqtSignal(list)
    def __init__(self):
        super().__init__()
    
    def run(self):
        while True:
            data = read_serial()
            self.recieved.emit(data)
            time.sleep(0.01)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gcs = Main()
    gcs.mainwin.show()
    gcs.main()
    sys.exit(app.exec_())