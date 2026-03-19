class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        i = 0
        units = 0
        while truckSize and i < len(boxTypes):
            multiplier = min( truckSize, boxTypes[i][0])
            truckSize = truckSize - multiplier
            units = units + (boxTypes[i][1]*multiplier)
            i += 1
        return units

#heap
import heapq
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        heap = []
        for boxes, units in boxTypes:
            heapq.heappush(heap, [-units, -boxes])
        totalUnits = 0
        while heap and truckSize != 0:
            units, boxes = heapq.heappop(heap)
            units, boxes = - units, - boxes
            if boxes < truckSize:
                totalUnits += units * boxes
                truckSize -= boxes
            elif boxes >= truckSize:
                totalUnits += units * truckSize
                truckSize = 0
        return totalUnits