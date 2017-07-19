#coding=utf-8
from numpy import *
import operator

def createDataSet():
    group = array([[1.0, 0.9], [1.0, 1.0], [0.1, 0.2], [0.0, 0.1]])
    labels = ['C','C','A','A']
    #print group,labels
    return group,labels
#inputX :: Represents the input vector (that is, we want to determine which class it belongs to)
#dataSet :: Indicates training samples
#label :: Indicates the label of the training sample
#k :: Is the nearest neighbor parameter，Choose the most recent k
def kNNclassify(inputX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]# Calculate there are several training data
    # Began to calculate the Euclidean distance
    diffMat = tile(inputX, (dataSetSize,1)) - dataSet
    
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)# The matrix adds each row of vectors
    distances = sqDistances ** 0.5
    # Euclidean distance is calculated
    sortedDistance = distances.argsort()
    classCount = {}
    for i in xrange(k):
        voteLabel = labels[sortedDistance[i]]
        classCount[voteLabel] = classCount.get(voteLabel,0) + 1
    res = max(classCount)
    return res

def main():
    group,labels = createDataSet()
    t = kNNclassify([0.5,0.5],group,labels,3)
    print t

if __name__=='__main__':
    main()
