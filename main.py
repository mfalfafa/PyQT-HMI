# always seem to need this
import sys
 
# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *

# for serial communication
import serial
import time
import threading

# This is our window from QtCreator
import mainwindow_auto
import my_dialog
import my_login

# To counter up with button clicked
n_detect=0

dialog1=''
login=''
mainWin=''

# Data variables
data1=''
data2=''
data3=''
lbl_data1=''
lbl_data2=''
lbl_data3=''
serial_data=''
lbl_serial=''
lbl_info=''
le_login=''

# Exit Flag
exit_f=0

# Using threading to communicate with serial port
class receiveDataThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        receiveData()

def receiveData():
    global lbl_serial, exit_f
    connected = False
    ser_to_hmi = 0
    ready_f=0
    ## Establish connection to COM Port
    ## Connection from HMI
    locations=['/dev/ttyUSB0']
    ## loop until the device tells us it is ready
    while not connected:
        if exit_f==1:
            break
        ## COM Port settings
        for device in locations: 
            try:
                # print ("Trying...",device)
                ## Serial Initialization
                ser_to_hmi = serial.Serial(device,      #port
                                    9600,              #baudrate
                                    serial.EIGHTBITS,   #bytesize
                                    serial.PARITY_NONE,  #parity
                                    serial.STOPBITS_ONE,#stop bit
                                    0,                  #timeout
                                    False,              #xonxoff
                                    False,              #rtscts
                                    0,                  #write_timeout
                                    False,              #dsrdtr
                                    None,               #inter byte timeout
                                    None                #exclusive
                                    )
                connected=True
            except:
                connected=False
                print ("trying to connect to ", device)
                time.sleep(1.5)
    if connected:
        serin = ser_to_hmi.read()
        print ("Connected to ",device)
        connected=False
        ready_f=1
        
    data_=''
    while not exit_f:
        try:
            if ser_to_hmi.inWaiting():
                x=ser_to_hmi.read()
                x=x.decode('ascii')
                data_=data_ + x
                lbl_serial.setText(str(data_))
                if x == '\r':
                    print (data_)
                    # Show to HMI
                    lbl_serial.setText(str(data_))
                    data_=''
        except KeyboardInterrupt:
            break
        except Exception as e:
            print ('Error : '+ str(e))
            break

    if ready_f==1:
        ## close the serial connection and text file
        print ("Connection is closed!")
        ser_to_hmi.close()

class Login_(QMainWindow, my_login.Ui_my_login):
    def ret_press(self):
        global lbl_info,le_login
        if le_login.text()=='11111':
            self.close()
            mainWin.show()
        else:
            lbl_info.setText('Login Failed!')

    def __init__(self):
        global lbl_info,le_login
        super(self.__class__, self).__init__()
        self.setupUi(self)
        lbl_info=self.lbl_info
        le_login=self.le_login
        self.le_login.returnPressed.connect(lambda: self.ret_press())


# Sub Window
class MyDialog(QMainWindow, my_dialog.Ui_my_dialog):
    def submitData(self):
        global data1,data2,data3,lbl_data1,lbl_data2,lbl_data3
        data1=self.le1.text()
        data2=self.le2.text()
        data3=self.le3.text()
        lbl_data1.setText(data1)
        lbl_data2.setText(data2)
        lbl_data3.setText(data3)

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        # Exit dialog
        self.pb_exit.clicked.connect(self.close)
        # line edit
        le1=self.le1
        le2=self.le2
        le3=self.le3
        # Submit Button
        self.pb_submit.clicked.connect(self.submitData)

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
    # access variables inside of the UI's file

    # Functions for the button
    def pressPB1(self):
        self.lbl1.setText('PB1 Clicked')
        print('Clicked')
        pass

    def pressPB2(self):
        global n_detect
        n_detect=n_detect+1
        self.lcdNumber.display(n_detect)
        self.lbl2.setText('PB2 Clicked')
        pass
        
    def pressInsert(self):
        # Current text of Combo Box
        self.lbl3.setText(self.comboBox.currentText())
        # Insert to ListWidget
        self.listWidget.addItem(self.comboBox.currentText())

    def valuechange(self):
        self.lbl4.setText(str(self.spinBox.value()))

    def comboIndexChanged(self):
        self.lbl5.setText(self.comboBox.currentText())

    def listClicked(self,item):
        self.lbl6.setText(str(item.text()))

    def exitWindow(self):
        global exit_f,lbl_info,le_login
        exit_f=1
        lbl_info.setText('')
        le_login.setText('')
        self.close()
        login.show()

    def showdialog(self):
        dialog1.show()
        # d = QDialog()
        # b1 = QPushButton("ok",d)
        # b1.move(50,50)
        # d.setWindowTitle("Dialog")
        #d.setWindowModality(Qt.ApplicationModal)
        # d.setModal(True)
        # d.exec_()
        pass

    def ret_press(self):
        print ('Enter in pressed!')

    def __init__(self):
        global lbl_data1,lbl_data2,lbl_data3,lbl_serial
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
 
        # Hooks to for button
        self.pb_on.clicked.connect(lambda: self.pressPB1())
        self.pb_off.clicked.connect(lambda: self.pressPB2())
        self.pb_insert.clicked.connect(lambda: self.pressInsert())
        self.pb_dialog.clicked.connect(lambda: self.showdialog())
        # Close main window
        self.pb_exit.clicked.connect(lambda: self.exitWindow())

        # Change text while clicked
        lbl1=self.lbl1
        lbl2=self.lbl2
        lbl3=self.lbl3
        lbl4=self.lbl4
        self.lbl4.setText(str(0))
        lbl5=self.lbl5
        self.lbl5.setText('Select 1')
        lbl6=self.lbl6
        # Data label (with global variable)
        lbl_data1=self.lbl_data1
        lbl_data2=self.lbl_data2
        lbl_data3=self.lbl_data3
        # For serial data
        lbl_serial=self.lbl8

        # LineEdit
        le1=self.le1
        self.le1.returnPressed.connect(lambda: self.ret_press())

        # LCD Number
        self.lcdNumber.display(n_detect)
        lcdNumber=self.lcdNumber

        # Combo Box
        comboBox=self.comboBox
        self.comboBox.currentIndexChanged.connect(self.comboIndexChanged)

        # SpinBox
        self.spinBox.valueChanged.connect(self.valuechange)
        spinBox=self.spinBox

        # List Widget
        listWidget=self.listWidget
        self.listWidget.itemClicked.connect(self.listClicked)
        
# I feel better having one of these
def main():
    global dialog1,login,mainWin,le_login
    # a new app instance
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    # form.show()
    dialog1 = MyDialog()
    login = Login_()
    login.show()
    le_login.setFocus()
    # without this, the script exits immediately.
    sys.exit(app.exec_())
 
# Create new thread for sending data every second
try:
    recDataThread=receiveDataThread()
except Exception as e:
    print ("Error: unable to start thread!")
    print (str(e))
# Start thread
recDataThread.start()

# python bit to figure how who started This
if __name__ == "__main__":
    main()
