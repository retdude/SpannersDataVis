import networkx as nx
import csv
import matplotlib.pyplot as plt #visualization

def main():
    #Main Function

    G = handleCSV()
    edgelessG = nx.create_empty_copy(G, with_data=True) #creates edgeless graph copy

    testDisplay(G)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def handleCSV():
    #This function is responsible for importing the csv and converting it to a graph

    data  = open('test.csv', "r", encoding='utf8')
    #read = csv.reader(Data) (idk if i need this)
    G = nx.read_edgelist(data, comments='#', delimiter=',', nodetype=str, data=[str, str], edgetype=None)
    for e in G.edges():
        print(e)

    return G

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def testDisplay(G):
    #the following creates a visual for test purposes

    print(G)

    pos = nx.spring_layout(G,scale=1)
    nx.draw(G, pos, with_labels=True)
    plt.savefig('this.png')
    plt.show() 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def edgeWeightCalculation():
    #this function is responsible for determining edge weight and deciding if to add/remove it

    print("incomplete")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def edgeAddition(G, edgelessG):
    #this function handles the for loop that adds edges to the edgless graph using the MST

    print("incomplete")




main()