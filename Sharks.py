import pygame
from random import randrange
	

class Sharks:
	
	def __init__(self,N):
#		self.Sharks_path = filename
		Sharks_img_init()		
#        if (orientation == 1): 		


		self.alpha =128
#		self.Sharks_cp.fill((255, 255, 255, self.alpha), None, pygame.BLEND_RGBA_MULT)
		self.N_self.Sharks = N

	def Sharks_img_init(self):
		
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

	
	def randNumbers(self):
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


	def Draw_Sharks(self):
		for i in range(1,self.N_self.Sharks) :
			self.screen.blit( self.Sharks_img[0][0],(self.N_self.Sharks_ListX[i], self.N_self.Sharks_ListY[i] ), self.Shark_area)
		#pygame.Surface.blit( self.Sharks_img (50,50))


