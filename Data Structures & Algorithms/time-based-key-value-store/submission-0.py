class TimeMap:

    def __init__(self):
        self.store = {}
        # perform binary search on a set with tuples appended to it 
        # store mood with time 
        # schema -> key: [[value, timestamp], [value, timestamp]]
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        # perform a binary search and add a fallback to previous
        result = ""
        values = self.store.get(key, [])
        start = 0
        end = len(values) - 1

        while start <= end:
            mid = (start + end) // 2
            
            # increasing order 
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif timestamp > values[mid][1]:
                result = values[mid][0]
                start = mid + 1
            elif timestamp < values[mid][1]:
                end = mid - 1

        return result
            

        
