import pygame
from random import randrange
import threading
import game
import time

class Fishes(threading.Thread, pygame.sprite.Sprite):

	def __init__(self,fish_lst,X,Y,vel,genre,X_max,Y_max):

		super(Fishes, self).__init__()
		self._stop = threading.Event()
		pygame.sprite.Sprite.__init__(self)
		self.fish_lst = fish_lst
		self.X = X
		self.Y = Y
		self.alive = True
		self.vel = vel
		self.mov_n = 0		
		self.Or = randrange(0,4)
		self.movd = 0
		self.mov_p = 4
		self.Sharkslist=[]
		self.Fisheslist=[]	
		self.genre=genre
		self.die =0

		self.Y_max_limit = Y_max		
		self.X_max_limit = X_max
		
		self.Y_min_limit = 0
		self.X_min_limit = 0

		if self.genre==0:
			self.mov_p = 0
		else:
			self.mov_p = 4

		#self.topleft = [self.X, self.Y]
		#SPRITES
		#self.spri = pygame.sprite.Sprite() # create sprite
		self.img_pos = 0

		self.fish_img_curr = self.fish_lst[self.img_pos][0]	
		self.image = self.fish_img_curr
		self.rect = self.fish_img_curr.get_rect() # use image extent values			
		self.rect.topleft = [self.X, self.Y] # put the ball in the top left corner
		
		self.type="fish"
		
	def Mov(self):
		
		self.image = self.fish_img_curr # load ball image
		self.rect = self.fish_img_curr.get_rect() # use image extent values			
		self.rect.topleft = [self.X, self.Y]
		
		#print "Fish: ",self.topleft

		if self.movd == 10:
			self.Or = randrange(0,4)	
			self.movd =0
		elif self.movd < 10:
			self.movd +=1
		

		#self.Or = randrange(4)
	
		self.img_pos = self.Or + self.img_pos

		if (self.Or == 0):
			self.Y -= self.vel

			if(self.mov_n==0):
				self.fish_img_curr = self.fish_lst[self.Or +self.mov_p][0]
				self.mov_n =1
			elif (self.mov_n==1):
				self.fish_img_curr = self.fish_lst[self.Or +self.mov_p][1]
				self.mov_n=0
			elif (self.die==1):
				self.fish_img_curr = self.fish_lst[self.Or +self.mov_p][2]

			elif(self.comer==1):
				self.fish_img_curr = self.fish_lst[self.Or +self.mov_p][3]
				self.comer=0
			#elif(self.Y>self.Y_max_limit):
				##self.Y=20
				#self.Y=self.Y_max_limit-20

		elif(self.Or == 1):
			self.X += self.vel
			if(self.mov_n==0):
				self.fish_img_curr = self.fish_lst[self.Or +self.mov_p][0]
				self.mov_n =1
			elif (self.mov_n==1):
				self.fish_img_curr = self.fish_lst[self.Or +self.mov_p][1]
				self.mov_n=0
			elif (self.die==1):
				self.fish_img_curr = self.fish_lst[self.Or +self.mov_p][2]

			elif(self.comer==1):
				self.fish_img_curr = self.fish_lst[self.Or +self.mov_p][3]
				self.comer=0
			#elif(self.X>self.X_max_limit):
				##self.X=20
			#	self.X=X_max_limit-20

		elif (self.Or == 2):
			self.Y += self.vel
			if(self.mov_n==0):
				self.fish_img_curr = self.fish_lst[self.Or +self.mov_p][0]
				self.mov_n =1
			elif (self.mov_n==1):
				self.fish_img_curr = self.fish_lst[self.Or +self.mov_p][1]
				self.mov_n=0
			elif (self.die==1):
				self.fish_img_curr = self.fish_lst[self.Or +self.mov_p][2]

			elif(self.comer==1):
				self.fish_img_curr = self.fish_lst[self.Or +self.mov_p][3]
				self.comer=0
			#elif(self.Y<self.Y_min_limit):
			#	#self.Y=self.Y_max_limit-20
			#	self.Y=20

		elif(self.Or ==3):
			self.X -= self.vel

			if(self.mov_n==0):
				self.fish_img_curr = self.fish_lst[self.Or +self.mov_p][0]
				self.mov_n =1
			elif (self.mov_n==1):
				self.fish_img_curr = self.fish_lst[self.Or +self.mov_p][1]
				self.mov_n=0
			elif (self.die==1):
				self.fish_img_curr = self.fish_lst[self.Or +self.mov_p][2]

			elif(self.comer==1):
				self.fish_img_curr = self.fish_lst[self.Or +self.mov_p][3]
				self.comer=0
			#elif(self.X<self.X_min_limit):
				##self.X=X_max_limit-20
			#	self.X=20

		if(self.X>self.X_max_limit):				
				self.X=0
				self.movd=0
		elif(self.Y<self.Y_min_limit):
				self.Y=self.Y_max_limit
				self.movd=0
				#self.Y=20
		elif(self.Y>self.Y_max_limit):
				self.Y=0
				self.movd=0				
				#self.Y=self.Y_max_limit-20
		elif(self.X<self.X_min_limit):
				self.X=X_max_limit
				self.movd=0
				#self.X=20

			#self.topleft = [self.X, self.Y]
		self.image = self.fish_img_curr # load ball image
		self.rect = self.fish_img_curr.get_rect() # use image extent values						
		self.rect.topleft = [self.X, self.Y] # put the ball in the top left corner

	def load_sprite(self,sprit_sharks,sprit_fishes):
		self.sprit_sharks = sprit_sharks
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
		Y= self.Y +5
		g=randrange(1);
		fish=Fishes(self.fish_lst,X,Y,self.vel,g,self.X_max_limit,self.Y_max_limit)
		game.Fisheslist.append(fish)
		fish.start()

	def Comer(self,objeto):
		print "Comi"
		self.comer=1
	 	self.fish_img_curr = self.fish_lst[self.Or +self.mov_p][2]
         	#time.sleep(0.7)

		objeto.Die()

	def Die(self):
		
		 self.die = 1
		 self.fish_img_curr = self.fish_lst[self.Or +self.mov_p][3]
		# time.sleep(0.7)
    		 time.sleep(0.7) 	 
                  
		 print "Mori"
		 self.alive=False
		 self._stop.set()

	def get_curr_img(self):
		return self.fish_img_curr

	def juan(self):
		
			print "Chocaron"


	def run(self):
		print "SOY UN PEZ@"

		while self.alive==True:
			self.Mov() 
			#print self.sprit_fishesun 
			
			
			# lock.acquire()
			# if self.sprit_fishes.has(self):
			# 	self.sprit_fishes.remove(self)
			# lock.release()
			colideFish=pygame.sprite.spritecollide(self,self.sprit_fishes,False)
			#print self.sprit_fishes
			if colideFish:
				if self!=colideFish[0]:
					self.Colision(colideFish[0])
					print "Soy un pez, choque con un pez"

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


