import pygame
import Fishes, Sharks
import thread

from random import randrange


class Game:
	Sharks = []
	Fishes = []

	Width = 800
	Heigth = 600

	def __init__(self, Shark_n, Fishes_n):
		self.game = pygame
		self.game.init()
		self.background_path ="./Images/background.jpg"
		self.screen=pygame.display.set_mode( (800,600),0,32)
		self.background = self.game.image.load(self.background_path).convert()
		self.vel = 3
		self.Sharks_img()
		self.Fishes_img()
		self.Create_units(Shark_n,Fishes_n,self.vel)

# se carga el lote de imagenes


	def Create_units(self,Shark_n,Fishes_n,vel):
		self.pos = []
		self.vel = vel
		self.Shark_n = Shark_n
		self.Fishes_n = Fishes_n
		self.Sharks = []
		self.Fishes = []
# se crean los threads q representaran a los tiburones y peces


		for i in range (Shark_n):
			x = Sharks.Sharks( self.Retrieve_shark_lst(), randrange(self.Width), randrange(self.Heigth),self.vel, randrange(2) )
			x.start()
			self.Sharks.append ( x )

		for i in range (Fishes_n):
			y = Fishes.Fishes(self.Retrieve_fish_lst(), randrange(self.Width),randrange(self.Heigth), self.vel, randrange(2))
			y.start()
			self.Fishes.append(y)

# se inicia pygame
		self.game.init()

#self.clock = pygame.time.Clock()




	def Fishes_img(self):

		self.Fishes_path = "./Images/sprites/peces/hembra"

		self.Fish_movs_n = [self.Fishes_path + "norte/mov1-norte-f.png", self.Fishes_path + "norte/mov2-norte-f.png",self.Fishes_path + "norte/eat-norte-f.png", self.Fishes_path + "norte/hit-norte-f.png"]
		self.Fish_movs_s = [self.Fishes_path + "sur/mov1-sur-f.png", self.Fishes_path + "sur/mov2-sur-f.png",self.Fishes_path + "sur/eat-sur-f.png", self.Fishes_path + "sur/hit-sur-f.png"]
		self.Fish_movs_e = [self.Fishes_path + "este/mov1-este-f.png", self.Fishes_path + "este/mov2-este-f.png",self.Fishes_path + "este/eat-este-f.png", self.Fishes_path + "este/hit-este-f.png"]
		self.Fish_movs_w = [self.Fishes_path + "oeste/mov1-oeste-f.png", self.Fishes_path + "oeste/mov2-oeste-f.png",self.Fishes_path + "oeste/eat-oeste-f.png", self.Fishes_path + "oeste/hit-oeste-f.png"]

		self.Fish_lst = [[],[],[],[]]
# self.Fishe_lst = [ self.Fishes_movs_n for i in range(0,3) , self.Fishes_movs_e for i in range(0,3), self.Fishes_movs_s for i in range(0,3), self.Fishes_movs_w for i in range(0,3) ]
		self.Fish_lst = [ list(self.Fish_movs_n) , list(self.Fish_movs_e), list(self.Fish_movs_s), list(self.Fish_movs_w) ]

		self.Fishes_img_n = []
		self.Fishes_img_e = []
		self.Fishes_img_s = []
		self.Fishes_img_w = []
		self.Fishes_w = 20
		self.Fishes_h = 20
		self.Fishe_area = pygame.Rect((0,0),(self.Fishes_w,self.Fishes_h))


	for i in range(0,4):
		self.Fishes_img_n.append(self.game.image.load(self.Fish_lst[0][i]).convert_alpha(self.background))
		self.Fishes_img_e.append( self.game.image.load(self.Fish_lst[1][i]).convert_alpha(self.background) )
		self.Fishes_img_s.append( self.game.image.load(self.Fish_lst[2][i]).convert_alpha(self.background) )
		self.Fishes_img_w.append( self.game.image.load(self.Fish_lst[3][i]).convert_alpha(self.background) )

	self.Fishes_img = [ list(self.Fishes_img_n), list(self.Fishes_img_e),list(self.Fishes_img_s), list(self.Fishes_img_w) ]

	def Retrieve_fish_lst(self):
		return self.Fishes_img


	def Sharks_img(self):
		self.Shark_path = "./Images/sprites/tiburon/"
		self.Shark_movs_n = [self.Shark_path + "norte/mov1-norte.png", self.Shark_path + "norte/mov2-norte.png",self.Shark_path + "norte/eat-norte.png", self.Shark_path + "norte/hit-norte.png"]
		self.Shark_movs_s = [self.Shark_path + "sur/mov1-sur.png", self.Shark_path + "sur/mov2-sur.png",self.Shark_path + "sur/eat-sur.png", self.Shark_path + "sur/hit-sur.png"]
		self.Shark_movs_e = [self.Shark_path + "este/mov1-este.png", self.Shark_path + "este/mov2-este.png",self.Shark_path + "este/eat-este.png", self.Shark_path + "este/hit-este.png"]
		self.Shark_movs_w = [self.Shark_path + "oeste/mov1-oeste.png", self.Shark_path + "oeste/mov2-oeste.png",self.Shark_path + "oeste/eat-oeste.png", self.Shark_path + "oeste/hit-oeste.png"]
		self.Shark_lst = [[],[],[],[]]
		# self.Shark_lst = [ self.Sharks_movs_n for i in range(0,3) , self.Sharks_movs_e for i in range(0,3), self.Sharks_movs_s for i in range(0,3), self.Sharks_movs_w for i in range(0,3) ]
		self.Shark_lst = [ list(self.Shark_movs_n) , list(self.Shark_movs_e), list(self.Shark_movs_s), list(self.Shark_movs_w) ]

		self.Sharks_img_n = []
		self.Sharks_img_e = []
		self.Sharks_img_s = []
		self.Sharks_img_w = []
		self.Sharks_w = 30
		self.Sharks_h = 30
		self.Shark_area = pygame.Rect((0,0),(self.Sharks_w,self.Sharks_h))

	# Se cargan las imagenes con todos los movimientos del tiburon
		for i in range(0,4):
			self.Sharks_img_n.append(self.game.image.load(self.Shark_lst[0][i]).convert_alpha(self.background))
			self.Sharks_img_e.append( self.game.image.load(self.Shark_lst[1][i]).convert_alpha(self.background) )
			self.Sharks_img_s.append( self.game.image.load(self.Shark_lst[2][i]).convert_alpha(self.background) )
			self.Sharks_img_w.append( self.game.image.load(self.Shark_lst[3][i]).convert_alpha(self.background) )
			self.Sharks_img = [ list(self.Sharks_img_n), list(self.Sharks_img_e),list(self.Sharks_img_s), list(self.Sharks_img_w) ]

	def Retrieve_shark_lst(self):
		return self.Sharks_img

	def draw(self):
		self.screen.blit( self.background, (0,0) )

	for i in range(self.Shark_n):
		self.screen.blit( self.Sharks[i].get_curr_img() ,(self.Sharks[i].X, self.Sharks[i].Y ))

	for j in range(self.Fishes_n):
		self.screen.blit( self.Fishes[i].get_curr_img() ,(self.Fishes[j].X, self.Fishes[j].Y ))



def main():
	juego = Game(40,40) #Se recibe 1er parametro la cantidad de tiburones y 2do cantidad de peces

	while True:
# for event in pygame.event.get():
# if event.type == QUIT:
 # pygame.quit()
  # sys.exit()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit_game()
				juego.draw()

		pygame.display.update()

    # pygame.display.update()

if __name__ == "__main__":
	main()

