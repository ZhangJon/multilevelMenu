#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Jon Zhang
@contact: zj.fly100@gmail.com
@site:
@version: 1.0
@license:
@file: multilevel_menu.py
@time: 2017-3-8 16:04
Multilevel menu
   Three-Level menu
   select one menu enter its submenu
   enter 'b' go back,enter 'q' exit the system
"""
import sys
def createRegionList(regionFile):
    """
    let the same level region information store in a list
    :param aFile:
    :return regionFileList:
    """
    readRegionFile = open(regionFile)
    regionFileList = [i.split() for i in readRegionFile.readlines()]
    return regionFileList
    readRegionFile.close()

def createLinkOfUpperAndLower(firstFile,secondFile,thiredFile):
    """
    create link of superior and subordinate
    :param firstFile:
    :param secondFile:
    :param thiredFile:
    :return firstDict:
    """
    firstList = createRegionList(firstFile)
    secondList = createRegionList(secondFile)
    thiredList = createRegionList(thiredFile)
    firstDict = {}
    for i in firstList:
        secondDict = {}
        for j in secondList:
            innerList = []
            for k in thiredList:
                if k[1] == j[0]:
                    innerList.append(k[2])
            if j[1] == i[0]:
                secondDict[j[2]] = innerList
        firstDict[i[2]] = secondDict
    return firstDict

def multilevelMenu(provinceDict):
    """
    the show of the multilevel menu
    :param provinceDict:
    :return:
    """
    print("-------------------------------------------------")
    print("+            +")
    print("+            +")
    print("+   Welcome to the China region query system   +")
    print("+            +")
    print("+            +")
    print("-------------------------------------------------")
    while True:
        for i in provinceDict.keys():
            print(i)
        #for i in range(len(provinceDict)):
        #    print("%04d : %s" %(i,list(provinceDict.keys())[i]))
        firstLevelInput = input("Please input one province id to look ( 'q' to exit ):").strip()
        if firstLevelInput == "q":
            sys.exit("Welcome back again!")
        elif firstLevelInput in provinceDict.keys():
            while True:
                for j in provinceDict[firstLevelInput].keys():
                    print(j)
                secondLevelInput = input("Please input one city to look ( 'b' to back or 'q' to exit ):").strip()
                if secondLevelInput == "b":
                        break
                elif secondLevelInput == "q":
                    sys.exit("Welcome back again!")
                elif secondLevelInput in provinceDict[firstLevelInput].keys():
                    while True:
                        for k in provinceDict[firstLevelInput][secondLevelInput]:
                            print(k)
                        innerLevelInput = input("Please input 'b' to back or 'q' to exit:").strip()
                        if innerLevelInput == "b":
                            break
                        elif innerLevelInput == "q":
                            sys.exit("Welcome back again!")

if __name__ == '__main__':
    provinceFile = "province.txt"
    cityFile = "city.txt"
    countyFile = "county.txt"
    #provinceDict = createLineOfThe(provinceFile,cityFile,countyFile)
    multilevelMenu(createLinkOfUpperAndLower(provinceFile,cityFile,countyFile))