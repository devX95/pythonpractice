class Bird:
  
  def __init__(self):
    print("Bird is ready")
  
  def whoThis(self):
    print("Bird")

  def swim(self):
    print("Swim faster")

class Penguine(Bird):
  def __init__(self):
    super().__init__()
    print("Penguine is ready")

  def whoThis(self):
    print("penguin")
  
  def run(self):
    print("Run faster")

peggy = Penguine()
peggy.whoThis()
peggy.swim()
peggy.run()