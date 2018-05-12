# class implementation of a min Heap in python3
# author Lucas Roberts

class BinaryHeap:
    def __init__(self):
        self.currentSize=0
        self.heapList=[0]

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i//2]:
                tmp=self.heapList[i//2] 
                self.heapList[i//2]=self.heapList[i]
                self.heapList[i]=tmp
            i=i//2 

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize+=1
        self.percUp(self.currentSize)

    def size(self):
        return self.currentSize


