#coding:utf-8
from numpy import *
import time
import matplotlib.pyplot as plt


# Calculate the European distance
def euclDistance(vector1, vector2):
    return sqrt(sum(power(vector2 - vector1, 2)))
    # 0ρ = sqrt( (x1-x2)^2+(y1-y2)^2 )　|x| = √( x2 + y2 )
    # power Calculate the second order of the list

# Initialized centroid random samples
def initCentroids(dataSet, k):
    numSamples, dim = dataSet.shape # Gets the total number of rows in the data collection
    centroids = zeros((k, dim))
    for i in range(k):
        index = int(random.uniform(0, numSamples))
        # uniform() The method will randomly generate the next real number，it is within the range [x,y]。
        centroids[i, :] = dataSet[index, :]
    return centroids

# k-means cluster
def kmeans(dataSet, k):
    numSamples = dataSet.shape[0]# Rows

    clusterAssment = mat(zeros((numSamples, 2))) #

    clusterChanged = True #Stop loop flag

    ## step 1: init, Initialize k particles
    centroids = initCentroids(dataSet, k)

    while clusterChanged:
        clusterChanged = False
        ## for each 行
        for i in xrange(numSamples):
            minDist  = 100000.0 # Set a maximum value
            minIndex = 0
            ## for each centroid
            ## step 2: Looking for the closest centroid
            for j in range(k):
                distance = euclDistance(centroids[j, :], dataSet[i, :])
                # will centroids （K initialize centroid） The j line and dataset （ Data collection ） Of the E line of Euclidean distance，Returns the numerical distance
                if distance < minDist:
                # Find the nearest spot，record it。
                    minDist  = distance
                    minIndex = j


            ## step 3: update its cluster # Update this cluster
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True  # clusterAssment Is a matrix of n rows and 2 columns  Assment Evaluation
                clusterAssment[i, :] = minIndex, minDist**2 # Assigned a new mark

        ## step 4: update centroids
        for j in range(k):
            # The average of all the values ​​belonging to this particle is calculated as a new particle
            pointsInCluster = dataSet[nonzero(clusterAssment[:, 0].A == j)[0]]
            centroids[j, :] = mean(pointsInCluster, axis = 0)

    print 'Congratulations, cluster complete!'
    return centroids, clusterAssment

# Two - point k - means algorithm
def biKmeans(dataSet, k):
    numSamples = dataSet.shape[0]
    # first column stores which cluster this sample belongs to,
    # second column stores the error between this sample and its centroid
    clusterAssment = mat(zeros((numSamples, 2)))
    # Initialize the cluster evaluation table with the value of 0 for the row line 2 column matrix
    # step 1: the init cluster is the whole data set
    # The initial cluster is the entire data set,Count
    centroid = mean(dataSet, axis = 0).tolist()[0]
    # mean After processing is matrix([[  22.32695245,  114.25989385]]) Need to use tolist converted into a heart
    centList = [centroid]
    # Set the initial center list, There is at least one cluster

    for i in xrange(numSamples):
        clusterAssment[i, 1] = euclDistance(mat(centroid), dataSet[i, :])**2
        # Calculate the distance between each point and the current figure
        # print mat(centroid), dataSet[i, :]
        # [[  22.32695245  114.25989385]] [[  22.325637  114.25936 ]]


    while len(centList) < k:
        # Gradually increase the number of clusters，Until the k value is reached
        # min sum of square error
        minSSE = 100000.0
        numCurrCluster = len(centList)
        # for each cluster
        for i in range(numCurrCluster):
            # step 2: get samples in cluster i
            pointsInCurrCluster = dataSet[nonzero(clusterAssment[:, 0].A == i)[0], :]
            # nonzero(a) :: Returns the subscript of the element whose value is not zero in array a, and its return value is a length a.ndim
            # (The number of axes of array a), each element of the tuple is an array of integers whose value is the value of the index of the nonzero element on the corresponding axis
            # point :: the final value is
            #       matrix([[  22.325637,  114.25936 ],
            #       [  22.325522,  114.259091],
            #       [  22.328594,  114.256648],

            # step 3: cluster it to 2 sub-clusters using k-means
            # The k-means clustering on a given cluster will be divided into two
            centroids, splitClusterAssment = kmeans(pointsInCurrCluster, 2)


            # step 4: calculate the sum of square error after split this cluster
            # Calculate the total error after dividing the cluster into two
            splitSSE = sum(splitClusterAssment[:, 1])
            notSplitSSE = sum(clusterAssment[nonzero(clusterAssment[:, 0].A != i)[0], 1])
            currSplitSSE = splitSSE + notSplitSSE

            # step 5: find the best split cluster which has the min sum of square error
            # Find the optimal segmentation clustering with the least squares error and the least square sum
            if currSplitSSE < minSSE:
                minSSE = currSplitSSE
                bestCentroidToSplit = i
                bestNewCentroids = centroids.copy()
                bestClusterAssment = splitClusterAssment.copy()

        # step 6: modify the cluster index for adding new cluster
        # Modify the cluster index to add a new cluster
        bestClusterAssment[nonzero(bestClusterAssment[:, 0].A == 1)[0], 0] = numCurrCluster
        bestClusterAssment[nonzero(bestClusterAssment[:, 0].A == 0)[0], 0] = bestCentroidToSplit

        # step 7: update and append the centroids of the new 2 sub-cluster
        # Update and add the new 2 subgroup of centroids
        centList[bestCentroidToSplit] = bestNewCentroids[0, :]
        centList.append(bestNewCentroids[1, :])

        # step 8: update the index and error of the samples whose cluster have been changed
        # Updates the indexes and errors of the samples that have changed the cluster
        clusterAssment[nonzero(clusterAssment[:, 0].A == bestCentroidToSplit), :] = bestClusterAssment

    print 'Congratulations, cluster using bi-kmeans complete!'
    return mat(centList), clusterAssment


# show your cluster only available with 2-D data
def showCluster(dataSet, k, centroids, clusterAssment):
    numSamples, dim = dataSet.shape
    if dim != 2:
        print "Sorry! I can not draw because the dimension of your data is not 2!"
        return 1

    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    if k > len(mark):
        print "Sorry! Your k is too large! please contact Zouxy"
        return 1

    # Draw all the sample points that belong to the same class to draw the same color
    for i in xrange(numSamples):
        markIndex = int(clusterAssment[i, 0])
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])

    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']

    # draw the centroids
    # Draw a particle, with a special pattern
    for i in range(k):
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize = 12)
        print centroids[i, 0], centroids[i, 1]

    plt.show()

if __name__ == '__main__':
    ## step 1: Load data
    print "step 1: load data..."
    dataSet = []
    fileIn = open('./data.txt')
    for line in fileIn.readlines():
        lineArr = line.strip().split(' ')
        # Python strip() Method to remove the character specified by the head of the string (default is a space)
        # And then follow the space between the data as a separator。
        dataSet.append([float(lineArr[0]), float(lineArr[1])])
        # Returns each set of data added to the dataset as a list. Form a two-dimensional array
    ## step 2: Start clustering...
    print "step 2: clustering..."
    dataSet = mat(dataSet)
    # mat Function, the array into a matrix

    k = 3

    # This part can choose to use k mean or two k average

    centroids, clusterAssment = kmeans(dataSet, k)
    #centroids, clusterAssment = biKmeans(dataSet, k)

    ## step 3: show the result
    print "step 3: show the result..."
    showCluster(dataSet, k, centroids, clusterAssment)
    print 'end'
