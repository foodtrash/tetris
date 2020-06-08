import pygame

class Render:
	def __init__(self,width,height,bg_color):
		self.width,self.height = width,height
		self.bg_color = bg_color
		self.screen=pygame.display.set_mode((width,height))
		self.surface = pygame.display.get_surface()
		self.colors = self.get_colors()
		pygame.display.set_caption('Tetromino')

	def fill_surface(self):
		self.surface.fill(self.bg_color)

	def display_update(self):
		pygame.display.update()

	def draw_board(self,board):
		pygame.draw.rect(self.surface,(51,51,51),board.rect)
		block_rect = pygame.Rect(0,0,board.rect_width//board.dimensions_width,
								board.rect_height//board.dimensions_height)
		for x in range(board.dimensions_width):
			for y in range(board.dimensions_height):
				if board.blocks[y][x]:
					block_rect.x = board.rect_x + block_rect.width * x
					block_rect.y = board.rect_y + block_rect.height * y
					pygame.draw.rect(self.surface,self.colors[board.blocks[y][x]],block_rect)

	def get_colors(self):
		LIGHTGREEN = (0, 255, 0 )
		GREEN = (0, 200, 0 )
		BLUE = (0, 0, 128)
		LIGHTBLUE = (0, 0, 255)
		RED = (200, 0, 0 )
		LIGHTRED = (255, 100, 100)
		PURPLE = (102, 0, 102)
		LIGHTPURPLE = (153, 0, 153)
		colors = [LIGHTGREEN, GREEN, BLUE, LIGHTBLUE, RED, LIGHTRED, PURPLE, LIGHTPURPLE]
		return colors

	def center_msg(self, msg):
		pygame.font.init()
		font = pygame.font.SysFont("comicsansms", 35)
		text = font.render(msg, True, (255, 105, 105))
		self.screen.blit(text,(400,320))
		self.display_update()

	def print_score(self, msg,score):
		pygame.font.init()
		font = pygame.font.SysFont("comicsansms", 35)
		text = font.render(msg+str(score), True, (255, 105, 105))
		self.screen.blit(text,(420,200))
		self.display_update()
	    
	def draw_tetris(self,tetris,position,block_rect):
		for block in tetris.blocks:
			block_rect.x = position[0] + block[0] * block_rect.width
			block_rect.y = position[1] + block[1] * block_rect.height
			pygame.draw.rect(self.surface,self.colors[block[2]],block_rect)
		self.display_update()

	def clear_zone(self,tetris,position,block_rect):
		for block in tetris.blocks:
		 	block_rect.x = position[0] + block[0] * block_rect.width
		 	block_rect.y = position[1] + block[1] * block_rect.height 
		 	pygame.draw.rect(self.surface,(0,0,0),block_rect)
		self.display_update()
		return False