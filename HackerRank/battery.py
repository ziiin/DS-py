'''
This is solution to problem https://www.hackerrank.com/challenges/battery
Status : Incomplete
'''

import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

def load ():
    data = np.loadtxt ("data/battery_train.txt", \
            delimiter=",")
    #print data
    charged, ran = (data[:,0], data [:,1])

    '''
    print "Charged list: ", charged
    print "Total: ", len(charged)

    print "##########"
    
    print "Ran list: ", ran
    print "Total: ", len(ran)
    '''
    return data

def plot (data):
    charged_X, ran_Y = (data[:,0], data [:,1])
    print "LEN : ", len(charged_X), len(ran_Y)
    regr = linear_model.LinearRegression()
    #regr.fit(charged_X[:20], ran_Y[:20])
    # getting exception here:
    # ValueError: Found arrays with inconsistent numbers of samples
    plt.scatter(charged_X, ran_Y,  color='black')
    #plt.plot(charged_X, regr.predict(charged_X), color='blue', \
    #                 linewidth=3)
    plt.show()


plot (load())
