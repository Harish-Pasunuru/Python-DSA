def selectionsort(a):
  for i in range(len(a)):
    min = i 
    for j in range(i+1,len(a)):
      if a[j] < a [min]:
        min = j 
    a[i],a[min] = a[min],a[i]
  return a 
def bubblesort(a):
  for i  in range(len(a)):
    for j in range(i+1,len(a)):
      if a[i]>a[j]:
        a[i],a[j] = a[j],a[i]
  return a 
a = [23,12,22,45,7,8]
print(selectionsort(a))
a = [23,1245,6,7,8]
print(bubblesort(a))





#problem 2 
def linearsearch(ar, target):
  for i in range(len(ar)):
    if ar[i] == target:
      print(f'(target) is found at index{i}')
      return 
  print('found')
  return -1
a = [23,12,33,46,7,8]
print(linearsearch(a,10))

#problem 3



def binarysearch(a, target = 17):
  l = 0
  r = len(a) - 1
  m = (l+r)//2
  while l < r:
    if a [m] == target:
      print(f'(target) is found at index{m}')
      return
    elif a[m]<target:
      l = m 
      m = (l+r)//2
    else:
      r = m 
      m = (l+r)//2
      



b = [10,11,15,17,18,21]
binarysearch(b,17)
      
#problem 4




