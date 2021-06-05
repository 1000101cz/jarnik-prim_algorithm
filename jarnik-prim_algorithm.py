#!/usr/bin/env python3

#********************************************
#********************************************
#***                                      ***
#***    NAME:    Jarnik-Prim algorithm    ***
#***    VERSION: 0.0.1                    ***
#***    AUTHOR:  MAROUSEK S.              ***
#***    DATE:    2021/6/5                 ***
#***                                      ***
#********************************************
#********************************************

# Program input   1) list of all vertexes
#                         a b c d e f
#                 2) list of possible edges
#                         a b 3,a c 5,b c 6,b d 7


import copy
import sys
import os

# Return cheapest edge pointing out of component
def cheapestE(unusedE,unusedV,vertex,vertexes_in_component):
    possibleEdges = []
    minimalEdge = []

    for edge in unusedE:

        if (((edge[0] == vertex) and (edge[1] not in vertexes_in_component))
            or ((edge[1] == vertex) and (edge[0] not in vertexes_in_component))):
            possibleEdges.append(edge)

    if (possibleEdges != []):
        minimalEdge = copy.deepcopy(possibleEdges[0])

        for edge in possibleEdges:

            if (int(edge[2]) < int(minimalEdge[2])):
                minimalEdge = copy.deepcopy(edge)
    return minimalEdge


# Print all components
def finalPrint(all_components):
    print("");print("")
    totalCost = 0

    for i in range(len(all_components)):
        if (len(all_components)>1):
            print("Component",i+1)
        print("  Vertexes:  ",", ".join(all_components[i][0]))
        print("  Edges:")

        if (all_components[i][1] != []):
            for j in range(len(all_components[i][1])):
                print("     %c - %c  |  %d"%(all_components[i][1][j][0],
                    all_components[i][1][j][1],int(all_components[i][1][j][2])))

        print("  Component cost: ",all_components[i][2])
        totalCost += int(all_components[i][2])
        print("");print("")

    if (len(all_components)>1):
        print("Total cost of %d components: "%(len(all_components)),totalCost)


# Jarnik-Prim algorithm
def jpAlgorithm():
    # process input
    V=[]
    E=[]
    if (len(sys.argv) > 1): # read input from file
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print("File ",filename," does not exist")
            exit()
        print("File: ",filename)
        file = open(filename)
        inputf = file.readline()

        while ("Vertexes:" not in inputf):
            inputf = file.readline()
        input1 = file.readline()

        while ("Edges:" not in inputf):
            inputf = file.readline()
        input2 = file.readline()

    else: # read input from std in
        input1 = input("Vertexes: ")
        input2 = input("Edges:    ")
    V=input1.split(" ")
    input2=input2.split(",")
    for i in input2:
        E.append(i.split(" "))
    unusedV = copy.deepcopy(V)
    unusedE = copy.deepcopy(E)

    # inits
    component = [[],[],0] #vertexes, edges, cost
    all_components = []

    # special cases
    if (unusedV == []):
        print("No vertexes entered")
        exit()
    if (unusedE == [['']]):
        print("No edges entered")
        for i in range(len(unusedV)):
            all_components.append([[unusedV[i]],[],0])
        finalPrint(all_components)
        exit()

    # find minimal spanning tree
    while (unusedV != []):

        if (component[0] == []): # component is empty -> add unused vertex
            component[0].append(unusedV[0])
            unusedV.remove(unusedV[0])
        cheapest_edge = []
        lowest_cost = 0

        for vertex in component[0]: # finding cheapest edge pointing out of current component
            cheapest_from_vertex = cheapestE(unusedE,unusedV,vertex,component[0])

            if (cheapest_edge == []): # no edge points out of this vertex
                if (cheapest_from_vertex != []):
                    lowest_cost = int(cheapest_from_vertex[2])
                cheapest_edge = cheapest_from_vertex
            else:
                if (cheapest_from_vertex != []):
                    if (int(cheapest_from_vertex[2]) < int(cheapest_edge[2])):
                        lowest_cost = cheapest_from_vertex[2]
                        cheapest_edge = cheapest_from_vertex

        if (cheapest_edge == []): # current component cannot be expanded -> done
            all_components.append(component)
            component = [[],[],0]

        else:  # component is expanding -> remove edge from unusedE and vertex from unusedV
            component[2] = component[2] + int(lowest_cost)
            component[1].append(cheapest_edge)

            if (cheapest_edge[0] in unusedV):
                unusedV.remove(cheapest_edge[0])
            elif (cheapest_edge[1] in unusedV):
                unusedV.remove(cheapest_edge[1])
            else:
                print("Sthg fucked up 1")

            if (cheapest_edge[0] not in component[0]):
                component[0].append(cheapest_edge[0])
            elif (cheapest_edge[1] not in component[0]):
                component[0].append(cheapest_edge[1])
            else:
                print("Sthg fucked up 2")
            unusedE.remove(cheapest_edge)

            if (unusedV == []):
                all_components.append(component)

    finalPrint(all_components)
#end


jpAlgorithm()
