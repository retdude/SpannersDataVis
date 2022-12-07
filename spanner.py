import networkx as nx
import csv
import matplotlib.pyplot as plt #visualization
import random as rand

def main():
    #Main Function

    isFinished = False
    G = handleCSV()
    H = nx.create_empty_copy(G, with_data=True) #creates edgeless graph copy

    #testDisplay(G, isFinished)
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
        d['weight']+= rand.randint(0,9)

    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def testDisplay(G, isFinished):
    #the following creates a visual for test purposes

    for u,v,d in G.edges(data=True):
        print(u,v,d)

    print()

    print("Graph output:", G)
    print("Size = ", G.size(weight="weight"))

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

    get mst of G
    subdivide the edges
    add all the edges of the mst into h(spanner)
    apply the d-light weight initialization sort the neightbor edges for each node accorting to the sorted order, add them to h and sum the edge weights for each node
    keep adding the edges until the total sum is = D
    spanner completion for each vertex try to add all edges in the shortest path if the spanner condition doesn't satisfy 
    """

    mst = nx.minimum_spanning_tree(G) #get mst of G



    return(H)

main()