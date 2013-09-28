import pygame
from random import randrange
import threading



class Sharks(threading.Thread):
	# recibe lista de tiburiones, posicion, velocidad y genero
	def __init__(self,shark_lst,X,Y,vel,genre):
#		self.Sharks_path = filename
		#threading.Thread.__init__(self)
		super(Sharks, self).__init__()
        	self._stop = threading.Event()
		self.shark_lst = shark_lst
		self.X = X
		self.Y = Y
		self.alive = True
		self.vel = vel
		self.mov_n = 0 # dos tipos de movimiento 
		self.genre=genre
		self.shark_img_curr = shark_lst[0][0]

	def Mov(self):

		""" OR = 0 : NORTE
		    OR = 1 : ESTE 
		    OR = 2 : SUR
		    OR = 3 : OESTE 
			"""
		self.Or = randrange(4)
		if (self.Or == 0):
			self.Y += self.vel
			if(self.mov_n==0):
				self.shark_img_curr = self.shark_lst[0][0]
				self.mov_n =1
			elif (self.mov_n==1):
				self.shark_img_curr = self.shark_lst[0][1]				
				self.mov_n=0
			elif (self.alive==0):
				self.shark_img_curr = self.shark_lst[0][3]
			elif(self.comer==1):
				self.shark_img_curr = self.shark_lst[0][2]		
			elif(self.Y>self.Y_max_limit):
				self.Y=0
			
				
		elif(self.Or == 1):
			self.X += self.vel
			if(self.mov_n==0):
				self.shark_img_curr = self.shark_lst[1][0]
				self.mov_n =1
			elif (self.mov_n==1):
				self.shark_img_curr = self.shark_lst[1][1]				
				self.mov_n=0
			elif (self.alive==0):
				self.shark_img_curr = self.shark_lst[1][3]

			elif(self.comer==1):
				self.shark_img_curr = self.shark_lst[1][2]		
			elif(self.X>self.X_max_limit):
				self.X=0
			

		elif (self.Or == 2):
			self.Y -= self.vel			
			if(self.mov_n==0):
				self.shark_img_curr = self.shark_lst[2][0]
				self.mov_n =1
			elif (self.mov_n==1):
				self.shark_img_curr = self.shark_lst[2][1]				
				self.mov_n=0
			elif (self.alive==0):
				self.shark_img_curr = self.shark_lst[2][3]

			elif(self.comer==1):
				self.shark_img_curr = self.shark_lst[2][2]		
			
			elif(self.Y<self.Y_min_limit):
				self.Y=self.Y_max_limit+4
			
		elif(self.Or ==3):
			self.X -= self.vel
			
			if(self.mov_n==0):
				self.shark_img_curr = self.shark_lst[3][0]
				self.mov_n =1
			elif (self.mov_n==1):
				self.shark_img_curr = self.shark_lst[3][1]				
				self.mov_n=0
			elif (self.alive==0):
				self.shark_img_curr = self.shark_lst[3][3]

			elif(self.comer==1):
				self.shark_img_curr = self.shark_lst[3][2]		
			elif(self.X<self.X_min_limit):
				self.X=X_max_limit+4
			
		
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
		shark=Sharks()
		shark.start()

	def Comer(self,objeto):
		objeto.Die()

	def Die(self):
		 self._stop.set()

	def run(self):
		print "hola"
		while True:
			self.Mov()

				



"""

		self.Sharks_ListX = []
		self.Sharks_ListY = []

		self.N_fishes_ListX = []
		self.N_fishes_ListY = []
		print self.N_self.Sharks
		for i in range (1,self.N_self.Sharks+1):
			self.N_self.Sharks_ListX.append( randrange(800) )
		for i in range (1,self.N_self.Sharks+1):
			self.N_self.Sharks_ListY.append(randrange(600))
		print self.N_self.Sharks_ListY[1]
"""

"""	def Draw_Sharks(self):
		for i in range(1,self.N_self.Sharks) :
			self.screen.blit( self.Sharks_img[0][0],(self.N_self.Sharks_ListX[i], self.N_self.Sharks_ListY[i] ), self.Shark_area)
		#pygame.Surface.blit( self.Sharks_img (50,50))
"""	
	

