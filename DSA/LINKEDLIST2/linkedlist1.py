# problem 1 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.size += 1
            return

        cn = self.head
        while cn.next is not None:
            cn = cn.next

        cn.next = new_node
        self.size += 1

    def traversal(self):
        if self.head is None:
            print("no elements")
            return

        cn = self.head
        while cn is not None:
            print(cn.data, end="->")
            cn = cn.next

        print("None")

    def search(self, data):
        cn = self.head
        ind = 0

        while cn is not None:
            if cn.data == data:
                print(f"element {data} is at {ind} index")
                return

            cn = cn.next
            ind += 1

        print("element not found")

    def length(self):
        return self.size

    def insBig(self, data):
        obj = Node(data)
        obj.next = self.head
        self.head = obj
        self.size += 1

    def delbig(self):
        if self.head is None:
            return

        self.head = self.head.next
        self.size -= 1

    def dellast(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            self.size -= 1
            return

        cn = self.head
        while cn.next.next is not None:
            cn = cn.next

        cn.next = None
        self.size -= 1

    def insAt(self, data, position):
        if position < 0 or position > self.size:
            print("invalid position")
            return

        obj = Node(data)

        if position == 0:
            obj.next = self.head
            self.head = obj
            self.size += 1
            return

        cn = self.head
        for _ in range(position - 1):
            cn = cn.next

        obj.next = cn.next
        cn.next = obj
        self.size += 1

    def count(self, data):
        count = 0
        cn = self.head

        while cn is not None:
            if cn.data == data:
                count += 1
            cn = cn.next

        return count


ll = linkedlist()
ll.add(10)
ll.add(20)
ll.add(30)

ll.traversal()
ll.search(20)
print(ll.length())

ll.insBig(5)
ll.traversal()

ll.delbig()
ll.traversal()

ll.insAt(50, 2)
ll.traversal()

# problem 2 

class Node:
    def __init__(self,data):
      self.data=data
      self.next=None
class linkedlist:
    def __init__(self):
      self.head=None
      self.size=0
    def add(self,data):
      if self.head==None:
        self.head=Node(data)
        self.size+=1
        return
      cn=self.head
      while cn.next is not None:
        cn=cn.next
      cn.next=Node(data)
      self.size+=1
    def traversal(self):
      if self.head==None:
          print('no elements')
      cn=self.head
      while cn is not None:
          print(cn.data,end="->")
          cn=cn.next
      print(cn)
    def search(self,data):
  
      cn=self.head
      ind=0
      while cn is not None:
          if cn.data == data:
            print(f'element {data} is at {ind} index')
            return
          cn=cn.next
          ind+=1
      print('element not found')
    def length(self):
      return self.size
    def insBig(self,data):
      obj=Node(data)
      obj.next=self.head
      self.head=obj
    def delbig(self):
      if self.head is None:
          return
      self.head=self.head.next
    def dellast(slef):

        cn = self.head
        if cn.next is None:
            cn = None 
        while cn.next.next is not None:
            cn = next=None 
        
  
  
ll=linkedlist()
ll.add(10)
ll.add(20)
ll.add(30)
ll.traversal()
ll.search(20)
print(ll.length())
ll.insBig(5)
ll.traversal() 
ll.delbig()  
ll.traversal()

#problem 3 

class Node:
    def __init__(self,data):
      self.data=data
      self.next=None
class linkedlist:
    def __init__(self):
      self.head=None
      self.size=0
    def add(self,data):
      if self.head==None:
        self.head=Node(data)
        self.size+=1
        return
      cn=self.head
      while cn.next is not None:
        cn=cn.next
      cn.next=Node(data)
      self.size+=1
    def traversal(self):
      if self.head==None:
          print('no elements')
      cn=self.head
      while cn is not None:
          print(cn.data,end="->")
          cn=cn.next
      print(cn)
    def search(self,data):
  
      cn=self.head
      ind=0
      while cn is not None:
          if cn.data == data:
            print(f'element {data} is at {ind} index')
            return
          cn=cn.next
          ind+=1
      print('element not found')
    def length(self):
      return self.size
    def insBig(self,data):
      obj=Node(data)
      obj.next=self.head
      self.head=obj
    def delbig(self):
      if self.head is None:
          return
      self.head=self.head.next
  
  
ll=linkedlist()
ll.add(10)
ll.add(20)
ll.add(30)
ll.traversal()
ll.search(20)
print(ll.length())
ll.insBig(5)
ll.traversal() 
ll.delbig()  
ll.traversal()

