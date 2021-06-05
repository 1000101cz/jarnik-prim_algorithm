# Stepan Marousek
# Jarnikuv-Primuv algoritmus

# Jako vstup bere 1) seznam vsech vrcholu grafu
#                         a b c d e f
#                 2) seznam vsech hran grafu a jejich ceny
#                         a b 3, a c 5, b c 6, b d 7
import copy

def cheapestE(currentV,unusedE):
    minCost = None
    if (unusedE == []):
        return minCost
    for e in unusedE:
        if (currentV in e):
            cost = e[2]
            if minCost == None:
                minCost = cost
            else:
                if (len(minCost) == 1)
                    if cost < minCost[2]:
                        minCost = e
                else:
                    if cost = minCost[0][2]:
                        minCost.append(e)
                    else if cost < minCost[0][2]:
                        minCost = e
    return minCost

def removePossibleCircles(V,unusedV,unusedE):
    usedV = V - unusedV
    for e in unusedE:
        if (e[0] in usedV) and (e[1] in usedV):
            unusedE.remove(e)
    return unusedE

def jpAlgorithm():
    V=[]
    E=[]

    input1 = input()
    input2 = input()

    V=input1.split(" ")
    input2=input2.split(",")
    for i in input2:
        E.append(i.split(" "))
    unusedV = copy.deepcopy(V)
    unusedE = copy.deepcopy(E)

    finalE = []
    currentComponent = []
    while(1):
        if (len(unusedV)>1):
            if (currentComponent == []):
                currentV = unusedV[0]
                currentComponent.append(currentV)



        else:
            break
    print("Tohle bude vysledna cesta:  ",finalE)

jpAlgorithm()
