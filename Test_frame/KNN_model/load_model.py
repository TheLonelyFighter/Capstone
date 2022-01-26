from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import math as math
import os


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
def load_by_training():
    cwd = os.getcwd()
    files = os.listdir(cwd)
    print("Files in %r: %s" % (cwd, files))
    data_path = cwd+"/KNN_model/DataFrame_26_01_22.csv"
    data = pd.read_csv(data_path)
    variables = ["RMS","RMS_filt","Zero_Cross","Zero_Cross_filt","Spectral_centroid","Spectral_centroid_filt","Spectral_spread","Spectral_spread_filt","STD","STD_filt","kurt_filt"]

    X,y=getSamplesAndLabels(data,variables,"Label")

    knn=KNeighborsClassifier(n_neighbors=3)
    knn.fit(X,y)
    return knn