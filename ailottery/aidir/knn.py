# -*- coding: utf-8 -*-
#!/usr/bin/python
from numpy import *
import numpy as np
import operator
import sys
#字符识别导入目录中的数据
from os import listdir



def classify0(inX ,dataSet,labels,k):
    #计算给出的二级数组的个数，此处为6个。
    dataSetSize=dataSet.shape[0]
    #print(dataSetSize)
    #计算测试点列到阵列中各个点的坐标距离，并形成距离矩阵。
    diffMat=tile(inX,(dataSetSize,1))-dataSet
    #print(diffMat)
    #将距离做平方
    sqDiffMat=diffMat**2
    #print(sqDiffMat)
    #将平方加和
    sqDistances=sqDiffMat.sum(axis=1)
    #print(sqDistances)
    #计算平方根，即为欧氏距离。
    distances=sqDistances**0.5
    #print(distances)
    #根据到目标点的欧氏距离对训练集进行排序
    sortDistIndicies=distances.argsort()
    #print(sortDistIndicies)
    classCount={}
    for i in range(k):
        #将点按照投票来排序 450132对应 CCAABB
        voteIlabel=labels[sortDistIndicies[i]]
        #print(voteIlabel)
        #计算字典中key是否存在，存在则加1，后面那个0代表从多少开始计数
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
        #print(classCount[voteIlabel])
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    #print(sortedClassCount)#计算计数之后的结果 [('C', 2), ('A', 1)]
    return sortedClassCount[0][0]

def file2matrix(filename):
    fr=open(filename)
    arrayOLines=fr.readlines()
    numberOfLines=len(arrayOLines)
    returnMat=zeros((numberOfLines,20))
    #print("returnMat %s",returnMat)
    classLabelVector=[]
    index=0
    for line in arrayOLines:
        line=line.strip()
        #切分每一行数据得到一个列表形式的数据
        listFromLine=line.split(',')
        #为二维数组的每一份儿数据赋值，每行三个数据组成数组，文件有多长，这样的数组就有多少个。
        returnMat[index,:]=listFromLine[0:20]
        #将数组中最后一个分类数据存储在列表中，最后一项数据代表分类。根据喜欢程度分成三个层次。
        classLabelVector.append(int(listFromLine[-1]))
        index+=1
    return returnMat,classLabelVector


def autoNorm(dataSet):
    minVals=dataSet.min(0)
    maxVals=dataSet.max(0)
    ranges=maxVals-minVals
    #print("min %f max %f range %f",minVals,maxVals,ranges)
    normDataSet=zeros(shape(dataSet))
    m=dataSet.shape[0]
    normDataSet=dataSet-tile(minVals,(m,1))
    normDataSet=normDataSet/tile(ranges,(m,1))
    return normDataSet,ranges,minVals


def classifyPerson():
    resultList=[1,2]
    #将文件读入到矩阵当中
    datingDataMat,datingLabels=file2matrix('aidir/knnlist.txt')
    #将矩阵归一化
    normMat,ranges,minVals=autoNorm(datingDataMat)
    inArrList=[]

    for i in range(1, len(sys.argv)):
        inArrList.append(int(sys.argv[i]))
    inArr=np.array(inArrList) 
    classifierResult=classify0(((inArr-minVals)/ranges),normMat,datingLabels,7)
    print(resultList[classifierResult-1])


classifyPerson()

