import pyaudio
import numpy as np
import os
import time
import joblib
from preprocessing.get_features import get_features
from KNN_model.load_model import load_by_training
from sklearn.neighbors import KNeighborsClassifier
from scipy.signal import decimate

def main():
    AUDIO_WINDOW_LENGTH=3
    form_1 = pyaudio.paInt16 # 16-bit resolution
    chans = 1 # 1 channel
    samp_rate = 44100 # 44.1kHz sampling rate
    DOWN_SAMPLING_FACTOR = 4
    chunk = 4096 # 2^12 samples for buffer
    record_secs = 1 # seconds to record
    #dev_index = 2 # device index found by p.get_device_info_by_index(ii)
    p = pyaudio.PyAudio()
    cwd = os.getcwd()
    #files = os.listdir(cwd)
    #print(files)
    #knn_classifier=joblib.load(cwd+'/KNN_model/knn_model.pkl' , mmap_mode ='r')
    knn_classifier = load_by_training()
    dev_index = 2
    print("Using device",p.get_device_info_by_index(dev_index))
    wav_output_filename = 'test1.wav' # name of .wav file

    audio = pyaudio.PyAudio() # create pyaudio instantiation

    #method for getting the current date and time
    

    

    chunk_counter = 0
    print("recording")
    recordings=[]
    test=[]
    i=20
    stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                        input_device_index = dev_index,input = True, \
                        frames_per_buffer=chunk)
    while 1>0:
        
        frames = []

        # loop through stream and append audio chunks to frame array
        for ii in range(0,int((samp_rate/chunk)*record_secs)):
            data = stream.read(chunk,exception_on_overflow=False)
            frames.append(data)
        joined_frame=b''.join(frames)
        sound_data = np.frombuffer(joined_frame, dtype=np.int16)
        recordings.append(sound_data)
        test.append("test"+str(i))
        if(len(recordings)>AUDIO_WINDOW_LENGTH/record_secs):
            recordings.pop(0)
            test.pop(0)
        # stop the stream, close it, and terminate the pyaudio instance
        #concatenate the audio samples and extract features
        #big_chungus is a large audiosample in as a numpy array
        big_chungus = np.concatenate(recordings)
        #print(big_chungus)
        time_decimation_start = time.time()
        decimated_signal = decimate(big_chungus,DOWN_SAMPLING_FACTOR)
        time_decimation_end = time.time()
        time_decimation = time_decimation_end-time_decimation_start
        #extract features using tsfel and other libraries
        time_ftr_xtrctn_start = time.time()
        decimated_samp_rate=int(samp_rate/DOWN_SAMPLING_FACTOR)
        features = get_features(decimated_signal,decimated_samp_rate)
        time_ftr_xtrctn_end = time.time()
        time_ftr_xtrctn = time_ftr_xtrctn_end-time_ftr_xtrctn_start
        #print("features:",features)
        #Use knn to classify the audiosamples and other features i.e. temps, humidity, speed etc.
        time_knn_start = time.time()
        predicted_road_type=knn_classifier.predict([features])
        time_knn_end = time.time()
        time_knn = time_knn_end-time_knn_start
        #print the road condition
        print("frame length:",len(decimated_signal))
        print("Time taken by decimation:        ",time_decimation,"seconds")
        print("Time taken by feature extraction:",time_ftr_xtrctn,"seconds")
        print("Time taken by knn model:         ",time_knn,"seconds")
        print("Total computation time:          ",time_knn+time_ftr_xtrctn+time_decimation,"seconds")
        print(predicted_road_type[0])
        #print(test)
        #print(len(recordings))
        #print(recordings[0])
        #print(len(recordings[-1]))
        i=i-1
    stream.stop_stream()
    stream.close()
    audio.terminate()
main()