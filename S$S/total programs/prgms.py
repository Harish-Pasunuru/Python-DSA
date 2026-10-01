
# PROBLEM 1 - Anagram

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    a = ["" for _ in range(len(s1))]
    b = ["" for _ in range(len(s2))]

    for i in range(len(s1)):
        a[i] = s1[i]

    for i in range(len(s2)):
        b[i] = s2[i]

    a.sort()
    b.sort()

    for i in range(len(a)):
        if a[i] != b[i]:
            return False

    return True


s = "hello"
s2 = "olleh"
print(is_anagram(s, s2))



# PROBLEM 2 - Equilibrium Index


def equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0

    for i in range(len(arr)):
        right_sum = total_sum - left_sum - arr[i]

        if left_sum == right_sum:
            return i

        left_sum += arr[i]

    return -1


numbers = [-7, 1, 5, 2, -4, 3, 0]
print(equilibrium_index(numbers))


# PROBLEM 3 - Range Sum Using Prefix Sum


def build_prefix_sum(numbers):
    prefix = []
    total = 0

    for number in numbers:
        total += number
        prefix.append(total)

    return prefix


def range_sum(prefix, left, right):
    if left == 0:
        return prefix[right]

    return prefix[right] - prefix[left - 1]


numbers = [3, 1, 4, 1, 5, 9, 2, 6]
prefix = build_prefix_sum(numbers)

print(range_sum(prefix, 2, 6))



# PROBLEM 4 - Build Prefix Sum Array

def build_prefix_sum(arr):
    prefix = [0] * len(arr)

    if len(arr) == 0:
        return prefix

    prefix[0] = arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]

    return prefix


numbers = [3, 1, 4, 1, 5, 9, 2, 6]
prefix = build_prefix_sum(numbers)

print(prefix)



# PROBLEM 5 - Maximum of Subarrays


def maxofsubarray(a, k):
    li = []

    for i in range(k, len(a) + 1):
        li.append(maximum(a, i - k, i))

    return li


def maximum(a, st, end):
    max_value = a[st]

    for i in range(st, end):
        if max_value < a[i]:
            max_value = a[i]

    return max_value


a = [1, 3, -1, -3, 5, 3, 6, 7]
print(maxofsubarray(a, 3))



# PROBLEM 6 - Pair Sum


def pairsum(a, el):
    l = 0
    r = len(a) - 1
    ar = []

    for i in range(len(a) // 2):
        if a[l] + a[r] == el:
            ar = ar + [l, r]

        l += 1
        r -= 1

    return ar


n = int(input())
a = list(map(int, input().split()))[:n]
el = int(input())

b = pairsum(a, el)

for i in range(0, len(b), 2):
    print(f"[{b[i]},{b[i + 1]}]")



# PROBLEM 7 - Reverse Array


def reverse(a):
    l = 0
    r = len(a) - 1

    while l < r:
        temp = a[l]
        a[l] = a[r]
        a[r] = temp

        l += 1
        r -= 1

    return a


n = int(input())
a = list(map(int, input().split()))[:n]

print(reverse(a))



# PROBLEM 8 - Pair Sum


def pairsum(a, el):
    l = 0
    r = len(a) - 1
    ar = []

    for i in range(len(a) // 2):
        if a[l] + a[r] == el:
            ar = ar + [l, r]

        l += 1
        r -= 1

    return ar


n = int(input())
a = list(map(int, input().split()))[:n]
el = int(input())

b = pairsum(a, el)

for i in range(0, len(b), 2):
    print(f"[{b[i]},{b[i + 1]}]")



# PROBLEM 9 - Pair Sum - Return First Pair


def pairsum(a, el):
    l = 0
    r = len(a) - 1

    for i in range(len(a) // 2):
        if a[l] + a[r] == el:
            return [l, r]

        l += 1
        r -= 1

    return [-1, -1]


n = int(input())
a = list(map(int, input().split()))[:n]
el = int(input())

print(pairsum(a, el))



# PROBLEM 10 - Linear Search - All Occurrences


def linearsearch(a, el):
    ar = []

    for i in range(len(a)):
        if a[i] == el:
            ar = apnd(ar, i)

    print(ar)


def apnd(a, el):
    ar = [0 for _ in range(len(a) + 1)]

    for i in range(len(a)):
        ar[i] = a[i]

    ar[-1] = el

    return ar


n = int(input())
ar = list(map(int, input().split()))[:n]
el = int(input())

linearsearch(ar, el)



# PROBLEM 11 - Linear Search - First Occurrence


def linearsearch(arr, ele):
    for i in range(len(arr)):
        if arr[i] == ele:
            print(f"element {ele} is found at index {i}")
            return

    print(f"element {ele} is not found")


n = int(input())
arr = list(map(int, input().split()))[:n]
ele = int(input())

linearsearch(arr, ele)



# PROBLEM 12 - Find Minimum Element


def find_minimum(arr):
    if len(arr) == 0:
        return -1

    minimum = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]

    return minimum


n = int(input())
arr = list(map(int, input().split()))[:n]

print(find_minimum(arr))

# PROBLEM 13 - Find Maximum Element


def find_maximum(arr):
    if len(arr) == 0:
        return -1

    maximum = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]

    return maximum


n = int(input())
arr = list(map(int, input().split()))[:n]

print(find_maximum(arr))



# PROBLEM 14 - Count Occurrences of an Element


def count_occurrences(arr, element):
    count = 0

    for i in range(len(arr)):
        if arr[i] == element:
            count += 1

    return count


n = int(input())
arr = list(map(int, input().split()))[:n]
element = int(input())

print(count_occurrences(arr, element))