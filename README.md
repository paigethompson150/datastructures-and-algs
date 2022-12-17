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
    ![node removal](/Day1/node-removal.png)


#Udacity
#Day 2
Big O(n) Notation:
n is the amount of time or space it takes for your algorith to run.

Time Efficiency Practice, Manatees
Example1: O(n)
Example2: O(1)
Example3: O(nm)
Example4: O(nn)

Big O Cheat Sheet: https://www.bigocheatsheet.com/


List-Based Collections
