import pygame
from random import randrange
import threading
<<<<<<< HEAD
import time
=======

>>>>>>> e8af9c493a41215176a4fb405073446dae192741
class Fishes(threading.Thread):

	def __init__(self,fish_lst,X,Y,vel,genre):
		threading.Thread.__init__(self)

		self.fish_lst = fish_lst
		self.X = X
		self.Y = Y
		self.alive = True
		self.vel = vel
		self.mov_n = 0		
		self.Or = randrange(4)
		self.movd = 0
		self.fish_img_curr = fish_lst[0][0]


		#SPRITES
		self.spri = pygame.sprite.Sprite() # create sprite
		self.spri.image = self.fish_img_curr
		self.spri.rect = self.fish_img_curr.get_rect() # use image extent values			
		self.spri.rect.topleft = [self.X, self.Y] # put the ball in the top left corner

	def Mov(self):
		
<<<<<<< HEAD
		if self.movd == 6:
			self.Or = randrange(4)	
			self.movd =0
		elif self.movd < 6:
			self.movd +=1

=======
		self.Or = randrange(4)
>>>>>>> e8af9c493a41215176a4fb405073446dae192741
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
			
			self.spri.image = self.fish_img_curr # load ball image
			self.spri.rect = self.fish_img_curr.get_rect() # use image extent values			
			self.spri.rect.topleft = [self.X, self.Y] # put the ball in the top left corner

	def load_sprite(self,sprit_sharks,sprit_fishes):
		self.sprit_sharks =sprit_sharks
		self.sprit_fishes = sprit_fishes
	
	def getClases(self,sprite):

		for a in self.listClases:
			if(a.X==sprite.x and a.Y==sprite.y):
				self.Colision(a)

	def get_curr_img(self):
		return self.fish_img_curr
<<<<<<< HEAD

=======
>>>>>>> e8af9c493a41215176a4fb405073446dae192741

	def run(self):
		print "SOY UN PEZ@"
		while True:
<<<<<<< HEAD
			self.Mov() 
#			colisionF = pygame.sprite.spritecollide(self.spri,self.sprit_fishes,True)
#			for i in colisionF:
#				self.getClases(i)
#
#			colisionS= pygame.sprite.spritecollide(self.spri,self.sprit_sharks,True)
#			for j in colisionS:
#				self.getClases(j)
			time.sleep(.7)
=======
			self.Mov()

>>>>>>> e8af9c493a41215176a4fb405073446dae192741
