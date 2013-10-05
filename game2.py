import pygame
from random import randrange


class Game:

	def __init__(self):
		self.game = pygame
		self.game.init()
		self.clock = pygame.time.Clock()

	def Background(self,filename):
		self.background_path =filename
		self.screen=pygame.display.set_mode( (800,600),0,32)
		self.background = self.game.image.load(self.background_path).convert()


	def init_Sharks(self, Shark_lst,w,h):
	# self.sharks_path = filename

	# if (orientation == 1):
		self.sharks_img_n = []
		self.sharks_img_e = []
		self.sharks_img_s = []
		self.sharks_img_w = []
		self.sharks_w = w
		self.sharks_h = h
		self.shark_area = pygame.Rect((0,0),(self.sharks_w,self.sharks_h))


		for i in range(0,4):	
			self.sharks_img_n.append(self.game.image.load(Shark_lst[0][i]).convert_alpha(self.background))
			self.sharks_img_e.append( self.game.image.load(Shark_lst[1][i]).convert_alpha(self.background) )
			self.sharks_img_s.append( self.game.image.load(Shark_lst[2][i]).convert_alpha(self.background) )
			self.sharks_img_w.append( [self.game.image.load(Shark_lst[3][i]).convert_alpha(self.background) ] )

			self.Sharks_img = [ list(self.sharks_img_n), list(self.sharks_img_e),list(self.sharks_img_s), list(self.sharks_img_w) ]

			self.alpha =128
			# self.sharks_cp.fill((255, 255, 255, self.alpha), None, pygame.BLEND_RGBA_MULT)
			self.N_sharks = 50

	def randNumbers(self):
		self.N_sharks_ListX = []
		self.N_sharks_ListY = []

		self.N_fishes_ListX = []
		self.N_fishes_ListY = []
		print self.N_sharks
		for i in range (1,self.N_sharks+1):
			self.N_sharks_ListX.append( randrange(800) )
		for i in range (1,self.N_sharks+1):
			self.N_sharks_ListY.append(randrange(600))
		print self.N_sharks_ListY[1]





	def init_Fishes(self,filename):
		self.fishes_path = filename
		self.fishes_img = pygame.image.load(self.fishes_path).convert_alpha(self.background)

	def draw(self):
		for i in range(1,self.N_sharks) :
			self.screen.blit( self.Sharks_img[0][0],(self.N_sharks_ListX[i], self.N_sharks_ListY[i] ), self.shark_area)
	#pygame.Surface.blit( self.sharks_img (50,50))

def main() :
	juego = Game()
	juego.Background("./Images/background.jpg")

	Shark_path = "./Images/sprites/tiburon/"

	Shark_movs_n = [Shark_path + "norte/mov1-norte.png", Shark_path + "norte/mov2-norte.png",Shark_path + "norte/eat-norte.png", Shark_path + "norte/hit-norte.png"]
	Shark_movs_s = [Shark_path + "sur/mov1-sur.png", Shark_path + "sur/mov2-sur.png",Shark_path + "sur/eat-sur.png", Shark_path + "sur/hit-sur.png"]
	Shark_movs_e = [Shark_path + "este/mov1-este.png", Shark_path + "este/mov2-este.png",Shark_path + "este/eat-este.png", Shark_path + "este/hit-este.png"]
	Shark_movs_w = [Shark_path + "oeste/mov1-oeste.png", Shark_path + "oeste/mov2-oeste.png",Shark_path + "oeste/eat-oeste.png", Shark_path + "oeste/hit-oeste.png"]

	Shark_lst = [[],[],[],[]]
	# Shark_lst = [ Sharks_movs_n for i in range(0,3) , Sharks_movs_e for i in range(0,3), Sharks_movs_s for i in range(0,3), Sharks_movs_w for i in range(0,3) ]
	Shark_lst = [ list(Shark_movs_n) , list(Shark_movs_e), list(Shark_movs_s), list(Shark_movs_w) ]

	juego.init_Sharks( Shark_lst, 40,40)
	juego.randNumbers()

	while True:
		# for event in pygame.event.get():
		    # if event.type == QUIT:
		     # pygame.quit()
		      # sys.exit()
		 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
	                       exit_game()

		juego.screen.blit(juego.background, (0,0))
		juego.draw()
		# x,y = pygame.mouse.get_pos()
		 # x -= mouse_c.get_width()/2
		  # y -+ mouse_c.get_height()/2

		 # screen.blit(mouse_c, (x,y))

		pygame.display.update()
if __name__ == "__main__":
	main()