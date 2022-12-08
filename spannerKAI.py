import networkx as nx
import csv
import matplotlib.pyplot as plt #visualization
import numpy as np
import math

def main():
    #Main Function

    isFinished = False
    G = handleCSV()
    testDisplay(G, isFinished)
    #Creation of G_Prime which will then be passed into H
    G_prime = scaleGraph(G) 
    H = nx.create_empty_copy(G_prime, with_data=True) #creates edgeless graph copy
    testDisplay(G_prime, isFinished)
    testDisplay(H, isFinished)
    H=spanning(G,H)

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

    """"for u,v,d in G.edges(data=True):
        print(u,v,d)"""

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
    #Iterate through the nodes of the graph
    #The creation of the G_prime is just a copy of G which we will use for parsing in H
    G_prime = G.copy()
    sum = G_prime.size(weight="weight")
    n = G_prime.number_of_nodes()
    for U,V in G_prime.edges():
        tempEdge = G.get_edge_data(U,V, default=None)
        newWeight = (n/2)*(1/sum)
        LastVert = U
        NewEdgeCount = (tempEdge['weight'])/(math.ceil(tempEdge['weight']))
        if tempEdge['weight'] > 1:
            #Stores the end point for the scaling temporarily
            i = 0
            while (i<NewEdgeCount):
                #Rewriting U to be the new V until we hit the very end
                i+=1
                createNewNode(G_prime, U,V, newWeight)
                if i == NewEdgeCount-1:
                    G_prime.addedge(LastVert,V,newWeight)
                
        else:
            createNewNode(G_prime, U,V, newWeight)

    #Returns the scaled graph wtih all of the new nodes in between the old nodes of G
    return G_prime

def createNewNode(G,U,V,d):
    G.add_node(U)
    G.add_edge(V,U)
    #G.add_path([U,V])
    #G.remove_edge(U,V)
    G[U][V]['weight']=float(d)
    print(G[U][V]['weight'])
    #nx.set_edge_attributes(G,(U,V),{"weight":d})


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def dlightweightinit(G,d):
    for V in G.nodes():
        summation =0
        for u in V.edges():
            summation += u['weight']
        if summation < 0:
            while sum < d:
                newWeight = math.rand()
                v.add_edge({"weight":newWeight})
                summation += newWeight

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""TODO: What even is dh in this scenario here?"""
def SpannerCompletion(G, H):
    for Uh,Vh in H:
        for Ug, Vg in G:
            #if
            print()


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



    return(H)



main()