import random

class Tetris:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.game_over = False
		self.type = random.randint(0,6)
		self.blocks = [[(-1,0,1),(0,0,1),
					    (1,0,1),(0,1,1)],#

					    [(0,0,2),(1,0,2),
					    (0,1,2),(1,1,2)],#cube

					    [(-1,0,3),(0,0,3),
					    (1,0,3),(2,0,3)],#line

					    [(-1,0,4),(0,0,4),
					    (1,0,4),(-1,1,4)],#l

					    [(-1,0,5),(0,0,5),
					    (1,0,5),(1,1,5)],#j

					    [(-1,0,6),(0,0,6),
					    (0,1,6),(1,1,6)], #z

					    [(1,0,7),(0,0,7),
					    (0,1,7),(-1,1,7)]#mirror z
					    ][self.type]

	def rotate(self,direction):
		self.blocks=self.get_blocks(direction)

	def get_blocks(self, direction):
		if direction == 0 or self.type == 1:
			return self.blocks
		return [(b[1] * direction, -b[0] * direction,b[2])for b in self.blocks]