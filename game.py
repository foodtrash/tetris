import pygame, random
from graphic.render import Render
from logic.board import Board
from logic.tetris import Tetris

class Game:
	def __init__(self):
		pygame.init()
		self.score = 0
		self.speed = 800
		self.render = Render(640,640,(0,0,0))
		self.board = Board((10,20),pygame.Rect(20,20,300,600))
		self.tetris = Tetris(self.board.dimensions_width//2,0)
		self.next_figure = Tetris(self.board.dimensions_width//2,0)
		self.time = pygame.time.set_timer(pygame.USEREVENT,self.speed)
		self.block_rect = pygame.Rect(0,0,self.board.rect_width//self.board.dimensions_width,
								self.board.rect_height//self.board.dimensions_height)

	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False
			if self.tetris.game_over:
				self.render.center_msg('Game Over!')
			if self.tetris.game_over:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_F5:
						self.start_game()
			else:
				if event.type == pygame.USEREVENT:
					self.tetris.y += 1
					if  self.board.check_tetris_collision(self.tetris,(0,1),0):
							self.board.place_figure(self.tetris)
							self.get_next_figure()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT and not self.board.check_tetris_collision(self.tetris,(-1,0),0):
						self.tetris.x -= 1
					if event.key == pygame.K_RIGHT and not self.board.check_tetris_collision(self.tetris,(1,0),0):
						self.tetris.x += 1
					if event.key == pygame.K_UP and not self.board.check_tetris_collision(self.tetris,(0,0),1):
						self.tetris.rotate(-1)
					if event.key == pygame.K_DOWN:
						if  self.board.check_tetris_collision(self.tetris,(0,1),0):
							self.board.place_figure(self.tetris)
							self.get_next_figure()
						else:
							self.tetris.y += 1
					if event.key == pygame.K_SPACE:
						while not self.board.check_tetris_collision(self.tetris,(0,1),0):
							self.tetris.y += 1
						self.get_next_figure()
		return True

	def start_game(self):
		self.init_game()
		self.game_over = False

	def init_game(self):
		self.board=Board((10,20),pygame.Rect(20,20,300,600))
		self.tetris=Tetris(self.board.dimensions_width//2,0)
		self.next_figure=Tetris(self.board.dimensions_width//2,0)
		self.render.fill_surface()
		self.render.print_score('Score: ',self.score)

	def get_next_figure(self):
		self.render.clear_zone(self.next_figure,(self.board.rect_x + self.board.rect_width + self.block_rect.width * 5, 
		 										  self.board.rect_y + self.block_rect.height * 2),
		 										   self.block_rect)
		self.board.place_figure(self.tetris)
		self.add_score()
		self.tetris = self.next_figure
		self.next_figure = Tetris(self.board.dimensions_width//2,0)
		if self.board.check_tetris_collision(self.tetris,(0,1),0):
						self.tetris.game_over=True

	def add_score(self):
		if self.board.remove_row():
			self.score += 10 
			self.render.fill_surface()
			self.render.print_score('Score: ',self.score)
		self.check_speed()

	def check_speed(self):
		if self.score % 100 == 0:
			self.speed -= 30

	def update(self):
		self.render.draw_board(self.board)
		self.render.draw_tetris(self.tetris,(self.board.rect_x + self.tetris.x * self.block_rect.width, 
											self.board.rect_y + self.tetris.y * self.block_rect.height),
											 self.block_rect)
		self.render.draw_tetris(self.next_figure,(self.board.rect_x + self.board.rect_width + self.block_rect.width * 5, 
		 										  self.board.rect_y + self.block_rect.height * 2),
		 										   self.block_rect)
		return self.handle_events()