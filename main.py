# always seem to need this
import sys
 
# For PostgreSQL database 
import psycopg2

# This gets the Qt stuff
import PyQt5
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QThread

# for serial communication
import serial
import time
import threading

# This is our window from QtCreator
import mainwindow_auto
import loginForm
import downtime
import minor
import insertReasonForm

# Qt Windows
login_form=''
mainwin=''
le_login=''
lbl_info=''
dt_page=''
minor_page=''
insertReasonPage=''

# Qt label status
lbl_status_1=''
lbl_status_2=''
lbl_status_3=''
lbl_status_4=''
lbl_status=['']*4   # 4 = how many machines

# Python Thread
timeThread=''
statusThread=''

# Qt Signal
dtSignalStart=''
dtSignalStop=''
minorSignalStart=''
minorSignalStop=''
insertReason=''

# DB data
changeStatusCheck=[0]*4
changeDTStatusCheck=[0]*2   # 2 = Donwntime and Minor status
reasonChangeCheck=-1
reason=''
id_=''

# Flags
checkReady=0
checkReady_main=0
close1_f=0
close2_f=0
close3_f=0
close4_f=0
dt_page_active=0
minor_page_active=0
first_execute=0

# server PostgreSQL DB
hostname='192.168.10.151'
username='postgres'
password='alfafa077'
database='mv-hmi'
port='5432'

while 1:
    try:
        myConnection = psycopg2.connect( host=hostname, port=port, user=username, password=password, dbname=database )
        break
    except Exception as e:
        print ('Trying to connect to Database Server...')
        time.sleep(1)

def doQueryLogin( conn , rfid ):
    cur = conn.cursor()
    myConnection.commit()
    cur.execute("select rfid from public.login_data where rfid='{0}';".format(str(rfid)))
    result = cur.fetchone()
    if result is not None:
        return 1
    else :
        return 0

def doQueryCheckStatus(conn):
    # global status
    cur=conn.cursor()
    myConnection.commit()
    cur.execute("select status from public.status_machine order by id asc")
    result = cur.fetchall()
    status=result
    return status

def doQueryCheckDTStatus(conn):
    global dtSignalStart,dtSignalStop,minorSignalStart,minorSignalStop,changeDTStatusCheck,checkReady_main,dt_page_active,minor_page_active
    cur=conn.cursor()
    myConnection.commit()
    cur.execute("select dt_status from public.status_machine_dt order by id asc")
    result=cur.fetchall()
    # Check downtime status
    if checkReady_main == 1:
        if (changeDTStatusCheck[0] != int(result[0][0])):
            if int(result[0][0]) == 1:
                # Downtime occured
                # Check wheter minor page is active or not
                if minor_page_active==1:
                    # if active, then close it first
                    minorSignalStop.emit()
                    minor_page_active=0
                    changeDTStatusCheck[1]=0
                # Send Downtime signal to Downtime page
                dtSignalStart.emit()
                dt_page_active=1
            elif int(result[0][0]) == 0:
                # Close downtime page
                dtSignalStop.emit()
                dt_page_active=0
            # Update change DT Flags
            changeDTStatusCheck[0]=int(result[0][0])
        if dt_page_active != 1:
            if (changeDTStatusCheck[1] != int(result[1][0])):
                if int(result[1][0]) == 1:
                    # Minor occured
                    minorSignalStart.emit()
                    minor_page_active=1
                elif int(result[1][0]) == 0:
                    # Close Minor page
                    minorSignalStop.emit()
                    minor_page_active=0
                # Update change DT Flags
                changeDTStatusCheck[1]=int(result[1][0])

def doQueryCheckReason(conn):
    global reasonChangeCheck,insertReason,id_,reason,first_execute,myConnection
    cur=conn.cursor()
    if first_execute==0:
        first_execute=1
        cur.execute("select id,data_dt from public.data_downtime order by id asc")
    else:
        cur.execute("select id,data_dt from public.data_downtime order by id desc LIMIT 1")
    result = cur.fetchall()
    # print (result)
    for i in range(len(result)):
        # There are new reasons
        if reasonChangeCheck != result[i][0]:
            id_=result[i][0]
            reason=result[i][1]
            # Check reason flag
            flag=doQueryCheckReasonFlag(myConnection,id_)
            updateReason=''
            if flag==1:
                updateReason=doQueryGetReason(myConnection,id_)
                updateReason='\n'+updateReason+'\n~Submitted~'
            dataReason=reason+updateReason
            insertReason.emit(str(id_),str(dataReason))
            reasonChangeCheck=result[i][0]

def doQueryUpdateReason(conn, reasonData, id_):
    cur=conn.cursor()
    try:
        cur.execute("UPDATE data_downtime set update_dt=('{0}'), update_flag=(1) where id={1}".format(reasonData,id_))
    except Exception as e:
        print ('update reason error : '+ e)
    conn.commit()

