import pygame
from random import randrange
import threading

import time

class Fishes(threading.Thread, pygame.sprite.Sprite):

	def __init__(self,fish_lst,X,Y,vel,genre):
		super(Fishes, self).__init__()
		self._stop = threading.Event()
		pygame.sprite.Sprite.__init__(self)
		self.fish_lst = fish_lst
		self.X = X
		self.Y = Y
		self.alive = True
		self.vel = vel
		self.mov_n = 0		
		self.Or = randrange(4)
		self.movd = 0
		self.fish_img_curr = fish_lst[0][0]
		self.Sharkslist=[]
		self.Fisheslist=[]
		self.genre=genre

		#SPRITES
		#self.spri = pygame.sprite.Sprite() # create sprite
		self.image = self.fish_img_curr
		self.rect = self.fish_img_curr.get_rect() # use image extent values			
		self.rect.topleft = [self.X, self.Y] # put the ball in the top left corner
		self.type="fish"
		self.genre=self.genre

	def Mov(self):
		

		if self.movd == 6:
			self.Or = randrange(4)	
			self.movd =0
		elif self.movd < 6:
			self.movd +=1


		#self.Or = randrange(4)

		if (self.Or == 0):
			self.Y -= self.vel
			if(self.mov_n==0):
				self.fish_img_curr = self.fish_lst[0][0]
				self.mov_n =1
			elif (self.mov_n==1):
				self.fish_img_curr = self.fish_lst[0][1]
				self.mov_n=0
			elif (self.alive==0):
				self.fish_img_curr = self.fish_lst[0][2]

			elif(self.comer==1):
				self.fish_img_curr = self.fish_lst[0][3]
			elif(self.Y>self.Y_max_limit):
				self.Y=0


		elif(self.Or == 1):
			self.X += self.vel
			if(self.mov_n==0):
				self.fish_img_curr = self.fish_lst[1][0]
				self.mov_n =1
			elif (self.mov_n==1):
				self.fish_img_curr = self.fish_lst[1][1]
				self.mov_n=0
			elif (self.alive==0):
				self.fish_img_curr = self.fish_lst[1][2]

			elif(self.comer==1):
				self.fish_img_curr = self.fish_lst[1][3]
			elif(self.X>self.X_max_limit):
				self.X=0


		elif (self.Or == 2):
			self.Y += self.vel
			if(self.mov_n==0):
				self.fish_img_curr = self.fish_lst[2][0]
				self.mov_n =1
			elif (self.mov_n==1):
				self.fish_img_curr = self.fish_lst[2][1]
				self.mov_n=0
			elif (self.alive==0):
				self.fish_img_curr = self.fish_lst[2][2]

			elif(self.comer==1):
				self.fish_img_curr = self.fish_lst[2][3]

			elif(self.Y<self.Y_min_limit):
				self.Y=self.Y_max_limit+4

		elif(self.Or ==3):
			self.X -= self.vel

			if(self.mov_n==0):
				self.fish_img_curr = self.fish_lst[3][0]
				self.mov_n =1
			elif (self.mov_n==1):
				self.fish_img_curr = self.fish_lst[3][1]
				self.mov_n=0
			elif (self.alive==0):
				self.fish_img_curr = self.fish_lst[3][2]

			elif(self.comer==1):
				self.fish_img_curr = self.fish_lst[3][3]
			elif(self.X<self.X_min_limit):
				self.X=X_max_limit+4
			
			self.image = self.fish_img_curr # load ball image
			self.rect = self.fish_img_curr.get_rect() # use image extent values			
			self.rect.topleft = [self.X, self.Y] # put the ball in the top left corner

	def load_sprite(self,sprit_sharks,sprit_fishes):
		self.sprit_sharks =sprit_sharks
		self.sprit_fishes = sprit_fishes
	
	def getClases(self,sprite):

		for a in self.listClases:
			if(a.X==sprite.x and a.Y==sprite.y):
				self.Colision(a)

	def Colision(self,objeto):
		if (objeto.type=="shark"):
			self.Die()
		elif (objeto.type=="fish"):
			print "sexo uno " + `self.genre` +" sexo dos "  +`objeto.genre`
			if (self.genre != objeto.genre):
				self.Reproducir()
			else:
				if(randrange(2)==1):
					self.Comer(objeto)
				else:
					self.Die()

	def Reproducir(self):
		print "Me reproduje"
		X=self.X +5
		Y= self.Y +15
		g=randrange(1);
		fish=Fishes(self.fish_lst,X,Y,self.vel,g)
		fish.start()

	def Comer(self,objeto):
		print "Comi"
		objeto.kill()

	def Die(self):
		 print "Mori"
		 self.alive=False
		 self._stop.set()

	def get_curr_img(self):
		return self.fish_img_curr

	def juan(self):
		
			print "Chocaron"


	def run(self):
		print "SOY UN PEZ@"
		while True:

			self.Mov() 
			#print self.sprit_fishesun 
			#if pygame.sprite.spritecollide(self,self.sprit_fishes,0):
				#print "Soy un pez, choque con un pez"

			# for i in colisionF:
			# 	#print "Me tocaron"
			# 	#print i.genre
			# 	#self.Reproducir()
			# 	self.Colision(i)

				#self.alive=False
				#self.Colision(i)
				#print i.groups()
#
#			colisionS= pygame.sprite.spritecollide(self.spri,self.sprit_sharks,True)
#			for j in colisionS:
#				self.getClases(j)
			time.sleep(.7)



