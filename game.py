import pygame
import Fishes, Sharks
import thread
import time
from random import randrange
	

	
Sharkslist = []
Fisheslist = []

class Game:

	def __init__(self, Shark_n, Fishes_n,w,h):
		self.game = pygame
		self.game.init()
		self.background_path ="./Images/background.jpg"
		self.Width = w
		self.Heigth = h		
		self.screen=pygame.display.set_mode( (800,600),0,32)
		self.background = self.game.image.load(self.background_path).convert()
		
		self.vel = 8

		self.Sharks_img()
		self.Fishes_img()

		self.img_pos = 0
		self.alpha = 128
		self.Sharks_spri = pygame.sprite.Group()
		self.Fishes_spri = pygame.sprite.Group()		
		self.Create_units(Shark_n,Fishes_n,self.vel)
		self.Collect_sprites()

		
	# se carga el lote de imagenes



	

	def Collect_sprites(self):

		self.Sharks_spri.empty()
		self.Fishes_spri.empty()
		otherlistshark=[]
		for i in range(self.Shark_n):	
			if Sharkslist[i].alive:
				otherlistshark.append(Sharkslist[i])
				self.Sharks_spri.add( Sharkslist[i])

		for j in otherlistshark:
			j.load_sprite(self.Sharks_spri,self.Fishes_spri)

		otherlistfish = []
		for i in range(self.Fishes_n):
			if Fisheslist[i].alive:
				
				otherlistfish.append(Fisheslist[i])
				self.Fishes_spri.add( Fisheslist[i])

		for j in otherlistfish:
			j.load_sprite(self.Sharks_spri,self.Fishes_spri)
				#self.Fishes[i].load_sprite(self.Sharks_spri,self.Fishes_spri)
				
		




	def Create_units(self,Shark_n,Fishes_n,vel):
		self.pos = []
		self.vel = vel
		self.Shark_n = Shark_n
		self.Fishes_n = Fishes_n
		self.Sharks = []
		self.Fishes = []		
		self.Sharks_sprites = []
		self.Fishes_sprites = []

		


		for i in range (Shark_n):
			if i >= Shark_n/2:
				g=0
			else:
				g=1
			x = Sharks.Sharks( self.Retrieve_shark_lst(), randrange(self.Width), randrange(self.Heigth),self.vel,  g,self.Width,self.Heigth)
			#MODIFICADO
			Sharkslist.append(x)

		
		for i in range (Fishes_n):
			if i >= Fishes_n/2:
				g=0
			else:
				g=1

			y = Fishes.Fishes(self.Retrieve_fish_lst(), randrange(self.Width),randrange(self.Heigth), self.vel, g,self.Width,self.Heigth)

			#MODIFICADO
			Fisheslist.append(y)


		self.Collect_sprites()

		
		for i in range(Shark_n):
			#MODIFICADO
			Sharkslist[i].start()

		for i in range(Fishes_n):
			#MODIFICADO
			Fisheslist[i].start()

	#Imagenes de los peces
	def Fishes_img(self):
		
		self.Fishes_path = "./Images/sprites/peces/"
		
		#Se cargan las imagenes del pez varon
		self.Fish_movs_n_v = [self.Fishes_path + "norte/mov1-norte-v.png", self.Fishes_path + "norte/mov2-norte-v.png",self.Fishes_path + "norte/eat-norte-v.png", self.Fishes_path + "norte/hit-norte-v.png"]
		self.Fish_movs_s_v = [self.Fishes_path + "sur/mov1-sur-v.png", self.Fishes_path + "sur/mov2-sur-v.png",self.Fishes_path + "sur/eat-sur-v.png", self.Fishes_path + "sur/hit-sur-v.png"]
		self.Fish_movs_e_v = [self.Fishes_path + "este/mov1-este-v.png", self.Fishes_path + "este/mov2-este-v.png",self.Fishes_path + "este/eat-este-v.png", self.Fishes_path + "este/hit-este-v.png"]
		self.Fish_movs_w_v = [self.Fishes_path + "oeste/mov1-oeste-v.png", self.Fishes_path + "oeste/mov2-oeste-v.png",self.Fishes_path + "oeste/eat-oeste-v.png", self.Fishes_path + "oeste/hit-oeste-v.png"]
		
		#Se cargan las imagenes del pez hembra
		self.Fish_movs_n_h = [self.Fishes_path + "norte/mov1-norte-h.png", self.Fishes_path + "norte/mov2-norte-h.png",self.Fishes_path + "norte/eat-norte-h.png", self.Fishes_path + "norte/hit-norte-h.png"]
		self.Fish_movs_s_h = [self.Fishes_path + "sur/mov1-sur-h.png", self.Fishes_path + "sur/mov2-sur-h.png",self.Fishes_path + "sur/eat-sur-h.png", self.Fishes_path + "sur/hit-sur-h.png"]
		self.Fish_movs_e_h = [self.Fishes_path + "este/mov1-este-h.png", self.Fishes_path + "este/mov2-este-h.png",self.Fishes_path + "este/eat-este-h.png", self.Fishes_path + "este/hit-este-h.png"]
		self.Fish_movs_w_h = [self.Fishes_path + "oeste/mov1-oeste-h.png", self.Fishes_path + "oeste/mov2-oeste-h.png",self.Fishes_path + "oeste/eat-oeste-h.png", self.Fishes_path + "oeste/hit-oeste-h.png"]


		self.Fish_lst = [[],[],[],[],[],[],[],[]]

		# self.Fishe_lst = [ self.Fishes_movs_n for i in range(0,3) , self.Fishes_movs_e for i in range(0,3), self.Fishes_movs_s for i in range(0,3), self.Fishes_movs_w for i in range(0,3) ]
		self.Fish_lst = [ list(self.Fish_movs_n_v) , list(self.Fish_movs_e_v), list(self.Fish_movs_s_v), list(self.Fish_movs_w_v),list(self.Fish_movs_n_h) , list(self.Fish_movs_e_h), list(self.Fish_movs_s_h), list(self.Fish_movs_w_h) ]

		self.Fishes_img_n_v = []
		self.Fishes_img_e_v = []
		self.Fishes_img_s_v = []
		self.Fishes_img_w_v = []

		self.Fishes_img_n_h = []
		self.Fishes_img_e_h = []
		self.Fishes_img_s_h = []
		self.Fishes_img_w_h = []

		self.Fishes_w = 20
		self.Fishes_h = 20
		self.Fishe_area = pygame.Rect((0,0),(self.Fishes_w,self.Fishes_h))


		for i in range(0,4):
			self.Fishes_img_n_v.append(self.game.image.load(self.Fish_lst[0][i]).convert_alpha(self.background))
			self.Fishes_img_e_v.append( self.game.image.load(self.Fish_lst[1][i]).convert_alpha(self.background) )
			self.Fishes_img_s_v.append( self.game.image.load(self.Fish_lst[2][i]).convert_alpha(self.background) )
			self.Fishes_img_w_v.append( self.game.image.load(self.Fish_lst[3][i]).convert_alpha(self.background) )

		
		for i in range(0,4):
			self.Fishes_img_n_h.append(self.game.image.load(self.Fish_lst[4][i]).convert_alpha(self.background))
			self.Fishes_img_e_h.append( self.game.image.load(self.Fish_lst[5][i]).convert_alpha(self.background) )
			self.Fishes_img_s_h.append( self.game.image.load(self.Fish_lst[6][i]).convert_alpha(self.background) )
			self.Fishes_img_w_h.append( self.game.image.load(self.Fish_lst[7][i]).convert_alpha(self.background) )


		self.Fishes_img = [ list(self.Fishes_img_n_v), list(self.Fishes_img_e_v),list(self.Fishes_img_s_v), list(self.Fishes_img_w_v), list(self.Fishes_img_n_h), list(self.Fishes_img_e_h),list(self.Fishes_img_s_h), list(self.Fishes_img_w_h) ]


	def Retrieve_fish_lst(self):
		return self.Fishes_img



	def Sharks_img(self):
		self.Shark_path = "./Images/sprites/tiburon/"
		self.Shark_movs_n_v = [self.Shark_path + "norte/mov1-norte-v.png", self.Shark_path + "norte/mov2-norte-v.png",self.Shark_path + "norte/eat-norte-v.png", self.Shark_path + "norte/hit-norte-v.png"]
		self.Shark_movs_s_v = [self.Shark_path + "sur/mov1-sur-v.png", self.Shark_path + "sur/mov2-sur-v.png",self.Shark_path + "sur/eat-sur-v.png", self.Shark_path + "sur/hit-sur-v.png"]
		self.Shark_movs_e_v = [self.Shark_path + "este/mov1-este-v.png", self.Shark_path + "este/mov2-este-v.png",self.Shark_path + "este/eat-este-v.png", self.Shark_path + "este/hit-este-v.png"]
		self.Shark_movs_w_v = [self.Shark_path + "oeste/mov1-oeste-v.png", self.Shark_path + "oeste/mov2-oeste-v.png",self.Shark_path + "oeste/eat-oeste-v.png", self.Shark_path + "oeste/hit-oeste-v.png"]



		self.Shark_movs_n_h = [self.Shark_path + "norte/mov1-norte-h.png", self.Shark_path + "norte/mov2-norte-h.png",self.Shark_path + "norte/eat-norte-h.png", self.Shark_path + "norte/hit-norte-h.png"]
		self.Shark_movs_s_h = [self.Shark_path + "sur/mov1-sur-h.png", self.Shark_path + "sur/mov2-sur-h.png",self.Shark_path + "sur/eat-sur-h.png", self.Shark_path + "sur/hit-sur-h.png"]
		self.Shark_movs_e_h = [self.Shark_path + "este/mov1-este-h.png", self.Shark_path + "este/mov2-este-h.png",self.Shark_path + "este/eat-este-h.png", self.Shark_path + "este/hit-este-h.png"]
		self.Shark_movs_w_h = [self.Shark_path + "oeste/mov1-oeste-h.png", self.Shark_path + "oeste/mov2-oeste-h.png",self.Shark_path + "oeste/eat-oeste-h.png", self.Shark_path + "oeste/hit-oeste-h.png"]


		self.Shark_lst = [[],[],[],[],[],[],[],[]]
