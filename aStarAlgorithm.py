


def calculateHScore(frontier, destination):
    distanceForH = sqrt((frontier[0] - destination[0])**2 + (frontier[1] - destination[1])**2)
    return distanceForH


class Node:
   def __init__(self, number):
        self.number = number
        self.gScore = 0
        self.fScore = 0
        self.cameFrom = None

class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self,array):
        lastParentIdx = (len(array) - 2) // 2
        for i in range(lastParentIdx, -1,-1):
            self.siftDown(array)

        
    def insert(self, fScore):
        self.heap.append(fScore)
        self.siftUp()
        
    def siftUp(self):
        currentIdx = len(self.heap) -1
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and self.heap[currentIdx] > self.heap[parentIdx]:
            self.swap(currentIdx, parentIdx, self.heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2
            
            
    def swap(self, iDxOne, iDxTwo, array):
        array[iDxOne], array[iDxTwo] = array[iDxTwo], array[iDxOne]

    
    def remove(self):
        self.swap(0, len(self.heap) - 1)
        minFScore = self.heap.pop()
        self.siftDown()
        return minFScore


    def siftDown(self, array):
        currentIdx = 0
        childOneIdx = 2 * currentIdx + 1
        childTwoIdx = 2 * currentIdx + 2 
        while childOneIdx <= len(array) -1:
            if childTwoIdx <= len(array) -1:
                if array[currentIdx] < array[childOneIdx] and array[currentIdx] < array[childTwoIdx]:
                    break
                elif array[childOneIdx] < array[childTwoIdx]:
                    self.swap(currentIdx, childOneIdx, array)
                    currentIdx = childOneIdx

                elif array[childOneIdx] > array[childTwoIdx]:
                    self.swap(currentIdx, childTwoIdx, array)
                    currentIdx = childTwoIdx
                childOneIdx = 2 * currentIdx + 1
                childTwoIdx = 2 * currentIdx + 2    
            else:
                if array[currentIdx] < array[childOneIdx]:
                    break
                else:
                    self.swap(currentIdx, childOneIdx, array)
                    break