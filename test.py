# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import NdimToPlane as ndtp

# Do some argparse shennanigans for usability

# Read a matrix from a file (CSV, dat or such ==> check the most used format in data-science)
# Find Eigenvalues / Eigenvectors
# Sort the values, select 2 eigenvectors associated with the biggest eigenvalues
# Norm the selected eigenvectors
# Project the original matrix in the plan generated by the 2 eigenVectors
# Plot (with some formatting options), print biggest eigenvalues, normed eigenvectors, compute loss of information

def GenerateNRandTestData(shape=(100, 5)):
    """
    Generate a random matrix (with normally distributed values) of the passed shape.
    """
    testData = pd.DataFrame(np.random.randn(shape[0], shape[1]))
    return testData

def Generate3ClustersDataSet(shape=(400, 5)):
    """
    Generate a random matrix with 3 clusters more or less distinguishable
    """
    testData = np.random.randn(shape[0], shape[1])
    testData[99:199,:] = 2* np.random.randn(100, shape[1]) +8
    testData[200:299,:] = -4 * np.random.randn(99, shape[1]) -16
    testData[300:399, :] = -1 * np.random.randn(99, shape[1]) -2
    
    return pd.DataFrame(testData)

def SaveTestData(testData, path='Example/testSet.csv'):
    """
    Returns True if the data passed were successfully saved in the Example folder. Else, it returns False.
    """
    try:
        testData.to_csv(path, mode='w+', sep=',', index = False, header=False)
    except Exception as e:
        print("Could not save test data.")
        print(e)
        return False
    return True

def ReadTestData(path='Example/testSet.csv'):
    try:
        testData = np.genfromtxt(path, delimiter=',')
    except Exception as e:
        print(e)
        return 0
    return testData
    
    
if __name__ == "__main__":
    
    #testData = GenerateNRandTestData()
    testData = Generate3ClustersDataSet()
    SaveTestData(testData)
    
    projectedTestData = ndtp.Get2DProjectedMatrix(testData)
    SaveTestData(pd.DataFrame(projectedTestData), path='Example/projectedTestSet.csv')
    
    
    ndtp.Plot2DMatrix(projectedTestData)
    print(ndtp.GetInformationLoss(testData))
    
    