import pygame
from random import randrange
import threading
import time





class Sharks(threading.Thread,pygame.sprite.Sprite):
	# recibe lista de tiburiones, posicion, velocidad y genero
	def __init__(self,shark_lst,X,Y,vel,genre,X_max,Y_max,game):
#		self.Sharks_path = filename
		#threading.Thread.__init__(self)
		super(Sharks, self).__init__()
		self._stop = threading.Event()
		pygame.sprite.Sprite.__init__(self)
		self.shark_lst = shark_lst
		self.X = X
		self.Y = Y
		self.alive = True
		self.vel = vel
		self.mov_n = 0 # dos tipos de movimiento 
		self.genre=genre
		self.img_pos = 0
		self.Sharkslist=[]
		self.Fisheslist=[]
		self.type="shark"
		self.die =0
		self.TenerHijos=True
		#game.Collect_sprites()
		self.Y_max_limit = Y_max		
		self.X_max_limit = X_max
		self.Y_min_limit = 0
		self.X_min_limit = 0
		self.game=game
		self.game.Collect_sprites()


		if self.genre==0:
			self.mov_p = 0
		else:
			self.mov_p = 4
		self.shark_img_curr = self.shark_lst[self.img_pos][0]		
		
		#SPRITES
		
		self.image = self.shark_img_curr # load ball image
		self.rect = self.shark_img_curr.get_rect() # use image extent values			
		self.rect.topleft = [self.X, self.Y] # put the ball in the top left corner

		self.Or = randrange(0,4)
		self.movd =0

	def load_sprite(self,sprit_sharks,sprit_fishes):
		self.Sharks_sprites = sprit_sharks
		self.Fishes_sprites = sprit_fishes
		
	def Mov(self):

		""" OR = 0 : NORTE
		    OR = 1 : ESTE 
		    OR = 2 : SUR
		    OR = 3 : OESTE 
<<<<<<< HEAD
		"""
		self.image = self.shark_img_curr # load ball image
		self.rect = self.shark_img_curr.get_rect() # use image extent values			
		self.rect.topleft = [self.X, self.Y]


		if self.movd == 10:
			self.Or = randrange(0,4)	
			self.movd =0
		elif self.movd < 10:
			self.movd +=1


		self.img_pos = self.Or+self.img_pos

		if (self.Or == 0):
			self.Y -= self.vel
			if(self.mov_n==0):
				self.shark_img_curr = self.shark_lst[self.Or +self.mov_p][0]
				self.mov_n =1
			elif (self.mov_n==1):
				self.shark_img_curr = self.shark_lst[self.Or +self.mov_p][1]				
				self.mov_n=0
			
			elif(self.comer==1):
				self.comer=0
				
		elif(self.Or == 1):
			self.X += self.vel
			if(self.mov_n==0):
				self.shark_img_curr = self.shark_lst[self.Or +self.mov_p][0]
				self.mov_n =1
			elif (self.mov_n==1):
				self.shark_img_curr = self.shark_lst[self.Or +self.mov_p][1]				
				self.mov_n=0
			elif (self.die==1):
				self.shark_img_curr = self.shark_lst[self.Or +self.mov_p][2]

			elif(self.comer==1):
				self.comer=0
				

		elif (self.Or == 2):
			self.Y += self.vel			
			if(self.mov_n==0):
				self.shark_img_curr = self.shark_lst[self.Or +self.mov_p][0]
				self.mov_n =1
			elif (self.mov_n==1):
				self.shark_img_curr = self.shark_lst[self.Or +self.mov_p][1]				
				self.mov_n=0
			
			elif(self.comer==1):
				self.comer=0
			
		elif(self.Or ==3):
			self.X -= self.vel
			
			if(self.mov_n==0):
				self.shark_img_curr = self.shark_lst[self.Or +self.mov_p][0]
				self.mov_n =1
			elif (self.mov_n==1):
				self.shark_img_curr = self.shark_lst[self.Or +self.mov_p][1]				
				self.mov_n=0
				
			elif(self.comer==1):
				self.comer=0
		


		if(self.X>self.X_max_limit):				
				self.X=0
				self.movd=0
		elif(self.Y<self.Y_min_limit):
				self.Y=self.Y_max_limit
				self.movd=0
				
		elif(self.Y>self.Y_max_limit):
				self.Y=0
				self.movd=0				
				
		elif(self.X<self.X_min_limit):
				self.X=self.X_max_limit
				self.movd=0
				

			
		self.image = self.shark_img_curr # load ball image
		self.rect = self.shark_img_curr.get_rect() # use image extent values			
		self.rect.topleft = [self.X, self.Y] # put the ball in the top left corner
			
		
	def Draw(self):		
		self.screen.blit( self.shark_img_curr,(self.X, self.Y ))
	
	def get_curr_img(self):
		return self.shark_img_curr

	def Colision(self,objeto):
		if (objeto.type=="fish"):
			self.Comer(objeto)
		elif (objeto.type=="shark"):
			if (self.genre != objeto.genre):
				self.Reproducir()
			else:
				if(randrange(1)==1):
					self.Comer(objeto)
				else:
					self.Die()

	def Reproducir(self):
		if self.TenerHijos==True:
			print "Tiburon: Me reproduje"
			print "Me reproduje"
			X=self.X 
			Y= self.Y+15
			g=randrange(2)
			shark=Sharks(self.shark_lst,X,Y,self.vel,g,self.X_max_limit,self.Y_max_limit,self.game)
			self.game.Sharkslist.append(shark)
			self.game.Sharks_spri.add( self.game.Sharkslist[-1])
			self.game.Sharkslist[-1].start()
			self.TenerHijos=False
		
		#shark.start()

	def Comer(self,objeto):
		print "Tiburon: Comi "
		self.fish_img_curr = self.fish_lst[self.Or +self.mov_p][2]		     	
		objeto.Die()

	def Die(self):

		self.die = 1
		self.shark_img_curr = self.shark_lst[self.Or +self.mov_p][3]
		time.sleep(0.7)
		self.alive=False
		self._stop.set()

	def run(self):
		print "Tiburon: Soy Tiburon (>_>) "
		imgTemp=self.shark_img_curr
		self.shark_img_curr=pygame.image.load("./Images/huevoShark.png").convert_alpha()
		time.sleep(3)
		self.shark_img_curr=imgTemp
		
		while self.alive==True:
			
			self.Mov()

			colisionShark = pygame.sprite.spritecollide(self,self.Sharks_sprites,0)
			if colisionShark:
				if self!=colisionShark[0]:
					self.Colision(colisionShark[0])
					print "Choque entre tiburon con tiburon"

			time.sleep(0.3)

		



	def Draw_Sharks(self):
		for i in range(1,self.N_self.Sharks) :
			self.screen.blit( self.Sharks_img[0][0],(self.N_self.Sharks_ListX[i], self.N_self.Sharks_ListY[i] ), self.Shark_area)
		

	

