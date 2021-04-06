from sklearn import preprocessing
import numpy as np

mfcc = np.loadtxt(open("mfcc1.csv", "rb"), delimiter=",", skiprows=0)

# print(my_matrix)
print(mfcc.shape)
data_normal = preprocessing.scale(mfcc)  # data是多维数据

np.savetxt('mfcc_to_1.csv', data_normal, delimiter= ',')
print(data_normal.shape)