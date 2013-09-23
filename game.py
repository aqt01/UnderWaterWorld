import pygame
from random import randrange


class Game:

	def __init__(self):
		self.game = pygame
		self.game.init()
		self.clock =  pygame.time.Clock()
	def Background(self,filename):
		self.background_path =filename
		self.screen=pygame.display.set_mode( (800,600),0,32)
		self.background = self.game.image.load(self.background_path).convert()
	def init_Sharks(self, filename, N_sharks):
		self.sharks_path = filename
		self.sharks_img = self.game.image.load(self.sharks_path).convert()
		self.alpha =128
#		self.sharks_cp.fill((255, 255, 255, self.alpha), None, pygame.BLEND_RGBA_MULT)
		self.N_sharks = N_sharks
	
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
		self.fishes_img = pygame.image.load(self.fishes_path).convert()
	
	def draw(self):
		for i in range(1,self.N_sharks) :
			self.screen.blit(self.sharks_img,(self.N_sharks_ListX.pop(), self.N_sharks_ListY.pop() ) )
		#pygame.Surface.blit( self.sharks_img (50,50))

def main() :
	juego = Game()
	juego.Background("./Images/background.jpg")
	juego.init_Sharks("./Images/sprites/tiburon/norte/mov1-norte.png",50)
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
