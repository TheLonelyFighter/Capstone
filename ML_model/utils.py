import numpy as np
from scipy import signal

#Just some filters

# band-pass filter
def bpf(arr, fs, lf, hf, order):    # arr = signal, fs = frequency
    wbut = [lf, hf]                 # lf = lowpass, hf = highpass
    bbut, abut = signal.butter(order, wbut, btype ='bandpass', fs = fs)

    return signal.filtfilt(bbut, abut, arr)

# High-pass filter
def hpf(arr, fs, lf, order):        
    wbut = lf
    bbut, abut = signal.butter(order, wbut, btype ='highpass', fs =fs)

    return signal.filtfilt(bbut, abut, arr)

# Moving average filter
def moving_average(s, w):           # s = signal, w = window
    return np.convolve(s, np.ones(w), 'valid') / w    

    ######