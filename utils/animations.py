
class Animated():
  def __init__(self, frames, delay, loop=True):
    self.frames = frames
    self.delay = delay
    self.current_frame = 0
    self.timer = 0

  def update(self, dt):
    self.timer += dt
    if self.timer >= self.delay:
      self.timer = 0
      self.current_frame += 1
      if self.current_frame >= len(self.frames):
        self.current_frame = 0

  def get_current_frame(self):
    return self.frames[self.current_frame]