# Dev Set-up

In order to use and work on the spanner.py file, there are a few package dependencies that must be installed to your pyenv


1. First select the pyenv you want to use
    - To check your pyenv type `pyenv versions`, the version with the `*` is your current pyenv

2. Then pip install the following packages:
    - networkx
    - numpy
    - scipy
    - matplotlib

For example, type in your console `pip install networkx`
You will be able to check the status of these packages by typing `pip list` which will display the packages installed on your pyenv

# PSEUDO CODE FOR THE PROJECT AND MAJOR STAGES:

1. Spawn and create your initial graph G
2. Scale the graph by iterating through the edges and dividing those edges into proportional distance edges that overall still connect vertices U and V. This is G'
3. Apply the MST algorithm from NetworkX on G'
4. Perform the d-lightweight initialization 
5. Do the spanner completion for our project (already somewhat implemented) to produce H which is the final product we will be displaying. 
6. Visualization

**__Pseudocode for the project:__**

//Stage one of our project
Create and initialize our graph G

__Stage two: scaling__
for every edge within the graph G
    edge(i) = U (Vertice U, Vertice V)
    if w(U,V) > 1 //If the weight of the edge that we are iterating through is greater than 1
        NewEdgeCount = ((w(e))/(CEILING(w(e))) //This determines how many edges we will need to "fill in" the edge between it
        for (i = 0; i<NewEdgeCount; i++)
            Create a new vertice which links previous edge to the new edge to create G' 

__Stage three: Creating the MST__
Apply nx.minimum_spanning_tree to G' to create the MST

__Stage four: d-lightweight initialization__
for every vertice:
    summation =0;
    //Preliminary check for the weight of the vertice
    for every edge:
        summation += w(edge)
    if summation <d:
        while sum < d:
            keep adding edges to vertice
            summation += w(newEdgE)

__Stage five: Spanner Completion:__
For (U,V) in H:
    for (U, V) in G:
        if dh(U,V) <= dG'(U,V) + 2 * w(U,V)
            compute the shortest path for (U,V) in H and G'
            //NOTE: Then make this THE path to use within the final product H
        add edges from G' into H

__Stage six: Visualization__
Ret, you got this homie
        
    
