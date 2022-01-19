from tsfel.feature_extraction import features as tsfelf
import numpy as np
from scipy import signal

def hpf(arr, fs, lf, order):
    wbut = lf
    bbut, abut = signal.butter(order, wbut, btype ='highpass', fs =fs)

    return signal.filtfilt(bbut, abut, arr)
#the function is otherwise the same as in the ML_model folder but now the function returns a list
def get_features(sig,fs=44100):
    features = ["RMS", "RMS_filt","Zero-Cross", "Zero-Cross_filt", "Spectral_centroid",\
                "Spectral_centroid_filt", "Spectral_slope", \
                    "Spectral_slope_filt", "Spectral_spread", \
                        "Spectral_spread_filt", "STD", "STD_filt"]

        
    s_f = hpf(sig, fs, 65, 2)
    RMS = tsfelf.rms(sig)
    RMS_filt= tsfelf.rms(s_f)
    
    Zero_Cross = tsfelf.zero_cross(sig)
    Zero_Cross_filt = tsfelf.zero_cross(s_f)
            
    Spectral_centroid = tsfelf.spectral_centroid(sig, fs)
    Spectral_centroid_filt = tsfelf.spectral_centroid(s_f, fs)
            
    Spectral_slope = tsfelf.spectral_slope(sig, fs)
    Spectral_slope_filt = tsfelf.spectral_slope(s_f, fs) 
            
    Spectral_spread = tsfelf.spectral_spread(sig, fs)
    Spectral_spread_filt = tsfelf.spectral_spread(s_f, fs) 
            
    STD = np.std(sig)
            
    STD_filt = np.std(s_f)

    return [RMS, RMS_filt, Zero_Cross, Zero_Cross_filt, Spectral_centroid, 
     Spectral_centroid_filt,Spectral_slope, Spectral_slope_filt, Spectral_spread, Spectral_spread_filt,  
      STD, STD_filt]