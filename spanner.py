import networkx as nx
import csv
import matplotlib.pyplot as plt #visualization
import numpy as np
import math

def main():
    #Main Function

    isFinished = False
    G = handleCSV()
    H = nx.create_empty_copy(G, with_data=True) #creates edgeless graph copy

    testDisplay(G, isFinished) #gets starting graph image

    GScaled = scaleGraph(G)  
    mst = nx.minimum_spanning_tree(G, weight='weight', algorithm='kruskal', ignore_nan=False)
    Gprime = scaleGraph(mst) #takes the mst G and makes G'

    subdivideGraph(Gprime, H)
    dLightWeight(GScaled, Gprime, H)
    spannerCompletion(H, Gprime)

    isFinished = True

    testDisplay(H, isFinished)
    
    print("Spanning Complete")
   

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def handleCSV():
    #This function is responsible for importing the csv and converting it to a graph

    data  = open('testBig.csv', "r", encoding='utf8')
    #read = csv.reader(Data) (idk if i need this)
    G = nx.read_edgelist(data, comments='#', delimiter=',', nodetype=str, data=[str, str], edgetype=None)

    setEdgeWeight(G)

    return(G)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def setEdgeWeight(G):
    #this function sets the edge weight of each edge in G

    nx.set_edge_attributes(G, values = 1, name = 'weight')

    for u,v,d in G.edges(data=True):
        d['weight']+= np.random.uniform(0, 100)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def nodeCreation(G):
    #creates new node to be added

    checkList = list(G.nodes())

    largest = 0;
    for node in checkList:
        if int(node) > largest:
            largest = int(node)
    
    return(int(largest) + 1)
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def testDisplay(G, isFinished):
    #the following creates a visual for test purposes

    for u,v,d in G.edges(data=True):
        print(u,v,d)

    print("~~~~~~~~~~~~~~~~~")

    print("Graph Output:", G)
    print("Sum of Edge Weight = ", G.size(weight="weight"))

    print("~~~~~~~~~~~~~~~~~")
    print()

    pos = nx.spring_layout(G,scale=1)
    nx.draw(G, pos, with_labels=True)

    if(not isFinished):
        plt.savefig('start.png')

    else:
        plt.savefig('end.png')
    
    plt.show() #remove in final

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def scaleGraph(G):
    #Iterate through the nodes of the graph and scale each edge weight to (n/2)*(1/sum)

    sum = G.size(weight="weight")
    n = G.number_of_nodes()

    for u,v,d in G.edges(data=True): #scaling
        d['weight'] *= ((n/2) * (1/sum))

    return(G)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def subdivideGraph(Gprime, H):
    #iterate through all the edges 
    # if > 1: split each edge into mini edges and then fill those gaps with nodes
    #then add those mini edges and nodes to H
    #if <= 1, add anyway

    for u,v,d in Gprime.edges(data=True): #subdivision w(e) / ceiling(w(e))
        if(d['weight'] > 1):
            newEdgeCount = round((d['weight']) / (math.ceil(d['weight'])))
            newEdgeWeight = (d['weight']) / (newEdgeCount)
            lastNode = u

            for i in range(newEdgeCount):
                tempNode = nodeCreation(H)
                H.add_node(tempNode)
                H.add_edge(lastNode, tempNode, weight=newEdgeWeight)
                lastNode = tempNode
                print("adding")

            H.add_edge(lastNode, v, weight = newEdgeWeight) #completes the chain

        else:
            H.add_edge(u,v, weight = d['weight'])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def dLightWeight(GScaled, Gprime, H):
    #add mst to H, then add edges from g' until the sum <= d
    #d = n^(2/3)

    sum = 0
    n = Gprime.number_of_nodes()
    dWeight = n ** (2/3)
    print(dWeight)

    if(dWeight > 0):
        for u,v,d in GScaled.edges(data=True):
            if((sum + d['weight']) > dWeight):
                print("break")
                break
            elif(not H.has_edge(u,v)):
                H.add_edge(u,v, weight = d['weight'])
                sum += d['weight']
                print("added")
            
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def spannerCompletion(H, Gprime):
    #take each pair of vertex, calc the shortest path from u,v in H and u,v in G' check how much larger is H
    #if it is a lot larger and doesn't satisfy the equation, add all the edges into H from G' (for u,v)
    #do until this has been done for all vertex pairs
    #if there is a pair that is not in H but in G', then just add from G' to H

    for u,v,d in Gprime.edges(data=True):
        if((not H.has_edge(u,v))):
            H.add_edge(u,v, weight = d['weight'])
        elif(H[u][v]["weight"] > Gprime[u][v]["weight"]):
            H.remove_edge(u,v)
            H.add_edge(u,v, weight = d['weight'])
            print("replace")


main()