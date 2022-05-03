'''Implementing a Route Planner
In this project you will use A* search to implement a "Google-maps" style route planning algorithm.
# Used Pythagoras to caclculate the straight line between intersections.'''


'''
The map above (run the code cell if you don't see it) shows a disconnected network of 10 intersections. 
The two intersections on the left are connected to each other but they are not connected to the rest of the road network. 
On the graph above, the edge between 2 nodes(intersections) represents a literal straight road not just an abstract connection of 2 cities.

These `Map` objects have two properties you will want to use to implement A\* search: `intersections` and `roads`

**Intersections**

The `intersections` are represented as a dictionary. 

{0: [0.7798606835438107, 0.6922727646627362],
 1: [0.7647837074641568, 0.3252670836724646],
 2: [0.7155217893995438, 0.20026498027300055],
 3: [0.7076566826610747, 0.3278339270610988],
 4: [0.8325506249953353, 0.02310946309985762],
 5: [0.49016747075266875, 0.5464878695400415],
 6: [0.8820353070895344, 0.6791919587749445],
 7: [0.46247219371675075, 0.6258061621642713],
 8: [0.11622158839385677, 0.11236327488812581],
 9: [0.1285377678230034, 0.3285840695698353]}



In this example, there are 10 intersections, each identified by an x,y coordinate.
The coordinates are listed below. You can hover over each dot in the map above to see the intersection number.

'''
'''

**Roads**

The roads property is a list where, if i is an intersection, roads[i] contains 
a list of the intersections that intersection i connects to.

'''





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
        self.dictionary = {}
        self.heap = self.buildHeap(array)
        # the keys are the indexes of the heap, and the values are the nodes
        

    def buildHeap(self,array):
        lastParentIdx = (len(array) - 2) // 2
        for i in range(lastParentIdx, -1,-1):
            self.siftDown(i, array)

        return array

        
    def insert(self, node):
        self.heap.append(node)
        self.siftUp(len(self.heap)-1)
        
    # currentIDx = 0
    def siftUp(self, currentIdx):
        # key is node , value is index
        # THIS LIEN??
        self.dictionary[self.heap[currentIdx]] = currentIdx
        
        # currentIdx = len(self.heap) -1
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and self.heap[currentIdx].fScore < self.heap[parentIdx].fScore:
            self.swap(currentIdx, parentIdx, self.heap)
            # NEW
            self.dictionary[self.heap[currentIdx]] = currentIdx
            self.dictionary[self.heap[parentIdx]] = parentIdx
            # NEW
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2
            
            
    def swap(self, iDxOne, iDxTwo, array):
        array[iDxOne], array[iDxTwo] = array[iDxTwo], array[iDxOne]

    #open_nodes = [30, 14]
    #open_nodes = [14]
    def remove(self):
        # what if there is only one node in the MinHeap?
        if len(self.heap) == 1:
            minFScore_node = self.heap.pop()
        else:
            self.swap(0, len(self.heap) - 1, self.heap)
            minFScore_node = self.heap.pop()
            if len(self.heap) > 1:
                self.siftDown(0,self.heap)
            else:
                # In this situation... where there are only two elements in the array
                #open_nodes = [30, 14]
                #open_nodes = [14, 30]  --> 30 gets popped off
                #open_nodes = [14]
                #No need to sift down with only one element remaining in the array
                # But, we still need to update the dictionary because node 14 is no longer at index 1
                # We need to update it to be at index 0.
                self.dictionary[self.heap[0]] = 0
        return minFScore_node
   
    def siftDown(self, currentIdx,  array):
        # currentIdx = 0
        # NEW 
        self.dictionary[array[currentIdx]] = currentIdx
        childOneIdx = 2 * currentIdx + 1
        # NEW
        self.dictionary[array[childOneIdx]] = childOneIdx
        childTwoIdx = 2 * currentIdx + 2
        # NEW
        if childTwoIdx <= len(array) -1:
            self.dictionary[array[childTwoIdx]] = childTwoIdx
        
        while childOneIdx <= len(array) - 1:
            if childTwoIdx <= len(array) -1:
                if array[currentIdx].fScore < array[childOneIdx].fScore and array[currentIdx].fScore < array[childTwoIdx].fScore:
                    break
                elif array[childOneIdx].fScore < array[childTwoIdx].fScore:
                    self.swap(currentIdx, childOneIdx, array)
                    # NEW
                    self.dictionary[array[currentIdx]] = currentIdx
                    self.dictionary[array[childOneIdx]] = childOneIdx
                    # NEW
                    currentIdx = childOneIdx

                elif array[childOneIdx].fScore > array[childTwoIdx].fScore:
                    self.swap(currentIdx, childTwoIdx, array)
                    # NEW
                    self.dictionary[array[currentIdx]] = currentIdx
                    self.dictionary[array[childTwoIdx]] = childTwoIdx
                    # NEW
                    currentIdx = childTwoIdx
                childOneIdx = 2 * currentIdx + 1
                childTwoIdx = 2 * currentIdx + 2    
            else:
                if array[currentIdx].fScore < array[childOneIdx].fScore:
                    break
                else:
                    self.swap(currentIdx, childOneIdx, array)
                    # NEW
                    self.dictionary[array[currentIdx]] = currentIdx
                    self.dictionary[array[childOneIdx]] = childOneIdx
                    # NEW
                    break
                    
