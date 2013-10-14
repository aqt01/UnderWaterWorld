import pygame
import Fishes, Sharks
import thread
import time
import string
from random import randrange
	

def read_conf_file():
		conf = []
		all=string.maketrans('','')
		nodigs=all.translate(all, string.digits)
	
		f = open('configure.txt','r')
		n=0
		while 1:
			line = f.readline()
			if not line:
				break
			conf.append(line.translate(all, nodigs))
		return conf
	
class Game:


	def __init__(self, Shark_n, Fishes_n,w,h): # w = 800, h = 600
		#Se inicializa pygame
		self.game = pygame
		self.game.init()
		# Se carga el path del background
		self.background_path ="./Images/background.jpg"
		self.Width = w
		self.Heigth = h		
		# Se carga el fondo con w y h que son introducidas por parametros
		self.screen=pygame.display.set_mode( (w,h),0,32)
		# Se carga la imagen de fondo
		self.background = self.game.image.load(self.background_path).convert()
		# Se asigna la velocidad que seran los px que los sprites caminaran por cada paso
		self.vel = 8
		#se cargan las imagenes de tiburones y peces
		self.Sharks_img()
		self.Fishes_img()
		self.Sharkslist = []
		self.Fisheslist = []
		self.img_pos = 0
		self.alpha = 128
		self.Sharks_spri = pygame.sprite.Group()
		self.Fishes_spri = pygame.sprite.Group()		
		self.Create_units(Shark_n,Fishes_n,self.vel)
		self.Collect_sprites()

		
	# La funcion se encarga de ir colectando las imagenes en dos listas mientras estas se van moviendo durante la ejecucion
	def Collect_sprites(self):
		# Se vacean las imagenes ya cargadas para ir cargando las demas

		#self.Sharks_spri.empty()
		#self.Fishes_spri.empty()
		otherlistshark=[]

		for i in range(len(self.Sharkslist)):	

			if self.Sharkslist[i].alive:
				otherlistshark.append(self.Sharkslist[i])
				#self.Sharks_spri.add( self.Sharkslist[i])

			if self.Sharkslist[i].alive==False:
				self.Sharks_spri.remove( self.Sharkslist[i])

		for j in otherlistshark:
			j.load_sprite(self.Sharks_spri,self.Fishes_spri)

		otherlistfish = []
		for i in range(len(self.Fisheslist)):
			if self.Fisheslist[i].alive:
				
				otherlistfish.append(self.Fisheslist[i])
				#self.Fishes_spri.add( self.Fisheslist[i])
			if self.Fisheslist[i].alive==False:
				self.Fishes_spri.remove( self.Fisheslist[i])


		for j in otherlistfish:
			j.load_sprite(self.Sharks_spri,self.Fishes_spri)
				
				
	# Funcion para leer el archivo de configuracion
	def read_conf_file(self):		
		f = open('configure','r')
		n=0
		while 1:
			line = f.readline()
			n = n +1
			print n
			if not line:
				break
			#for i in range(0,20):
			maze_map.append(line.strip(":"))

		print maze_map[0][1]

	# Funcion para crear las unidades, tanto los peces como los tiburones

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
			x = Sharks.Sharks( self.Retrieve_shark_lst(), randrange(self.Width), randrange(self.Heigth),self.vel,  g,self.Width,self.Heigth,self)
			#MODIFICADO
			self.Sharkslist.append(x)
			self.Sharks_spri.add( self.Sharkslist[-1])

		
		for i in range (Fishes_n):
			if i >= Fishes_n/2:
				g=0
			else:
				g=1

			y = Fishes.Fishes(self.Retrieve_fish_lst(), randrange(self.Width),randrange(self.Heigth), self.vel, g,self.Width,self.Heigth,self)

			#MODIFICADO
			self.Fisheslist.append(y)
			self.Fishes_spri.add( self.Fisheslist[-1])


		self.Collect_sprites()

		
		for i in range(Shark_n):
			#MODIFICADO
			self.Sharkslist[i].start()

		for i in range(Fishes_n):
			#MODIFICADO
			self.Fisheslist[i].start()

	#Imagenes de los peces
	# Se cargan las imagenes de los peces, el mismo proceso se repite con los tiburones
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

		for i in range(len(self.Sharkslist)):	
			if self.Sharkslist[i].alive == True:
				#MODIFICADO
				self.screen.blit( self.Sharkslist[i].get_curr_img() ,(self.Sharkslist[i].X, self.Sharkslist[i].Y ))


		for j in range(len(self.Fisheslist)):
			if self.Fisheslist[j].alive == True:
				self.screen.blit( self.Fisheslist[j].get_curr_img() ,(self.Fisheslist[j].X, self.Fisheslist[j].Y ))

	

def main():
	conf = read_conf_file()
	
	juego = Game(int(conf[0]),int(conf[1]),int(conf[2]),int(conf[3])) #Se recibe 1er parametro la cantidad de tiburones y 2do cantidad de peces,
				   # 3er y 4to parametro son anchura y altura
	print "Configuracion inicial:"
	print 'Tiburones : %d | Peces : %d | Anchura %d px | Altura %d px' % (int(conf[0]), int( conf[1]), int (conf[2]), int(conf[3]))
	time.sleep(4)
	
	while True: # Loop, el juego se ejecuta dentro de esta clausura

		for event in pygame.event.get():
			if event.type == pygame.QUIT: # Para salir del juego
				exit_game()
		juego.draw()# Para dibujjar los sprites del juego
		colisionDict =pygame.sprite.groupcollide(juego.Sharks_spri,juego.Fishes_spri, 0, 0) # Para capturar las colisiones entre
										# Tiburones y peces, devuelve un diccionario con colisiones
		if  colisionDict:
			colisiones=colisionDict.values()
			for i in colisiones:
				for j in i:
					j.Die()
				
			print "Pez choco con tiburon"
		pygame.display.update()

if __name__ == "__main__":
	main()

