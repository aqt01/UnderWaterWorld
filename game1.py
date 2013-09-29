import pygame
import Fishes, Sharks
import thread

from random import randrange
	

class Game:

	def __init__(self, Sharks, Fishes, width, heigth):
		self.game = pygame
		self.Sharks_img = Shark_img()
		self.Fishes_img = Fishes_img()
		self.Sharks = Sharks
		self.Fishes = Fishes
		self.game.init()
		self.clock =  pygame.time.Clock()
	
	class Fishes_img:
def __init__(self):

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
self.Fishes_w = w
self.Fishes_h = h
self.Fishe_area = pygame.Rect((0,0),(self.Fishes_w,self.Fishes_h))


for i in range(0,4):
self.Fishes_img_n.append(self.game.image.load(self.Fish_lst[0][i]).convert_alpha(self.background))
self.Fishes_img_e.append( self.game.image.load(self.Fish_lst[1][i]).convert_alpha(self.background) )
self.Fishes_img_s.append( self.game.image.load(self.Fish_lst[2][i]).convert_alpha(self.background) )
self.Fishes_img_w.append( self.game.image.load(self.Fish_lst[3][i]).convert_alpha(self.background) )

self.Fishes_img = [ list(self.Fishes_img_n), list(self.Fishes_img_e),list(self.Fishes_img_s), list(self.Fishes_img_w) ]
		

	class Shark_img:
	
		def __init__(self):
		
			self.Shark_path = "./Images/sprites/tiburon/"

			self.Shark_movs_n = [self.Shark_path + "norte/mov1-norte.png", self.Shark_path + "norte/mov2-norte.png",self.Shark_path + "norte/eat-norte.png", self.Shark_path + "norte/hit-norte.png"]
			self.Shark_movs_s = [self.Shark_path + "sur/mov1-sur.png", self.Shark_path + "sur/mov2-sur.png",self.Shark_path + "sur/eat-sur.png", self.Shark_path + "sur/hit-sur.png"]
			self.Shark_movs_e = [self.Shark_path + "este/mov1-este.png", self.Shark_path + "este/mov2-este.png",self.Shark_path + "este/eat-este.png", self.Shark_path + "este/hit-este.png"]
			self.Shark_movs_w = [self.Shark_path + "oeste/mov1-oeste.png", self.Shark_path + "oeste/mov2-oeste.png",self.Shark_path + "oeste/eat-oeste.png", self.Shark_path + "oeste/hit-oeste.png"]

			self.Shark_lst = [[],[],[],[]]
	#	self.Shark_lst = [ self.Sharks_movs_n for i in range(0,3) , self.Sharks_movs_e for i in range(0,3), self.Sharks_movs_s for i in range(0,3), self.Sharks_movs_w for i in range(0,3) ]
		self.Shark_lst = [ list(self.Shark_movs_n) , list(self.Shark_movs_e), list(self.Shark_movs_s), list(self.Shark_movs_w) ]
	
			self.Sharks_img_n = []
			self.Sharks_img_e = []
			self.Sharks_img_s = []
			self.Sharks_img_w = []
			self.Sharks_w = w
			self.Sharks_h = h
			self.Shark_area = pygame.Rect((0,0),(self.Sharks_w,self.Sharks_h))


			for i in range(0,4):		
				self.Sharks_img_n.append(self.game.image.load(self.Shark_lst[0][i]).convert_alpha(self.background))
				self.Sharks_img_e.append( self.game.image.load(self.Shark_lst[1][i]).convert_alpha(self.background) )
				self.Sharks_img_s.append( self.game.image.load(self.Shark_lst[2][i]).convert_alpha(self.background) )
				self.Sharks_img_w.append( self.game.image.load(self.Shark_lst[3][i]).convert_alpha(self.background)  )

			self.Sharks_img = [ list(self.Sharks_img_n), list(self.Sharks_img_e),list(self.Sharks_img_s), list(self.Sharks_img_w) ]


	def Background(self,filename):
		self.background_path =filename
		self.screen=pygame.display.set_mode( (800,600),0,32)
		self.background = self.game.image.load(self.background_path).convert()

	
	
def main() :
	juego = Game(50,30)
	juego.Background("./Images/background.jpg")

	juego.init_Sharks( Shark_lst, 40,40)
	juego.randNumbers()

	while True:
#    for event in pygame.event.get():
    #    if event.type == QUIT:
     #       pygame.quit()
      #      sys.exit()
 
		for event in pygame.event.get():
	      if event.type == pygame.QUIT:
                       exit_game()

	    juego.screen.blit(juego.background, (0,0))
	    juego.draw()
#    x,y = pygame.mouse.get_pos()
 #   x -= mouse_c.get_width()/2
  #  y -+ mouse_c.get_height()/2
	
 #   screen.blit(mouse_c, (x,y))

	    pygame.display.update()

if __name__ == "__main__":
	main()
