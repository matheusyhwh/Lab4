# This is the file where you must implement the NRU algorithm

# This file will be imported from the main code. The PhysicalMemory class
# will be instantiated with the algorithm received from the input. You may edit
# this file as you wish

# NOTE: there may be methods you don't need to modify, you must decide what
# you need...

class NRU:
  INDEX_REFERENCED_ELEMENT = 0
  INDEX_MODIFIED_ELEMENT = 1  
  def __init__(self):
    self.allocated_frames = {}

  def put(self, frameId):
    self.allocated_frames.update({frame.get_id(): ['0', '0']})

  def evict(self):
    removed_frame_id = self._get_min_frame_id()
    del self.allocated_frames[removed_frame_id]
    
    return removed_frame_id

  def clock(self):
    for frame in self.allocated_frames:
        self.allocated_frames[frame][self.INDEX_REFERENCED_ELEMENT] = '0'

  def access(self, frameId, isWrite):
    self.allocated_frames[frame_id][self.INDEX_REFERENCED_ELEMENT] = '1'
    if is_write:
        self.allocated_frames[frame_id][self.INDEX_MODIFIED_ELEMENT] = '1'
