#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 23:37:12 2018

Problem: 
 A polynomial of 'n' sided polynomial, where each of the vertices is colored one of three colours(red, blue and yellow) at random.
 k>3 dots are placed inside the polygon. Using this dots as cornors the polygon is divided into nonoverlapping triangles.
 Can one color the inside dots so as to create two complete triangles and no more? (complete triangle has all 3 vertices of different color.)
 
The aim to to determine if a solution exisits or not


input: A triangularized graph of a polygon given as adjecency list and the list of points which already have color to begin with.
output: Yes/ No if the solution exists or not.


@author: meghapanda
"""





# import all the


import numpy as np
import unittest
import sys



class Test(unittest.TestCase):
    def test(self):
        # pass Test
        inputFile=open("/Users/meghapanda/Documents/Msc_Project/triangulation/test_input.txt")
        output= ({'A': ['B', 'C', 'E', 'F'], 'C': ['A', 'D', 'E', 'G'], 'B': ['A', 'F', 'D'], 'E': ['A', 'C', 'F', 'G'], 'D': ['B', 'C', 'G', 'F'], 'G': ['C', 'E', 'D', 'F'], 'F': ['A', 'B', 'D', 'E', 'G']}, {'A': 'Red', 'C': 'Yellow', 'B': 'Red', 'D': 'Blue'}, [['A', 7], ['B', 5], ['C', 7], ['D', 7], ['E', 7], ['F', 9], ['G', 7]])
        self.assertEqual(readInput(inputFile), output)
        self.assertEqual(checkSolution(output[0],output[1],output[2]), True)
        self.assertEqual(checkInput(output[0]), True)
        
        ## Fail Test
        inputFile=open("/Users/meghapanda/Documents/Msc_Project/triangulation/test_input_fail.txt")
        outputFail= ({'A': ['B', 'C'], 'C': ['A', 'B'], 'B': ['A', 'C']}, {'A': 'Red', 'C': 'Yellow', 'B': 'Red'}, [['A', 3], ['B', 3], ['C', 3]])
        self.assertEqual(readInput(inputFile), outputFail)
        self.assertEqual(checkSolution(outputFail[0],outputFail[1],outputFail[2]), False)
        
        
        ## failed matrix
        mat = {'A': ['B', 'C', 'E'], 'B': ['A', 'B'], 'C': ['B', 'C', 'E'], 'E': ['B', 'C']}
        self.assertEqual(checkInput(mat), False)




def readInput(inputFile):
    ## input file location, reads it line by line in and to create an adjacency list, 
    ## list of points with theirnumber of adjecent points, and list of coloured points and their colors. 
    inputColor = False
    adjacencyList = {}
    listOfColorPoints = {}
    listOfPoints=[]
    for line in inputFile:
        if line=="\n":         # set the flag for color input to True ie, ro knowif lines belong to adjeceny matri, or the color 
            inputColor=True
        elif not inputColor:
            line=line.strip()
            temp= line.split(':')
            adjacencyList[temp[0]] = temp[1].split(',')
            listOfPoints.append([str(temp[0]),len(temp[1])])
        else:
            line=line.strip()
            listOfColorPoints[line.split(':')[0]] = line.split(':')[1]     
    return(adjacencyList,listOfColorPoints,listOfPoints)    

def checkInput(adjacencyList):
    ## input: adjececy matrix
    ## output: boolean saying if it is symmetric, diagonal are 0 and square matrix
    matrix=np.zeros((len(adjacencyList),len(adjacencyList)))
    for point in adjacencyList.keys():
        index_i=adjacencyList.keys().index(point)
        for adj_point in adjacencyList[point]:
            index_j=adjacencyList.keys().index(adj_point)
            matrix[index_i,index_j]=1
    if isSymmetric(matrix, matrix.shape[1]) and isDiag(matrix, matrix.shape[1]):        
        return True
    else:
        return False
    
def isDiag(mat, N):
    ##input: matrix and size
    ##checks if all the digonal is 0
    ##output: boolean: 1: if all diagonal is 0; else 0
    for index_i in range(N):
            if (mat[index_i][index_i] != 0):
                return False
    return True

def isSymmetric(mat, N):
    ##input: matrix and size
    ##checks if it is symmetric or not
    ##output: boolean 1: if it is symmetric
    for index_i in range(N):
        for index_j in range(N):
            if (mat[index_i][index_j] != mat[index_j][index_i]):
                return False
    return True

def checkSolution(adjacencyList,listOfColorPoints,listOfPoints):
    ## imputs the adjacency list, lotf of points which are already assigned colors and list of points with count of 
    ## their adjecent points
    ## returns a boolean stating if the solution is possible
    answer=False
    listOfPoints = np.array(listOfPoints,dtype=object)
    listOfPoints = listOfPoints[listOfPoints[:,1].argsort()[::-1]]
    if len(listOfPoints)-len(listOfColorPoints)>=3:
        for index in range(len(listOfPoints)):
            point=listOfPoints[index][0]
            if point not in listOfColorPoints.keys() and not answer:
                #for each point count the number of adjecent points which are colored and which are not          
                countColored=0
                countUncolored=0
                for adjacentPoint in adjacencyList[point]:
                    if adjacentPoint in listOfColorPoints.keys():
                        countColored+=1
                    else:
                        countUncolored+=1
                if countUncolored>=2:
    #                print(point)
                    answer= True
            
            
    return answer                


def main():
    ##input: input file in the form of adjecency list, and list of point whichhas already been assigned color
    ## output : returns boolean if  the solution is possible or not
    inputFilePath=sys.argv[1]
#    print(inputFilePath)
    inputFile=open(inputFilePath)
    
#    inputFile=open("/Users/meghapanda/Documents/Msc_Project/triangulation/test_input.txt")
    (adjacencyList,listOfColorPoints,listOfPoints) = readInput(inputFile)
    
    
## check if the input matrix is correct
    try:
        check = checkInput(adjacencyList)
        if not check:
            raise ValueError('There is a problem with your adjececy matrix')
    except ValueError as error:
        print(error)
        
#    print((adjacencyList,listOfColorPoints,listOfPoints))
    
    answer = checkSolution(adjacencyList,listOfColorPoints,listOfPoints)
    if answer:
        print('Yes a solution exisits')
    else:
        print('No, a solution does not exisits')

    

if __name__ == "__main__":
#    unittest.main()
	main()         
    
