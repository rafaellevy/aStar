


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
            self.siftDown(i, array)

        return array

        
    def insert(self, fScore):
        self.heap.append(fScore)
        self.siftUp(len(self.heap)-1)
        
    def siftUp(self, currentIdx):
        # currentIdx = len(self.heap) -1
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and self.heap[currentIdx] < self.heap[parentIdx]:
            self.swap(currentIdx, parentIdx, self.heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2
            
            
    def swap(self, iDxOne, iDxTwo, array):
        array[iDxOne], array[iDxTwo] = array[iDxTwo], array[iDxOne]

    
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        minFScore = self.heap.pop()
        self.siftDown(0,self.heap)
        return minFScore

    # def siftDown(self, currentIdx, endIdx, heap):
    #     childOneIdx = currentIdx * 2 + 1
    #     while childOneIdx <= endIdx:
    #         childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
    #         if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
    #             idxToSwap = childTwoIdx
    #         else:
    #             idxToSwap = childOneIdx
    #         if heap[idxToSwap] < heap[currentIdx]:
    #             self.swap(currentIdx, idxToSwap, heap)
    #             currentIdx = idxToSwap
    #             childOneIdx = currentIdx * 2 + 1
    #         else:
    #             return    
    def siftDown(self, currentIdx,  array):
        # currentIdx = 0
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


myArray = [48,12,24,7,8,-5,24,391,24,56,2,6,8,41]

myHeap = MinHeap(myArray)



myHeap.insert(76)
print(myHeap.heap)

myHeap.remove()
myHeap.remove()
print(myHeap.heap)
myHeap.insert(87)
print(myHeap.heap)




