class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        
        for x in range(len(intervals)):
            if intervals[x][1]<newInterval[0]:
                merged.append(intervals[x])
            elif newInterval[1] < intervals[x][0]:
                
                merged.append(newInterval)
                return merged+intervals[x:]
            else:
                newInterval = [min(newInterval[0],intervals[x][0]),max(newInterval[1],intervals[x][1])]
        merged.append(newInterval) 
        return merged   