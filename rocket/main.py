from ui import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon
from api_man import *
import sys
import time
import datetime

counter_running = False

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
        data = json.loads(data)
        self.ui.altitude.setText("<html><head/><body><p>Altitude: <span style=\" color:#55ffff;\">"+ str(round(float(data["altitude"]))) +" m</span></p></body></html>" )
        self.ui.velocity.setText("<html><head/><body><p>Velocity: <span style=\" color:#55ffff;\">"+ str(round(float(data["velocity"]), 4)) +" m/s</span></p></body></html>" )
#        if data["state"] == 0:
#            self.ui.status.setText("StandBy")
#        elif data["state"] == 1:
#            self.ui.status.setText("Ascent")
#        elif data["state"] == 2:
#            self.ui.status.setText("Descent")
#        elif data["state"] == 3:
#            self.ui.status.setText("landed")
        
class update_thread(QtCore.QThread):
    recieved = QtCore.pyqtSignal(str)
    def __init__(self):
        super().__init__()
    
    def run(self):
        while True:
            data = api_call()
            self.recieved.emit(data)

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



if __name__ == "__main__":
    app = QApplication(sys.argv)
    gcs = Main()
    gcs.mainwin.showMaximized()
    gcs.main()
    sys.exit(app.exec_())