# Algorithm
def shortest_path(M,start,goal):
    # All nodes list -- create nodes:
    # key value pair  -- key is the number, value is the node 
    all_nodes = {}
    for intersection in M.intersections.keys():
        all_nodes[intersection] = Node(intersection)

    # initialize closed list -- this is the nodes that have been visited
    visited_nodes = []
    
    # initialize open list -- all the nodes that we can expand from -- initialize with the start node
    # open_nodes should be a minHeap, because we constantly need to find the frontier w/ the smallest fScore to expand from.
    # at initialization, pass in array of one element -- the start node
    open_nodes = MinHeap([all_nodes[start]])
    
    # initialize current node -- will be start node
    current_node = open_nodes.remove()
        
    # how to get start node coordinates?    
    # calculate h from start to goal
    # g is currently 0 because that is the distance from the start
    # 0 + h = f
    current_node.fScore = calculateHScore(M.intersections[start], M.intersections[goal])
    
    # destination
    destination = all_nodes[goal]
    count = 1
    
    # keep looping/searching while current_node is NOT the goal
    while current_node.number != destination.number:
        count += 1
        
        # HEAP OPEN NODES [14]
        # CURRENT NODE 30 [33, 8, 14, 16]
        for neighbor in M.roads[current_node.number]:
            # us the number to find the node
            neighbor_node = all_nodes[neighbor]
            
            
            if neighbor_node not in visited_nodes:
                # calculate g score for this neighbor node
                gScore = current_node.gScore + calculateHScore(M.intersections[current_node.number], M.intersections[neighbor_node.number])
                # calculate h score from neighbor to destination
                hScore = calculateHScore(M.intersections[neighbor_node.number], M.intersections[destination.number])
                # calculate f score
                fScore = hScore + gScore
                
                if gScore < neighbor_node.gScore or neighbor_node.gScore == 0:
                    # update or give fScore
                    neighbor_node.gScore = gScore
                
                
                # check if this fScore is less than the existing fScore of the neighbor  node
                # OR the fScore of the neighbor_node is 0 (meaning does not exist)
                if fScore < neighbor_node.fScore or neighbor_node.fScore == 0:
                    # update or give fScore
                    neighbor_node.fScore = fScore
                    # since this is the best fScore so far, we will update the camefrom property for the neighbor node
                    neighbor_node.cameFrom = current_node
                    
                # add neighbor node to open nodes -- or update it? 
                if neighbor_node not in open_nodes.heap:
                    # insert the node
                    open_nodes.insert(neighbor_node)
                else:
                    # neighbor node already in open nodes, meaning we have to reorganize the heap
                    # so making the fScore smaller -- may make it smaller than its parent node -- so we call siftUp
                    # pass in index where neighbor is in open nodes
                    # key as the node to unlock the index 
                    index = open_nodes.dictionary[neighbor_node]
                    
                    
                    open_nodes.siftUp(index)
           
        
                
        
        # after going through all the neighbors of the current node (updating/giving fScores as necessary),
        # currentNode can go into visited_nodes
        visited_nodes.append(current_node)

        # the next step, the new current node should be the open node with the lowest f score
        current_node = open_nodes.remove()
        
        
    # path list
    path = []
    
    # the current_node is now the destination 
    # keep finding camefrom until we find arrive at the start (where cameFrom is None)
    while current_node != None:
        path.append(current_node.number)
        current_node = current_node.cameFrom
        
    return path[::-1]
