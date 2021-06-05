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

# Return cheapest edge pointing out of component
def cheapestE(unusedE,unusedV,vertex,vertexes_in_component):
    possibleEdges = []
    minimalEdge = []
    for edge in unusedE:
        if ((edge[0] == vertex) and (edge[1] not in vertexes_in_component)):
            possibleEdges.append(edge)
        elif ((edge[1] == vertex) and (edge[0] not in vertexes_in_component)):
            possibleEdges.append(edge)
    #print("Possible edges from ",vertex," are: ",possibleEdges)
    if (possibleEdges != []):
        minimalEdge = copy.deepcopy(possibleEdges[0])
        for edge in possibleEdges:
            if (int(edge[2]) < int(minimalEdge[2])):
                minimalEdge = copy.deepcopy(edge)
    #print("cheapestE returns: ",minimalEdge)
    return minimalEdge

# Print all components
def finalPrint(all_components):
    print("");print("")
    totalCost = 0
    for i in range(len(all_components)):
        print("Component",i)
        print("  Vertexes:  ",(all_components[i][0]))
        print("  Edges:")
        if (all_components[i][1] != []):
            for j in range(len(all_components[i][1])):
                print("     ",all_components[i][1][j])
        print("  Component cost: ",all_components[i][2])
        totalCost += int(all_components[i][2])
        print("");print("")
    if (len(all_components)>1):
        print("Total cost of components: ",totalCost)


def jpAlgorithm():
    V=[]
    E=[]

    input1 = input("Vertexes: ")
    input2 = input("Edges:    ")

    V=input1.split(" ")
    input2=input2.split(",")
    for i in input2:
        E.append(i.split(" "))
    unusedV = copy.deepcopy(V)
    unusedE = copy.deepcopy(E)

    component = [[],[],0] #vertexes, edges, cost
    all_components = []

    if (unusedV == []):
        print("No vertexes entered")
        exit()
    if (unusedE == [['']]):
        print("No edges entered")
        for i in range(len(unusedV)):
            all_components.append([[unusedV[i]],[],0])
        finalPrint(all_components)
        exit()

    while (unusedV != []):
        if (component[0] == []):
            component[0].append(unusedV[0])
            unusedV.remove(unusedV[0])
        cheapest_edge = []
        lowest_cost = 0

        for vertex in component[0]: # Finding cheapest enge pointing out of current component
            cheapest_from_vertex = copy.deepcopy(cheapestE(unusedE,unusedV,vertex,component[0]))
            if (cheapest_edge == []):
                if (cheapest_from_vertex != []):
                    lowest_cost = int(cheapest_from_vertex[2])
                cheapest_edge = copy.deepcopy(cheapest_from_vertex)
            else:
                if (cheapest_from_vertex != []):
                    if (int(cheapest_from_vertex[2]) < int(cheapest_edge[2])):
                        lowest_cost = cheapest_from_vertex[2]
                        cheapest_edge = copy.deepcopy(cheapest_from_vertex)

        if (cheapest_edge == []): # current component cannot be expanded
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


jpAlgorithm()
