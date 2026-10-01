#problem 1

class queue:
  def __init__(self, cap=8):
    self._a = [None for i in range(cap)]
    self._front = None 
    self._rear = -1
    self._c=0
  def enqueue(self,data):
    if self._c == len(self._a):
      return"overflow"

    if self._c == 0:
      self._a[self._c]=data
      self._front=0
      self._c=1
    else:
      self._a[self._c]=data
      self._c+=1
   
  def peek(self):
    if self._c==0:
      return "no elements "
    return self._a[self._front]
  def peeklast(self):
    return self._a[self._c-1]
  def dequeue(self):
    if self._c==0:
      return "underflow"
      
    ar=[None for i in range(len(self._a))]
    for i in range(1,len(self._a)):
      ar[i - 1] = self._a[i]
    temp = self._a[0]
    self._a=ar
    self._c-=1
    return temp 

q=queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

print(q.dequeue())

print(q.peek())

#problem 2 
class queue:
  def __init__(self, cap=8):
    self._a = [None for i in range(cap)]
    self._front = None 
    self._rear = -1
    self._c=0
  def enqueue(self,data):
    if self._c == 0:
      self._a[self._c]=data
      self._front=0
      self._c=1
    else:
      self._a[self._c]=data
      self._c+=1
   
  def peek(self):
    return self._a[self._front]
  def peeklast(self):
    return self._a[self._c-1]
  def dequeue(self):
    ar=[None for i in range(len(self._a))]
    for i in range(1,len(self._a)):
      ar[i - 1] = self._a[i]
    temp = self._a[0]
    self._a = ar
    self._c-=1
    return temp 

q = queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())
print(q.peek())


#problem 3

class queue:
  def __init__(self, cap=8):
    self._a = [None for i in range(cap)]
    self._front = None 
    self._rear = -1
    self._c=0
  def enqueue(self,data):
    if self._c == 0:
      self._a[self._c]=data
      self._front=0
      self._c=1
    else:
      self._a[self._c]=data
      self._c+=1
   
  def peek(self):
    return self._a[self._front]
  def peeklast(self):
    return self._a[self._c-1]
  def dequeue(self):
    ar=[None for i in range(len(self._a))]
    for i in range(1,len(self._a)):
      ar[i - 1] = self._a[i]
    temp = self._a[0]
    self._a = ar
    self._c-=1
    return temp 

q = queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())


#problem 4

class queue:
  def __init__(self, cap=8):
    self._a = [None for i in range(cap)]
    self._front = None 
    self._rear = -1
    self._c=0
  def enqueue(self,data):
    if self._c == 0:
      self._a[self._c]=data
      self._front=0
      self._c=1
    else:
      self._a[self._c]=data
      self._c+=1

    
    
  def peek(self):
    return self._a[self._front]
  def peeklast(self):
    return self._a[self._rear]
q = queue()
q.enqueue(10)
q.enqueue(20)
print(q.peek())
print(q.peeklast())

