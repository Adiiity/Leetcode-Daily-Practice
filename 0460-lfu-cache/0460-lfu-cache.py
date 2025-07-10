class LFUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.size=0
        self.min_freq=0
        self.key_to_val_freq={}
        self.freq_to_key=defaultdict(OrderedDict)
        
    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1
        
        val,freq=self.key_to_val_freq[key]
        del self.freq_to_key[freq][key]

        if not self.freq_to_key[freq]:
            del self.freq_to_key[freq]
            if self.min_freq==freq:
                self.min_freq+=1
        
        self.freq_to_key[freq+1][key]=None
        self.key_to_val_freq[key]=(val,freq+1)

        return val

    def put(self, key: int, value: int) -> None:
        if self.cap==0:
            return 
        
        if key in self.key_to_val_freq:
            self.key_to_val_freq[key]=(value,self.key_to_val_freq[key][1])
            self.get(key)
            return
        
        if self.size>=self.cap:
            lfu_key,_=self.freq_to_key[self.min_freq].popitem(last=False)
            del self.key_to_val_freq[lfu_key]
            if not self.freq_to_key[self.min_freq]:
                del self.freq_to_key[self.min_freq]
            self.size-=1

        self.freq_to_key[1][key]=None
        self.key_to_val_freq[key]=(value,1)
        self.min_freq=1
        self.size+=1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)