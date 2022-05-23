class Node:
   def __init__(self, data):
      self.data = data
      self.children = []
      self.parent = None
   def add_child(self,child):
       child.parent = self
       self.children.append(child)
   def print_tree(self):
       print(self.data)
       for child in self.children:
           child.print_tree()

def build_book_tree():
    root=Node(" DSA Book")

    chapter1=Node("chapter1")
    chapter1.add_child(Node("Hashing"))

    chapter2 = Node("chapter2")
    chapter2.add_child(Node("Trees"))

    chapter3 = Node("chapter3")
    chapter3.add_child(Node("Graphs"))


    root.add_child(chapter1)
    root.add_child(chapter2)
    root.add_child(chapter3)

    return root

if __name__=='__main__':
    root=build_book_tree()
    root.print_tree()
    pass
