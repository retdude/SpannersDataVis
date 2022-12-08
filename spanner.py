import networkx as nx
import csv
import matplotlib.pyplot as plt #visualization
import numpy as np

def main():
    #Main Function

    isFinished = False
    G = handleCSV()
    H = nx.create_empty_copy(G, with_data=True) #creates edgeless graph copy

    testDisplay(G, isFinished)
    #testDisplay(H, isFinished)

    mst = nx.minimum_spanning_tree(G, weight='weight', algorithm='kruskal', ignore_nan=False)

    testDisplay(mst, isFinished)

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
        d['weight']+= np.random.uniform(0, 10)

    
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
def equationCheck(G, H):
    #this function is responsible for determining if the equation holds true

    #if()

    

    print("incomplete")

    return(True) #use this to set isFinished to True so the test display can change start.png to end.png for the html visualization

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def spanning(G, H):
    #this function handles the for loop that adds edges to the edgless graph using the MST

    """  
    Pseudocode:

    get mst of G (DONE)
    subdivide the edges (??)
    add all the edges of the mst into h(spanner) (SORTA DONE)
    apply the d-light weight initialization sort the neightbor edges for each node accorting to the sorted order, add them to h and sum the edge weights for each node
    keep adding the edges until the total sum is = D
    spanner completion for each vertex try to add all edges in the shortest path if the spanner condition doesn't satisfy 
    """

    mst = nx.minimum_spanning_tree(G) #get mst of G
    sum = mst.size(weight="weight")
    n = mst.number_of_nodes()

    for u,v,d in G.edges(data=True): #scaling
        d['weight'] *= (n/2)*(1/sum)


    for u,v,d in G.edges(data=True): #subdivision w(e) / ceiling(w(e))
        #iterate through all the edges, if > 1: split each edge into mini edges and then fill those gaps with nodes
        #then add those mini edges and nodes to H
        #if <= 1, add anyway

        print()

    #d- light weight
    #add mst to H, then add edges from g' until the sum <= d

    #spanner completion
    #take each pair of vertex, calc the shortest path from u,v in H and u,v in G' check how much larger is H
    #if it is a lot larger and doesn't satisfy the equation, add all the edges into H from G' (for u,v)
    #do until this has been done for all vertex pairs
    #if there is a pair that is not in H but in G', then just add from G' to H


    return(H)



main()