# This is the file where you must implement the Second Chance algorithm

# This file will be imported from the main code. The PhysicalMemory class
# will be instantiated with the algorithm received from the input. You may edit
# this file as you wish

# NOTE: there may be methods you don't need to modify, you must decide what
# you need...

class SecondChance:

  def __init__(self):
    self.allocatedFrames = []

  def put(self, frameId):
    self.allocatedFrames.append(frame)

  def evict(self):
    indexOldFrame = 0
    if self.allocatedFrames[indexOldFrame].is_referenced():
      self.allocatedFrames[indexOldFrame].set_referenced(False)
      self.allocatedFrames.append(self.allocatedFrames.pop(indexOldFrame))
      return self.evict()
      
    else:
      frameRemoved = self.allocatedFrames.pop(indexOldFrame) 
      return frameRemoved.get_id()

    return self.allocatedFrames.pop(indexOldFrame).get_id()
    

  def clock(self):
    pass

  def access(self, frameId, isWrite):
    for frame in self.allocatedFrames:
      if frame.get_id() == frameId: 
        frame.set_referenced(True)
        frame.set_modified(isWrite)
        break
            
