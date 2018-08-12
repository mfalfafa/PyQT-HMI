import serial
import time

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