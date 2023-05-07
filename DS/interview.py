"""
Problem 1
Anagrams. Given 2 strings s1 and s2 . 2 strings are anagrams if they're made of the same
characters with the same frequencies
input - danger output - garden
"""


def are_anagrams_1(s1, s2):
    if len(s1) != len(s2):
        return False
    freq1 = {}  # Frequency of characters for s1 string
    freq2 = {}  # Frequency of characters for s2 string

    for char in s1:
        if char in freq1:
            freq1[char] += 1  # If character present increase the value of the key by 1
        else:
            freq1[char] = 1  # If character absent add the first occurrence value as 1

    for char in s2:
        if char in freq2:
            freq2[char] += 1
        else:
            freq2[char] = 1

    # Now check whether characters exist as the same number after the loop
    for key in freq1:
        if key not in freq2 or freq2[key] != freq1[key]:
            return False
    return True


print('Anagram without using default method -', are_anagrams_1('danger', 'garden'))

from collections import Counter


def are_anagrams_2(s1, s2):
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)


print('Anagram using default method -', are_anagrams_2('danger', 'garden'))


def are_anagrams_3(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


print('Anagram using sorted method -', are_anagrams_3('danger', 'garden'))

print('=' * 100)

"""
Problem 2
First and Last position
Given a sorted array of integers 'arr' and an integer 'target', find the index of the first and last position
of 'target' in 'arr'. If 'target' can't be found in 'arr', return [-1, -1]
input = [2,4,5,5,5,5,5,7,9,9]
target = 5
output = [2,6]
"""


def first_and_last(arr, target):
    for item in arr:  # Iterate through arr
        if arr[item] == target:  # If the index of arr is the target
            start = item  # Create a variable start and assign item to it as it is the first position target is found
            while item + 1 < len(arr) and arr[item + 1] == target:
                item += 1  # Keep on incrementing item until we reach the end of that target
            return [start, item]
    return [-1, -1]


print('First and last position of target', first_and_last([2, 4, 5, 5, 5, 5, 5, 7, 9, 9], 5))

"""
First and Last position using binary search
mid = [(left+right)/2] = [(0+9)/2] = 4 in our case
"""


def find_start(arr, target):
    if arr[0] == target:
        return 0
    left, right = 0, len(arr) - 1  # left and right are the first & last element of arr

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target and arr[mid - 1] < target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # If mid-index of arr is < target than the left should start from right side of mid
        else:
            right = mid - 1  # If arr[mid] > target, so we need to shift left to find the target in arr
    return -1

def find_end(arr, target):
    if arr[-1] == target:
        return len(arr) - 1
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target and arr[mid + 1] > target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def first_and_last_bs(arr, target):
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1, -1]
    start = find_start(arr, target)
    end = find_end(arr, target)
    return [start, end]

print('First and last position of target using binary search', first_and_last_bs([2, 4, 5, 5, 5, 5, 5, 7, 9, 9], 5))

print('=' * 100)

"""
Problem 3
kth largest element
Given an array of integers 'arr' and an integer 'k', find kth largest element
arr = [4,2,9,7,5,6,7,1,3]
k = 4
"""

def kth_largest_1(arr, k):
    for i in range(k-1):
        arr.remove(max(arr))
    return max(arr)
print(kth_largest_1([4,2,9,7,5,6,7,1,3], 4))

def kth_largest_2(arr, k):
    n = len(arr)
    arr.sort()
    print('Sorted arr', arr)
    return arr[n-k]
print(kth_largest_2([4,2,9,7,5,6,7,1,3], 4))

import heapq
def kth_largest_3(arr, k):
    arr = [-elem for elem in arr]
    print('arr', arr)
    heapq.heapify(arr)
    print('heapify arr', arr)
    for i in range(k-1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)
print(kth_largest_3([4,2,9,7,5,6,7,1,3], 4))

print('=' * 100)

