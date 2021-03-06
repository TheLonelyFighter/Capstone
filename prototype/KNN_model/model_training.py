import pandas as pd
import math as math
import os
import joblib
from sklearn.neighbors import KNeighborsClassifier
cwd = os.getcwd()
files = os.listdir(cwd)
print("Files in %r: %s" % (cwd, files))
data_path = cwd+"/Test_frame/KNN_model/df-4_wl-3s_19.1.2022.csv"
data = pd.read_csv(data_path)

def getSamplesAndLabels(data,variables,label):
    x=[]
    y=[]
    for row in range(len(data)):
        sample=[]
        nan=False
        for variable in variables:
            point = data[variable][row]
            sample.append(data[variable][row])
            if math.isnan(point):
                nan=True
        if(not nan):
            x.append(sample)
            y.append(data[label][row])
        
    return x,y

variables = ["RMS","RMS_filt","Zero-Cross","Zero-Cross_filt","Spectral_centroid","Spectral_centroid_filt","Spectral_slope","Spectral_slope_filt","Spectral_spread","Spectral_spread_filt","STD","STD_filt"]

X,y=getSamplesAndLabels(data,variables,"Surface")

knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(X,y)

joblib.dump(knn,cwd+'/Test_frame/KNN_model/'+'knn_model.pkl')
