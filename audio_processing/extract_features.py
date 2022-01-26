from scipy import signal
from tsfel.feature_extraction import features as tsfelf
import numpy as np

def hpf(arr,fs,lf,order):
    wbut = lf
    bbut, abut = signal.butter(order,wbut, btype='highpass', fs=fs)
    return signal.filtfilt(bbut, abut, arr)

def get_features(sig,label,fs = 44100):
    
    s_f = hpf(sig, fs, 65, 2)

    Zero_Cross = tsfelf.zero_cross(sig)
    Zero_Cross_filt = tsfelf.zero_cross(s_f)
            
    Spectral_centroid = tsfelf.spectral_centroid(sig, fs)
    Spectral_centroid_filt = tsfelf.spectral_centroid(s_f, fs)

    Spectral_spread = tsfelf.spectral_spread(sig, fs)
    Spectral_spread_filt = tsfelf.spectral_spread(s_f, fs) 
            
    STD = np.std(sig)
    STD_filt = np.std(s_f)
    
    RMS = tsfelf.rms(sig)
    RMS_filt= tsfelf.rms(s_f)
    
    kurt_filt= tsfelf.kurtosis(s_f)
    
    return [label, RMS, RMS_filt, Zero_Cross, Zero_Cross_filt, Spectral_centroid, 
     Spectral_centroid_filt, Spectral_spread, Spectral_spread_filt, STD, STD_filt, kurt_filt]