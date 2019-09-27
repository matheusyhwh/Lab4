# This is the file where you must implement the Aging algorithm

# This file will be imported from the main code. The PhysicalMemory class
# will be instantiated with the algorithm received from the input. You may edit
# this file as you whish

# NOTE: there may be methods you don't need to modify, you must decide what
# you need...

ALGORITHM_AGING_NBITS = 8
"""How many bits to use for the Aging algorithm"""

class Aging:
  NBITS = 8
  VALUE_SUM = 2**(NBITS - 1)
  SHIFT = 1

  def __init__(self):
    self.allocatedFrames = []


  def put(self, frameId):
    self.allocatedFrames.append(frame)

  def evict(self):
    indexOldestFrame = 0
    
    self.allocatedFrames.sort(key=lambda frame: frame.access_counter)
    removedFrame = self.allocatedFrames.pop(indexOldestFrame)
    
    return removedFrame.get_id()



  def clock(self):
    for frame in self.allocatedFrames:
        frame.set_referenced(False)
        frame.set_access_counter(frame.get_access_counter() >> self.SHIFT)
    
  def access(self, frameId, isWrite):
    frame = self._get_frame(frameId)
          
    if not frame.is_referenced():
        frame.set_referenced(True)
        frame.set_access_counter(frame.get_access_counter() + self.VALUE_SUM)
