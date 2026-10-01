# problem 1 

def longest_unique_substring(s):
  char_index ={}
  max_length=0
  start=0

  for end in range(len(s)):
    if s[end] in char_index and char_index[s[end]] >= start:
      start = char_index[s[end]]+1

    char_index[s[end]]=end
    max_length = max(max_length , end - start + 1 )

  return max_length 

print(longest_unique_substring("bbbbb"))

# problem 2 

a = [2, 3, 4, 5, 6, 7, 8, 9]
k = 3

def maxavgsubarray(a, k):
    sum = 0
    for i in range(k):
        sum += a[i]

    maxavg = sum/k

    for i in range(k, len(a)):
        sum = sum + a[i] - a[i - k]
        avg = sum/k
        if avg>maxavg:
            maxavg = avg

    print(maxavg)

maxavgsubarray(a, k)

#problem 3

a = [2, 3, 4, 5, 6, 7, 8, 9]
k = 3

def minavgsubarray(a, k):
    sum = 0
    for i in range(k):
        sum += a[i]

    minavg = sum/k

    for i in range(k, len(a)):
        sum = sum + a[i] - a[i - k]
        avg = sum/k
        if avg<minavg:
            minavg = avg

    print(minavg)

minavgsubarray(a, k)