#	self.Shark_lst = [ self.Sharks_movs_n for i in range(0,3) , self.Sharks_movs_e for i in range(0,3), self.Sharks_movs_s for i in range(0,3), self.Sharks_movs_w for i in range(0,3) ]
		self.Shark_lst = [ list(self.Shark_movs_n_v) , list(self.Shark_movs_e_v), list(self.Shark_movs_s_v), list(self.Shark_movs_w_v),list(self.Shark_movs_n_h) , list(self.Shark_movs_e_h), list(self.Shark_movs_s_h), list(self.Shark_movs_w_h) ]


		self.Sharks_img_n_v = []
		self.Sharks_img_e_v = []
		self.Sharks_img_s_v = []
		self.Sharks_img_w_v = []

		self.Sharks_img_n_h = []
		self.Sharks_img_e_h = []
		self.Sharks_img_s_h = []
		self.Sharks_img_w_h = []



		self.Sharks_w = 30
		self.Sharks_h = 30
		self.Shark_area = pygame.Rect((0,0),(self.Sharks_w,self.Sharks_h))

		# Se cargan las imagenes con todos los movimientos del tiburon
		for i in range(0,4):		
			self.Sharks_img_n_v.append(self.game.image.load(self.Shark_lst[0][i]).convert_alpha(self.background))
			self.Sharks_img_e_v.append( self.game.image.load(self.Shark_lst[1][i]).convert_alpha(self.background) )
			self.Sharks_img_s_v.append( self.game.image.load(self.Shark_lst[2][i]).convert_alpha(self.background) )
			self.Sharks_img_w_v.append( self.game.image.load(self.Shark_lst[3][i]).convert_alpha(self.background)  )

		for i in range(0,4):		
			self.Sharks_img_n_h.append(self.game.image.load(self.Shark_lst[4][i]).convert_alpha(self.background))
			self.Sharks_img_e_h.append( self.game.image.load(self.Shark_lst[5][i]).convert_alpha(self.background) )
			self.Sharks_img_s_h.append( self.game.image.load(self.Shark_lst[6][i]).convert_alpha(self.background) )
			self.Sharks_img_w_h.append( self.game.image.load(self.Shark_lst[7][i]).convert_alpha(self.background)  )

		self.Sharks_img = [ list(self.Sharks_img_n_v), list(self.Sharks_img_e_v),list(self.Sharks_img_s_v), list(self.Sharks_img_w_v),list(self.Sharks_img_n_h), list(self.Sharks_img_e_h),list(self.Sharks_img_s_h), list(self.Sharks_img_w_h) ]



		
	def Retrieve_shark_lst(self):
		return self.Sharks_img

	def draw(self):
		self.screen.blit( self.background, (0,0) )

		self.Collect_sprites()

		for i in range(self.Shark_n):	
			if Sharkslist[i].alive == True:
				#MODIFICADO
				self.screen.blit( Sharkslist[i].get_curr_img() ,(Sharkslist[i].X, Sharkslist[i].Y ))


		for j in range(self.Fishes_n):
			if Fisheslist[j].alive == True:
				self.screen.blit( Fisheslist[j].get_curr_img() ,(Fisheslist[j].X, Fisheslist[j].Y ))

	

def main():
	juego = Game(10,40,800,600) #Se recibe 1er parametro la cantidad de tiburones y 2do cantidad de peces

	while True:
#    for event in pygame.event.get():
#    if event.type == QUIT:
 #       pygame.quit()
  #      sys.exit()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit_game()
		juego.draw()
		colisionDict =pygame.sprite.groupcollide(juego.Sharks_spri,juego.Fishes_spri, 0, 0)
		if  colisionDict:
			colisiones=colisionDict.values()
			for i in colisiones:
				for j in i:
					j.Die()
				#print i
			print "Pez Choco Con tiburon"
		

		# colisionDicts =pygame.sprite.groupcollide(juego.Fishes_spri,juego.Sharks_spri, 0, 0)
		# if  colisionDicts:
		# 	colisioness=colisionDicts.keys()
		# 	#print colisiones
		# 	for i in colisioness:
		# 			i.Die()
		# 		#print i
		# 	print "Alguien Choco"
			#print colisionDictoc

		



		
		pygame.display.update()

    #	pygame.display.update()

if __name__ == "__main__":
	main()