# Checking whether the reason has been submitted to database or not
def doQueryCheckReasonFlag(conn, id_):
    cur=conn.cursor()
    cur.execute("select update_flag from public.data_downtime where id={0}".format(id_))
    result = cur.fetchone()
    result = result[0]
    result=int(result)
    return result

# Get reason by id
def doQueryGetReason(conn, id_):
    cur=conn.cursor()
    cur.execute("select update_dt from public.data_downtime where id={0}".format(id_))
    result = cur.fetchone()
    result = result[0]
    return result

# User functions
def changeStatus(status):
    global lbl_status_1,lbl_status_2,lbl_status_3,lbl_status_4,lbl_status,changeStatusCheck
    for i in range(len(status)):
        if int(status[i][0]) != changeStatusCheck[i]:
            if status[i][0] == '1':
                # Red color / downtime
                lbl_status[i].setStyleSheet("background-color: rgb(255, 0, 0);")
            else:
                # Green color = normal
                lbl_status[i].setStyleSheet("background-color: rgb(0, 199, 0);")
            changeStatusCheck[i]=int(status[i][0])

# Python Thread
class StatusThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        checkStatus()

def checkStatus():
    global checkReady,close1_f,close2_f,close3_f,close4_f
    while not (close1_f and close2_f and close3_f and close4_f):
        if checkReady==1:
            status=doQueryCheckStatus(myConnection)
            changeStatus(status)
            # Checking signal for Downtime status
            doQueryCheckDTStatus(myConnection)
            # Reason check
            doQueryCheckReason(myConnection)
            time.sleep(0.5)

class TimeoutThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        timeoutThread()

def timeoutThread():
    global dtSignalStart,close1_f,close2_f,close3_f,close4_f
    while not (close1_f and close2_f and close3_f and close4_f):
        pass
        
# Qt delay Thread
class DelayThread(QThread):
    signal = pyqtSignal(name='signal')
    def __init__(self):
        QThread.__init__(self)

    # run method gets called when we start the thread
    def run(self):
        time.sleep(3)
        self.signal.emit()
        
class InsertReasonPage(QMainWindow, insertReasonForm.Ui_insertReason):
    def closePage(self, mainWin):
        self.close()
        mainWin.setEnabled(True)

    def submitData(self, mainWin):
        global myConnection
        date_=self.lbl_date.text()
        time_=self.lbl_time.text()
        duration=self.lbl_duration.text()
        mesin=self.cb_mesin.currentText()
        kategori=self.cb_kategori.currentText()
        alasan=self.cb_alasan.currentText()
        reason_data=alasan+' '+duration+'\n'+date_+' | '+time_
        lw=mainWin.lw_reason.currentItem()
        # Insert reason data to Database and update flag
        id_=lw.text().split('.')[0] # Get id for current list item
        id_=int(id_)
        doQueryUpdateReason(myConnection, reason_data, id_)
        # Change text in listwidget in Mainwindow
        lw.setText(lw.text()+'\n'+reason_data+'\n~Submitted~')
        mainWin.setEnabled(True)
        self.close()

    def __init__(self,mainWin):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        # Move to the center of window
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.pb_close.clicked.connect(lambda: self.closePage(mainWin))
        self.pb_submit.clicked.connect(lambda: self.submitData(mainWin))
        # Always on top
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

class MinorPage(QMainWindow, minor.Ui_minorForm):

    minorSignalStop = pyqtSignal(name='minorSignalStop')

    def sendminorSignalStop(self):
        global mainwin,close2_f
        self.close()
        close2_f=0
        mainwin.show()

    def __init__(self):
        global minorSignalStop
        super(self.__class__, self).__init__()
        self.setupUi(self)

        # Create Qt signal to emit minor stop signal
        minorSignalStop=self.minorSignalStop
        minorSignalStop.connect(self.sendminorSignalStop)

    def closeEvent(self,event):
        global mainwin
        mainwin.show()

    # For Key press slot
    def keyPressEvent(self, e):
        # print (e.key())
        pass

    # Mouse move slot
    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()
        # print (str(x)+' , '+str(y))

class DowntimePage(QMainWindow, downtime.Ui_downtimeForm):

    dtSignalStop = pyqtSignal(name='dtSignalStop')

    def sendDTStopSignal(self):
        global mainwin
        self.close()
        close2_f=0
        mainwin.show()

    def __init__(self, mainWin):
        global mainwin,dtSignalStop
        super(self.__class__, self).__init__()
        self.setupUi(self)
        #self.mainWin=mainWin
        #self.mainWin.dtSignalStart.connect(self.startThread)
        
        # Create thread object
        #self.delay_thread = DelayThread()
        # Connect the signal from the thread to the finished method
        #self.delay_thread.signal.connect(self.finished)

        # Create Qt signal to emit stop signal
        dtSignalStop=self.dtSignalStop
        dtSignalStop.connect(self.sendDTStopSignal)

    # slot for finished thread
    def finished(self):
        global mainwin,close2_f
        self.close()
        close2_f=0
        mainwin.show()

    def closeEvent(self, event):
        global close3_f
        close3_f=1
        
    # slot for start a thread for delay
    def startThread(self):
        pass
        # Uncomment below line to enable thread
        # self.delay_thread.start()
        
