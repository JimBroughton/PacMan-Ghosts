# Define the class ‘ghost’ with 4 attributes
class ghost:

  def __init__(self, name, colour, x, y, direction):
    self.name = name
    self.colour = colour
    self.x = x
    self.y = y
    self.direction = direction

  # method to print x & y coordinates
  def ghost_coords(self):
    print(self.name, ":", self.x, self.y)

  # method to update x & y coordinates depending on direction
  def update_coords(self):
    if self.direction == "left":
      self.x -= 1
    elif self.direction == "right":
      self.x += 1
    elif self.direction == "up":
      self.y += 1
    else:
      self.y -= 1


# Create 4 ‘ghost’ objects
inky = ghost("Inky", "blue", -100, 0, "left")
blinky = ghost("Blinky", "red", 100, -100, "up")
pinky = ghost("Pinky", "pink", -100, 100, "down")
clyde = ghost("Clyde", "orange", 100, 0, "right")

# print and then adjust coordinates for each ghost for 10 moves
x = 0
while x in range(0, 10):
  ghost.ghost_coords(inky)
  ghost.ghost_coords(blinky)
  ghost.ghost_coords(pinky)
  ghost.ghost_coords(clyde)
  print()
  ghost.update_coords(inky)
  ghost.update_coords(blinky)
  ghost.update_coords(pinky)
  ghost.update_coords(clyde)
  x += 1
