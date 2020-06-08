class Board:
	def __init__(self,dimensions,rect):
		self.dimensions_width=dimensions[0]
		self.dimensions_height=dimensions[1]
		self.rect_width=rect[2]
		self.rect_height=rect[3]
		self.rect=rect
		self.rect_x=rect[0]
		self.rect_y=rect[1]
		self.blocks = [[0 for x in range(self.dimensions_width)]for y in range(self.dimensions_height)]

	def check_tetris_collision(self,tetris,offset,rotation):
		for block in tetris.get_blocks(rotation):
			pos = (tetris.x + block[0] + offset[0],
				   tetris.y + block[1] + offset[1])
			if (
				pos[0] < 0 or pos[0] >= self.dimensions_width or
				pos[1] < 0 or pos[1] >= self.dimensions_height
				):
				return True
			if self.blocks[pos[1]][pos[0]]:
				return True
		return False

	def place_figure(self,tetris):
		for block in tetris.blocks:
			self.blocks[tetris.y + block[1]][tetris.x + block[0]] = block[2]

	def remove_row(self):
		for row in self.blocks:
			if 0 not in row:
				self.blocks.remove(row)
				self.blocks.insert(0,[0] * self.dimensions_width)
				return True
		return False