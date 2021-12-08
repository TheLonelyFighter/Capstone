import pyaudio
import numpy as np


def main():
    AUDIO_WINDOW_LENGTH=3
    form_1 = pyaudio.paInt16 # 16-bit resolution
    chans = 1 # 1 channel
    samp_rate = 44100 # 44.1kHz sampling rate
    chunk = 4096 # 2^12 samples for buffer
    record_secs = 1 # seconds to record
    #dev_index = 2 # device index found by p.get_device_info_by_index(ii)
    p = pyaudio.PyAudio()
    
    dev_index = 15
    print("Using device",p.get_device_info_by_index(dev_index))
    wav_output_filename = 'test1.wav' # name of .wav file

    audio = pyaudio.PyAudio() # create pyaudio instantiation

    #method for getting the current date and time
    

    

    chunk_counter = 0
    print("recording")
    recordings=[]
    test=[]
    i=10
    stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                        input_device_index = dev_index,input = True, \
                        frames_per_buffer=chunk)
    while i>0:
        
        frames = []

        # loop through stream and append audio chunks to frame array
        for ii in range(0,int((samp_rate/chunk)*record_secs)):
            data = stream.read(chunk)
            frames.append(data)
        joined_frame=b''.join(frames)
        sound_data = np.frombuffer(data, dtype=np.int16)
        recordings.append(sound_data)
        test.append("test"+str(i))
        if(len(recordings)>AUDIO_WINDOW_LENGTH/record_secs):
            recordings.pop(0)
            test.pop(0)
        # stop the stream, close it, and terminate the pyaudio instantiation
        #concatenate the audio samples and extract features
        #Use knn to classify the audiosamples and other features i.e. temps, humidity, speed etc.
        #print the road condition
        print(test)
        print(len(recordings))
        i=i-1
    stream.stop_stream()
    stream.close()
    audio.terminate()
main()