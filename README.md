# Data Structures & Algorithms

CodeAcademy Course

#Day 1
What is a Node?
- Node contains data and links to other nodes. 
- Link inside of a node is referred to as a pointer. 
- If pointer is null, it means you've reached the end of the path you were following. 

Node Linking:
- Nodes may only be linked to a single other node.
- A node's data may be lost if you inadvertently remove the single link to that node. 


Linked List
- Each node contains data and a pointer to the next node.
- Node with a null pointer is called the tail node.
- Since the nodes use links to denote the next node in the sequence, the nodes are not required to be sequentially located in memory. 
- Common Operations:
  - Adding nodes
  - Removing nodes
  - Finding a ndoe
  - Traversing through a linked list

  - Adding a new node to beginning of list:
    - Link to head node
  
  - Removing a node
    - How to prevent orphaned nodes
    - Must adjust link on previous node so that it points to the following node
    - ![](https://file%2B.vscode-resource.vscode-cdn.net/var/folders/f2/msjnmvg14mgdf6s2h2brfw3c0000gn/T/TemporaryItems/NSIRD_screencaptureui_uUtoYK/Screen%20Shot%202022-09-27%20at%207.06.42%20AM.png?version%3D1664276819486)