import node
from node import Node 

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  #Get first node
  def get_head_node(self):
    return self.head_node

  #Insert node at beginning of list
  def insert_beginning(self, new_node):
    new_node = Node(new_node)
    new_node.set_link_node(self.head_node)
    self.head_node = new_node
  
  #Print out string representation of a list
  def stringify_list(self):
    string = ""
    current_node = self.head_node
    while current_node:
      string += str(current_node.get_value()) + '\n'
      current_node = current_node.link_node
    return string

ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())
    