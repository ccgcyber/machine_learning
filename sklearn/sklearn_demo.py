# -*- coding: utf-8 -*-
from sklearn.cluster import KMeans
from sklearn.externals import joblib
import numpy
import time
import matplotlib.pyplot as plt

if __name__ == '__main__':
    ## step 1: Load data
    print "step 1: load data..."

    dataSet = []
    fileIn = open('./data.txt')
    for line in fileIn.readlines():
        lineArr = line.strip().split(' ')
        dataSet.append([float(lineArr[0]), float(lineArr[1])])

    # Set different k values ​​to operate
    for k in range(2,10):
        clf = KMeans(n_clusters=k) # Set k
        s = clf.fit(dataSet) # Load the data collection
        numSamples = len(dataSet)
        centroids = clf.labels_
        print centroids,type(centroids) # Show center point
        print clf.inertia_  # Show clustering effects
        mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
        # Draw all the sample points that belong to the same class to draw the same color
        for i in xrange(numSamples):
            #markIndex = int(clusterAssment[i, 0])
            plt.plot(dataSet[i][0], dataSet[i][1], mark[clf.labels_[i]]) #mark[markIndex])
        mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
        # Draw a particle, with a special pattern
        centroids =  clf.cluster_centers_
        for i in range(k):
            plt.plot(centroids[i][0], centroids[i][1], mark[i], markersize = 12)
            #print centroids[i, 0], centroids[i, 1]
        plt.show()















    #print s
    #print clf.cluster_centers_
    #print clf.labels_

    #print "step 2: clustering..."
    #dataSet = mat(dataSet)
    # mat Function, the array into a matrix
