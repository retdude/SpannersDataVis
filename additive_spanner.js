const numVertices = 30;
const p = .7;

let nodes = []; //global list of nodes in the dataset

class node{
    constructor(){ //constructor for an item in class node
        this.id = 0; //essentially name (or index in nodes list)
        this.x = Math.random() * 600; //plots to svg coordinates
        this.y = Math.random() * 480;
        this.edges = []; //other nodes to which this node connects
    }
    //fill with attributes
    
}

for (var i = 0; i<numVertices; i++){
    let currNode = new node;
    currNode.id = i;
    nodes.push(currNode);
}
//console.log(nodes);




function generateGraph(numVertices, p){ //creates the dataset
    var numEdges = 0;

    for (var i = 0; i < numVertices - 1; i++){

        for (var j = i + 1; j < numVertices; j++){

            var rand = Math.random();
           
            if (rand <= p ){

                nodes[i].edges.push(j);
                nodes[j].edges.push(i);
                numEdges += 1;
                var randX = Math.random() * 600;
                var randY = Math.random() * 480;
                

            }
        }
    }
}

function noCycles(unvisitedNodes){ //first time pass in an int array w/ values 0-29
    currNode = unvisitedNodes.shift();

//TODO -- Basically run a simple dfs on the dataset and make sure that we do not encounter the same edge twice
//if we do get the same edge twice we will have to delete it later but I was making this as a T/F func

//recursive DFS passing through an array of id's (just a number)


    
}

function additiveSpannerFormula(unknown){
    
    //TODO
    //Generate the formula to dictate which edges are to be removed (unclear what to do but read the paper)

    // paper link: https://arxiv.org/pdf/2103.09731.pdf

}




function calculateWeight(node1, node2){ //distance formula
    var xinstance = node2.x - node1.x;
    var yinstance = node2.y - node1.y;

    var result = Math.sqrt((xinstance*xinstance)+(yinstance*yinstance));
    return result;
}

function removeEdgefromGraph(nodeID, edgeID){ //removes an edge (to be used for actual spanning)
    var index1 = nodes[nodeID].edges.indexOf(edgeID);
    var index2 = nodes[edgeID].edges.indexOf(nodeID);

    nodes[nodeID].edges.splice(index1, 1);
    nodes[edgeID].edges.splice(index2, 1);
    
    
}

generateGraph(numVertices, p); 
//console.log(nodes);
console.log(nodes[0]);
console.log(nodes[1]);

console.log(calculateWeight(nodes[0], nodes[1]));

/* removeEdgefromGraph(0, 1);
console.log(nodes[0]);
console.log(nodes[1]);
 */





















/*(async () => {
    const {execute} = deployments
    const { deployer } = await getNamedAccounts()
    await execute('ExordiumOne', {from: deployer}, 'toggleActive')
  })();
  

const fs = require("fs");
const { parse } = require("csv-parse");
//let edges = [];

const node= {
    //fill with attributes
    number: 0,
    x: 0,
    y: 0,
    edges: {},

    applyAttributes: function(){
        this.x = Math.random() * 580; //these values so that thhe coodinates
        this.y = Math.random() * 420;//fit inside the SVG normally
        this.edges = [];

        return;
    
    }

    
}

async function fillNodeData() {

    let edges = [];

    let promise = new Promise((resolve, reject) => {
        fs.createReadStream("graph_n30_p.7.csv")
            .pipe(parse({ delimiter: ",", from_line: 2 }))
            .on("data", function (row) {
                //console.log(row);
                edges.push(row);
                //alert(window.edges.push(row));
            })
            .on("error", function (error) {
                reject("ERROR");
            })
            .on("end", function () {
                resolve("Sucsess");
            });
    }); 

    edges = await(promise); //await(edges);

    let nodes = []; //await(node data);
    

    console.log(edges);
    
    
    return Promise.resolve(1); //Change eventually
    



}
  
fillNodeData().then(console.log(edges)); // also to change








//console.log(edges);
//console.log(nodes);
*/
