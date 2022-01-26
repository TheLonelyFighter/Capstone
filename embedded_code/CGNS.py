import serial
import time
import hashlib
from math import radians, cos, sin, asin, sqrt
from datetime import datetime
import time
# define constants
SERIAL_DEVICE = '/dev/ttyS0' # for pi zero w
# SERIAL_DEVICE = '/dev/ttyAMA0' # for pi 3+ 
BAUD_RATE = 115200 # for SIM7000 family
# BAUD_RATE = 9600 # for SIM800 family
TIMEOUT = 10 # wait for 10 seconds before giving up on a command (it is high to account for the GPS latency)
ENTER_KEY = '\r\n'
FULL_FUNC = 'AT+CFUN=1'
GPS_LOCATION_CMD = 'AT+CGNSINF'
#returns GNSS runs status, Fix status, UTC date and time, latitude, longitude,
#MSL altitude, speed over ground, course over ground, fix mode, Reserved1, HDOP, PDOP, VDOP,
#Reserved2, GNSS satellites in view, GPS satellites used, glonass satellites used, Reserved3,
#C/N0 max, HPA, VPA
GPS_ON = 'AT+CGNSPWR=1'
GPS_OFF = 'AT+CGNSPWR=0'
GET_IMEI = 'AT+GSN'
SET_CMEE = 'AT+CMEE=1'
SET_SAPBR = 'AT+SAPBR=3,1,"%s","%s"'
APN_BEARER_OPEN = 'AT+SAPBR=1,1'
APN_BEARER_CLOSE = 'AT+SAPBR=0,1'
HTTP_INIT = 'AT+HTTPINIT'
HTTP_PARAM = 'AT+HTTPPARA="%s",%s'
HTTP_URL = 'AT+HTTPPARA="URL","%s"'
HTTP_DATA = 'AT+HTTPDATA=%s'
HTTP_START = 'AT+HTTPACTION=1'
HTTP_END = 'AT+HTTPTERM'
HTTP_READ = 'AT+HTTPREAD'

def send_command(cmd):
    # Define serial device
    sr_dev = serial.Serial(SERIAL_DEVICE, baudrate=BAUD_RATE, timeout=1)
    # Transmit command to the SIM Module
    message = cmd+ENTER_KEY
    sr_dev.write(message.encode("UTF-8"))
    # Receive output from the SIM Module
    rxbuffer = sr_dev.read(len(cmd)) # this will be the echo of the command
    
    rxbuffer = sr_dev.read(100) # read the max characters allowed
    print("rxbuffer after read:",rxbuffer)
    sr_dev.read(100) # read any additional characters to empty out buffer

    return rxbuffer.decode('UTF-8')

def write_command(cmd):
    # Define serial device
    sr_dev = serial.Serial(SERIAL_DEVICE, baudrate=BAUD_RATE, timeout=1)
    # Transmit command to the SIM Module
    message = cmd+ENTER_KEY
    sr_dev.write(message.encode("UTF-8"))
    
def read_location():
    lat = 0
    lgt = 0
    satellites=0
    datetime=0
    # Define serial device
    sr_dev = serial.Serial(SERIAL_DEVICE, baudrate=BAUD_RATE, timeout=1)
    
    rxbuffer = sr_dev.read(len(GPS_LOCATION_CMD)) # this will be the echo of the command
    print(rxbuffer)
    rxbuffer = sr_dev.read(100) # read the max characters allowed
    print("rxbuffer after read:",rxbuffer)
    sr_dev.read(100) # read any additional characters to empty out buffer

    data = rxbuffer.decode('UTF-8')
    if (len(data)>4): # sometimes due to not enough power device does not respond
        print("response:",len(data))
        #print(data[3],data[4])
        lat = 0 if data[3] == '' else float(data[3])
        lgt = 0 if data[4] == '' else float(data[4])
        satellites=0 if data[14] == '' else float(data[14])
        datetime = 0 if data[2] == '' else data[2]
    else:
        print("no response")
        lat = 0
        lgt = 0
        satellites=0
        datetime=0
    return [lat, lgt, satellites, datetime]

def get_location():
    
    lat = 0
    lgt = 0
    satellites=0
    datetime=0
     # it takes a while before the GPS is ready wait for minimum 5-10 minutes
    #data = send_command(GPS_LOCATION_CMD).split(',')
    data = send_command(GPS_LOCATION_CMD).split(',')
    print(type(data))
    #time.sleep(1)
    if (len(data)>4): # sometimes due to not enough power device does not respond
        print("response:",len(data))
        #print(data[3],data[4])
        lat = 0 if data[3] == '' else float(data[3])
        lgt = 0 if data[4] == '' else float(data[4])
        satellites=0 if data[14] == '' else float(data[14])
        datetime = 0 if data[2] == '' else data[2]
    else:
        print("no response")
        lat = 0
        lgt = 0
        satellites=0
        datetime=0
    return [lat, lgt, satellites, datetime]
def get_distance(coordinates):
    lon1=coordinates[0][1]
    lon2=coordinates[1][1]
    lat1=coordinates[0][0]
    lat2=coordinates[1][0]
    #harvesine formula
    dlon=lon2-lon1
    dlat=lat2-lat1
    a=sin(dlat/2)**2+cos(lat1)*cos(lat2)*sin(dlon/2)**2
    c=2*asin(sqrt(a))
    #radius of earth in kilometers
    r=6371*1000
    return (c*r)

def get_speed(coordinate_data):
    distance=get_distance(coordinate_data)
    
    #yyyy,mm,dd,hh,mm,ss
    time1_list=[coordinate_data[0][3][0:4],coordinate_data[0][3][4:6],coordinate_data[0][3][6:8],coordinate_data[0][3][8:10],coordinate_data[0][3][10:12],coordinate_data[0][3][12:14]]
    time2_list=[coordinate_data[1][3][0:4],coordinate_data[1][3][4:6],coordinate_data[1][3][6:8],coordinate_data[1][3][8:10],coordinate_data[1][3][10:12],coordinate_data[1][3][12:14]]
    d1=datetime(int(time1_list[0]),int(time1_list[1]),int(time1_list[2]),int(time1_list[3]),int(time1_list[4]),int(time1_list[5])).timestamp()
    d2=datetime(int(time2_list[0]),int(time2_list[1]),int(time2_list[2]),int(time2_list[3]),int(time2_list[4]),int(time2_list[5])).timestamp()
    time=d2-d1
    return [distance/time,time,distance]

if __name__ == "__main__":
    while(send_command(GPS_ON)==None or send_command(GPS_ON)==''):
        continue
    response=send_command("AT+CGNSHOT")
    print(response)
    iterator=0
    coordinate_data=[]
    while iterator<100:
        iterator = iterator +1
        #send_location(get_location(), url)
        start= time.time()
        coordinates=get_location()
        time.sleep(5)
        end=time.time()
        print("time:",end-start)
        print("latitude:",coordinates[0],"longitude:",coordinates[1])
        print("satellites in view:",coordinates[2])
        print("Datetime:",coordinates[3])
        if coordinates[3]==0:
            coordinate_data=[]
        else:
            if len(coordinate_data)==2:
                coordinate_data.pop(0)
            coordinate_data.append(coordinates)
        if len(coordinate_data)==2:
            speed=get_speed(coordinate_data)
            print("speed:",speed)
    while(send_command(GPS_OFF)==None or send_command(GPS_OFF)==''):
        continue
