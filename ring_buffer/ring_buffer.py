class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.count = 0

    def append(self, item):
        if len(self.buffer) < self.capacity: # if the buffer is not yet full it just appends it to the list
            self.buffer.append((item, self.count)) # the tuple with self.count keeps track of the order the elements were added
        else:
            for i in range(self.capacity):
                if self.buffer[i][1] == (self.count - self.capacity): # replacing the oldest entry  
                    self.buffer[i] = (item, self.count) 
        self.count += 1

    def get(self):
        return [each[0] for each in self.buffer] # gets rid of the internal count and only returns the item

