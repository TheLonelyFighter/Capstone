import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import math as math
import sklearn as sklearn
import random as random
import time
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.model_selection import LeaveOneOut
from scipy import stats
from sklearn.decomposition import PCA


data_path = "DataFrame_01_12.csv"

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

X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.20, random_state=42, shuffle=True, stratify=y)

labels=[]
for label in y:
    if label not in labels:
        labels.append(label)

knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)

predictions = knn.predict(X_test)
c_matrix=metrics.confusion_matrix(y_test, predictions,labels=labels)
#print
#print(c_matrix)


corrects=0
for pred,true in zip(predictions,y_test):
    if(pred==true):
        corrects=corrects+1
#print("accuracy: ",corrects/len(y_test))

"""
plt.figure(figsize=(10, 8))
sb.heatmap(c_matrix, xticklabels=labels, yticklabels=labels, 
            annot=True, fmt='g')
plt.xlabel('Prediction')
plt.ylabel('Label')
plt.show()
"""

# results of the classification don't mean anything. This is a computational benchmark 
def benchmark(classifier,X,iterations=10):
    number_of_samples=len(X)*iterations
    start_time = time.time()
    for i in range(iterations):
        predictions = classifier.predict(X)
    end_time = time.time()
    time_it = end_time-start_time
    return time_it, number_of_samples
first_time,samples=benchmark(knn,X,10)
print(first_time,samples/first_time)

classifiers=[]
for i in range(1,31):
    knn=KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train,y_train)
    classifiers.append(knn)

times=[]
iterations = 10
x_len=len(X)
for classifier in classifiers:
    knn_time,samples=benchmark(classifier,X,iterations)
    times.append(knn_time)

ks=range(1,31)
#print(len(ks),len(times))
for i in ks:
    speed=(iterations*x_len)/times[i-1]
    print("Speed for k =",i,":",speed)