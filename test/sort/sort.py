#coding=utf-8

import time
import random

class Sort(object):
    def sort(self, arr):
        pass
    def show(self, arr):
        print arr
    def isSorted(self, arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return False
        return True

class Bubble(Sort):
    '''冒泡排序O(n2)
    '''
    def sort(self, arr):
        for i in range(len(arr) - 1, 0, -1):
            for j in range(0, i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]    
    
class Select(Sort):
    '''选择排序 O(n2)
    '''
    def sort(self, arr):
        for i in range(len(arr)):
            minIndex = i
            for j in range(i, len(arr)):
                minIndex = minIndex if arr[minIndex] < arr[j] else j
            arr[i], arr[minIndex] = arr[minIndex], arr[i]

class Insert(Sort):
    '''插入排序 O(n2)
    '''
    def sort(self, arr):
        for i in range(1, len(arr)):
            while i >= 1 and arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                i -= 1

class Shell(Sort):
    '''希尔排序 
    '''
    def sort(self, arr):
        step = 1
        l = len(arr)
        while step < l / 3:
            step = step * 3 + 1
        while step >= 1:
            for i in range(step, len(arr)):
                while i >= step and arr[i] < arr[i - step]:
                    arr[i], arr[i - step] = arr[i - step], arr[i]
                    i -= step
            step = step / 3


class Merge(Sort):
    '''合并排序 O(nlgn)
    '''
    def sort(self, arr):
        self.mergeSort(arr, 0, len(arr) - 1)
    
    def mergeSort(self, arr, i, j):
        if i >= j:
            return
        mid = (i + j) / 2
        self.mergeSort(arr, i, mid)
        self.mergeSort(arr, mid + 1, j)
        self.merge(arr, i, mid, j)
    
    def merge(self, arr, lo, mid, hi):
        helper = []
        i, j = lo, mid + 1
        while i <= mid and j <= hi:
            if arr[i] <= arr[j]:
                helper.append(arr[i])
                i += 1
            else:
                helper.append(arr[j])
                j += 1
        if i == mid + 1:
            while j <= hi:
                helper.append(arr[j])
                j += 1
        if j == hi + 1:
            while i <= mid:
                helper.append(arr[i])
                i += 1
        for i in range(lo, hi + 1):
            arr[i] = helper[i - lo]


class Quick(Sort):
    def sort(self, arr):
        self.quicksort(arr, 0, len(arr) - 1)
        
    def quicksort(self, arr, i, j):
        if i >= j:
            return
        base = self.getBaseIndex(arr, i, j)
        self.quicksort(arr, i, base - 1);
        self.quicksort(arr, base + 1, j);
        
    def getBaseIndex(self, arr, i, j):
        base = arr[i]
        flag = True
        while i < j:
            if flag:
                while j > i and base <= arr[j]:
                    j -= 1
                if j == i:
                    break
                else:
                    arr[i] = arr[j]
                    flag = False
            else:
                while i < j and base >= arr[i]:
                    i += 1
                if j == i:
                    break
                else:
                    arr[j] = arr[i]
                    flag = True
        arr[i] = base
        return i

class SortTest(object):
    def time(self, alg, arr):
        start = time.time()
        if alg == 'Select':
            Select().sort(arr)
        elif alg == 'Insert':
            Insert().sort(arr)
        elif alg == 'Shell':
            Shell().sort(arr)
        elif alg == 'Merge':
            Merge().sort(arr)
        elif alg == 'Quick':
            Quick().sort(arr)
        return (time.time() - start) / 1000
    def test(self, alg, times, arrNum):
        total = 0
        for i in range(times):
            arr = []
            for j in range(arrNum):
                arr.append(random.random() * arrNum)
            total += self.time(alg, arr) 
        print alg, "'s time is", total, 'second.'



if __name__ == '__main__':
    test = SortTest()
    #test.test('Insert', 1000, 10000)
    test.test('Merge', 1000, 10000)
    test.test('Quick', 1000, 10000)
