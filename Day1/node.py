#Initializing node
class Node:
  def __init__(self, value, link_node = None):
    self.value = value
    self.link_node = link_node
  
  #Get value of pointer
  def get_link_node(self):
    return self.link_node
  
  #Change value of pointer
  def set_link_node(self, link_node):
    self.linK_node = link_node

    #Get value of node
  def get_value(self):
    return self.value

node3 = Node("third node")
node2 = Node("second node", node3)
node1 = Node("first node", node2)

#Getting value of a node's pointer
print(node1.get_link_node().get_value())
print(node2.get_link_node().get_value())


