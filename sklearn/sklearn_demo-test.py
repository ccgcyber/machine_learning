# -*- coding: utf-8 -*-
from sklearn.cluster import KMeans
from sklearn.externals import joblib
import numpy ,time
import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift, estimate_bandwidth
import numpy as np

if __name__ == '__main__':
    ## step 1: Load data
    print "step 1: load data..."

    dataSet = []
    fileIn = open('./data.txt')
    for line in fileIn.readlines():
        lineArr = line.strip().split(' ')
        dataSet.append([float(lineArr[0]), float(lineArr[1])])

    numSamples = len(dataSet)
    X = np.array(dataSet) # The list type is converted to an array array type

    bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)
    clf = MeanShift(bandwidth=bandwidth, bin_seeding=True,cluster_all=True).fit(X)

    centroids = clf.labels_
    print centroids,type(centroids) # Show the clustering of each point
    # Calculate its automatically generated k, and the number of clusters less than 3 exclusion
    arr_flag = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in clf.labels_:
        arr_flag[i]+=1
    k = 0
    for i in arr_flag:
        if(i > 3):
            k +=1
    print k

    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    # Draw all the sample points that belong to the same class to draw the same color
    for i in xrange(numSamples):
        plt.plot(dataSet[i][0], dataSet[i][1], mark[clf.labels_[i]]) #mark[markIndex])
    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
    # Draw a particle, with a special pattern
    centroids =  clf.cluster_centers_
    for i in range(k):
        plt.plot(centroids[i][0], centroids[i][1], mark[i], markersize = 12)
    print centroids # Show center point coordinates
    plt.show()















    #print s
    #print clf.cluster_centers_
    #print clf.labels_

    #print "step 2: clustering..."
    #dataSet = mat(dataSet)
    # mat 函数，将数组转化为矩阵
