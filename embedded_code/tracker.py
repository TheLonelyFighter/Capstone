import serial
import time
import hashlib

# define constants
SERIAL_DEVICE = '/dev/ttyS0' # for pi zero w
# SERIAL_DEVICE = '/dev/ttyAMA0' # for pi 3+ 
BAUD_RATE = 115200 # for SIM7000 family
# BAUD_RATE = 9600 # for SIM800 family
TIMEOUT = 10 # wait for 10 seconds before giving up on a command (it is high to account for the GPS latency)
ENTER_KEY = '\r\n'
FULL_FUNC = 'AT+CFUN=1'
GPS_LOCATION_CMD = 'AT+CGNSINF'
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
    print("rxbuffer:",rxbuffer)
    rxbuffer = sr_dev.read(100) # read the max characters allowed
    print("rxbuffer after read:",rxbuffer)
    print("reading therest of the buffer:",sr_dev.read(100)) # read any additional characters to empty out buffer

    return rxbuffer.decode('UTF-8')

def get_location():
    
    lat = 0
    lgt = 0
    satellites=0
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
    else:
        print("no response")
        lat = 0
        lgt = 0
        satellites=0
    return [lat, lgt, satellites]

def send_location(loc, base_url):
    # loc = tuple(lat, long)
    #print(loc)
    # get ID
    imei = "salt"+send_command(GET_IMEI)
    hash = hashlib.sha1(imei.encode("UTF-8")).hexdigest()
    uid = hash[:10]
    url = base_url+'?id='+uid+'&x='+str(loc[0])+'&y='+str(loc[1])
    # start post request
    send_command('AT+CIPSHUT')
    send_command(SET_CMEE)
    send_command(SET_SAPBR%("CONTYPE","GPRS"))
    send_command(SET_SAPBR%("APN","hologram"))
    while( 'OK' not in send_command(APN_BEARER_OPEN)):
        continue
    send_command(HTTP_INIT)
    send_command(HTTP_PARAM%("CID","1"))
    send_command(HTTP_URL%(url))
    send_command(HTTP_START)
    result = send_command(HTTP_READ)
    send_command(HTTP_END)
    send_command(APN_BEARER_CLOSE)
    #print(result)

if __name__ == "__main__":
    while(send_command(GPS_ON)==None or send_command(GPS_ON)==''):
        continue
    response=send_command("AT+CGNSHOT")
    print(response)
    iterator=0
    while iterator<100:
        iterator = iterator +1
        #send_location(get_location(), url)
        start= time.time()
        coordinates=get_location()
        end=time.time()
        print("time:",end-start)
        print("latitude:",coordinates[0],"longitude:",coordinates[1])
        print("satellites in view:",coordinates[2])
        
    while(send_command(GPS_OFF)==None or send_command(GPS_OFF)==''):
        continue