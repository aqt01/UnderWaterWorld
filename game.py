import pygame
import Fishes, Sharks
from random import randrange
	

class Game:

	def __init__(self, Sharks, Fishes):
		self.game = pygame
		self.Sharks = Sharks
			self.Fishes = Fishes
		self.game.init()
		self.clock =  pygame.time.Clock()

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
