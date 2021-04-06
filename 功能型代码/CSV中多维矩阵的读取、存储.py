import numpy





mfcc = numpy.loadtxt(open("mfcc.csv", "rb"), delimiter=",", skiprows=0)


numpy.savetxt('mfcc_1.csv', mfcc, delimiter= ',')