

class Grid(object):
   
   def __init__(self, width, height, defaultFill):
      self._grid = [[defaultFill for x in range(width)] for y in range(height)]
      
   
   def __getitem__(self, index):
      return self._grid[index]
   

   def getHeight(self):
      return len(self._grid)
   
   def getWidth(self):
      return len(self._grid[0])
   
   def __str__(self):
      
      return "\n".join(["".join(x) for x in self._grid])
   


if __name__ == "__main__":
   g = Grid(10, 20, "*")
   
   print(g)