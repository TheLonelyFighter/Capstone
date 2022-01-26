import pyaudio
import wave
import ntplib
import time
import CGNS

GPS_ON = 'AT+CGNSPWR=1'
GPS_LOCATION_CMD = 'AT+CGNSINF'
GPS_OFF = 'AT+CGNSPWR=0'
form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 # 1 channel
samp_rate = 44100 # 44.1kHz sampling rate
chunk = 4096 # 2^12 samples for buffer
record_secs = 3 # seconds to record
dev_index = 2 # device index found by p.get_device_info_by_index(ii)
wav_output_filename = 'test1.wav' # name of .wav file

audio = pyaudio.PyAudio() # create pyaudio instantiation

#method for getting the current date and time
def get_filename(speed="-"):
    # ntp_client = ntplib.NTPClient() 
    # response = ntp_client.request('pool.ntp.org')
    #use local time, otherwise timeout from server will terminate program
    timestamp = time.ctime()
    print(timestamp) 
    array = timestamp.split(" ")
    timestamp = array[4] + "_" + array[3] + "-" + array[1] + "-" + array[2]+"-speed:_"+str(speed)+"_"
    return timestamp
# create pyaudio stream
if __name__ == "__main__":
    while(CGNS.send_command(GPS_ON)==None or CGNS.send_command(GPS_ON)==''):
        continue
    response=CGNS.send_command("AT+CGNSHOT")
    print(response)
    stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                        input_device_index = dev_index,input = True, \
                        frames_per_buffer=chunk)

    chunk_counter = 0
    print("recording")
    coordinate_data=[]
    while 1>0:
        start = time.time()
        frames = []
        #CGNS.get_location()
        #CGNS.write_command(GPS_LOCATION_CMD)
        # loop through stream and append audio chunks to frame array
        for ii in range(0,int((samp_rate/chunk)*record_secs)):
            data = stream.read(chunk)
            frames.append(data)

        print("finished recording")

        # stop the stream, close it, and terminate the pyaudio instantiation
        stream.stop_stream()
        stream.close()
        audio.terminate()
        coordinates=CGNS.get_location()
        speed=["-"]
        if coordinates[3]==0:
            coordinate_data=[]
        else:
            if len(coordinate_data)==2:
                coordinate_data.pop(0)
            coordinate_data.append(coordinates)
        if len(coordinate_data)==2:
            speed=CGNS.get_speed(coordinate_data)
        if speed[0]*3.6>130:
            speed=['-']
        wav_output_filename= str(get_filename(speed[0]))+".wav"
        print(wav_output_filename)
        # save the audio frames as .wav file
        wavefile = wave.open('recordings/' + wav_output_filename,'wb')
        wavefile.setnchannels(chans)
        wavefile.setsampwidth(audio.get_sample_size(form_1))
        wavefile.setframerate(samp_rate)
        wavefile.writeframes(b''.join(frames))
        wavefile.close()
        print("Saved chunk " + str(chunk_counter) + ':  ' + wav_output_filename )
        chunk_counter += 1

        audio = pyaudio.PyAudio() # create pyaudio instantiation
        stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                        input_device_index = dev_index,input = True, \
                        frames_per_buffer=chunk)
        end=time.time()
        print("spent time:",str(end-start))