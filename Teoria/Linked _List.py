
#  Indexing O(n)------  Insert or delet at start O(1) ---- intert or delet at end O(n) ---- Insert element in middel O(n) ----

# creation: 

from ast import Return


class Node(object):
    def __init__(self,data,next=None):
        self.data = data
        self.next_node = next
    def get_next (self):
        return self.next_node
    def set_next (self,n):
        self.next_node = n
    def get_data (self):
        return self.data
    def set_data (self,data):
        self.data = data
class linked_list(object):
    def __init__(self,r=None):
        self.root=r
        self.size=0
    def get_size (self):
        return self.size
    def add (self,data):
        new_node = Node(data,self.root)
        self.root=new_node
        self.size +=1 
    def remove (self,data):
        this_node = self.root
        prev_node= None
        while this_node:
            if this_node.get_data()==data:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -=1
                return True #data remove
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False #data dont found
    def find (self,data):
        this_node = self.root
        while this_node:
            if this_node.get_data()==data:
                return data
            else:
                this_node = this_node.get_next()
        return None
    
    def print (self):
        if self.root is None:
            print("Linked List is empty")
            return
        itr = self.root
        llstr=''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.get_next()
        print(llstr)

myList=linked_list()
myList.add(5)
myList.add(50)
myList.add(46)
myList.add(38)
myList.add(68)
myList.remove(38)
print(myList.remove(50))
print(myList.find(5))
print(myList.print())