class LoginForm(QMainWindow, loginForm.Ui_login_form):
    def retPress(self):
        global lbl_info,le_login,mainwin,login_form,close2_f,checkReady_main
        # registered_id is from database
        if doQueryLogin(myConnection, self.le_login.text()) == 1:
            login_form.close()
            close2_f=0
            mainwin.show()
            checkReady_main=1
        else:
            lbl_info.setText('ID Number is not registered!\nPlease try again!')

    def __init__(self):
        global le_login,lbl_info
        super(self.__class__, self).__init__()
        self.setupUi(self)
        le_login=self.le_login
        le_login.returnPressed.connect(lambda: self.retPress())
        lbl_info=self.lbl_info

    def closeEvent(self, event):
        global close1_f
        close1_f=1

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
    # access variables inside of the UI's file

    dtSignalStart = pyqtSignal(name='dtSignalStart')
    minorSignalStart = pyqtSignal(name='minorSignalStart')
    insertReason = pyqtSignal(str,str,name='insertReason')
    
    def closeMain(self):
        global login_form,le_login,lbl_info,close1_f,checkReady_main
        self.close()
        close1_f=0
        login_form.show()
        le_login.setText('')
        lbl_info.setText('')
        checkReady_main=0
        
    def senddtSignalStart(self):
        global close3_f
        self.close()
        close3_f=0
        dt_page.show()

    def sendminorSignalStart(self):
        global close4_f,minor_page
        self.close()
        close4_f=0
        minor_page.show()

    def __init__(self):
        global dtSignalStart,minorSignalStart,insertReason,lbl_status_1,lbl_status_2,lbl_status_3,lbl_status_4,lbl_status,checkReady
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        pb_logout=self.pb_logout
        self.pb_logout.clicked.connect(lambda: self.closeMain())

        # Create Qt signal to emit to Downtime Page
        dtSignalStart=self.dtSignalStart
        dtSignalStart.connect(self.senddtSignalStart)
        minorSignalStart=self.minorSignalStart
        minorSignalStart.connect(self.sendminorSignalStart)
        insertReason=self.insertReason
        insertReason.connect(self.addItem)
        # Status label
        lbl_status[0]=self.lbl_status_1
        lbl_status[1]=self.lbl_status_2
        lbl_status[2]=self.lbl_status_3
        lbl_status[3]=self.lbl_status_4
        lbl_status_1=self.lbl_status_1
        lbl_status_2=self.lbl_status_2
        lbl_status_3=self.lbl_status_3
        lbl_status_4=self.lbl_status_4
        # ListWidget
        self.lw_reason.setStyleSheet("""
            QListWidget::item {
                border-style: solid;
                border-width:1px;
                border-color:#00aaff; 
                background-color: #fff;
                color:#000;
                padding:5px 3px 5px 3px;
                font: 12px Comic Sans MS;
                word-wrap:break-word;
                margin-bottom:5px;
            }
            QListWidget::item-selected {
                background-color:#00ff00;
            }
            QListWidget{
                border:2px solid #00aaff;
                padding:5px;
                background-color:#eeeeee;
            }
            """)
        QScroller.grabGesture(self.lw_reason.viewport(), QScroller.LeftMouseButtonGesture)
        self.lw_reason.itemClicked.connect(self.itemClicked)
        
        checkReady=1        
        
    def itemClicked(self,item):
        global insertReasonPage
        print (item.text())
        data=item.text()
        try:
            start = data.index( '~' ) + len( '~' )
            end = data.index( '~', start )
            flag = data[start:end]
        except:
            flag=''

        if flag!='Submitted':
            insertReasonPage.show()
            self.setEnabled(False)
        
    def addItem(self,id_,reason):
        data_=str(id_)+'. '+str(reason)
        self.lw_reason.addItem(data_)
        pass
        
    def closeEvent(self, event):
        global close2_f
        close2_f=1
# I feel better having one of these
def main():
    global mainwin,login_form,le_login,dt_page,minor_page,insertReasonPage
    # a new app instance
    app = QApplication(sys.argv)
    mainwin = MainWindow()
    dt_page = DowntimePage(mainwin)
    minor_page = MinorPage()    
    login_form = LoginForm()
    insertReasonPage = InsertReasonPage(mainwin)
    login_form.show()
    le_login.setFocus()
    # without this, the script exits immediately.
    sys.exit(app.exec_())

# Create new thread for sending data every second
try:
    timeThread=TimeoutThread()
    statusThread=StatusThread()
except Exception as e:
    print ("Error: unable to start thread!")
    print (str(e))
# Start thread
timeThread.start()
statusThread.start()

# python bit to figure how who started This
if __name__ == "__main__":
    main()
