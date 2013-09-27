class Fishes:
	def __init__(self,filename):
	self.fishes_path = filename
	self.fishes_img = pygame.image.load(self.fishes_path).convert_alpha(self.background)
	

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





	def draw(self):
		for i in range(1,self.N_sharks) :
			self.screen.blit( self.Sharks_img[0][0],(self.N_sharks_ListX[i], self.N_sharks_ListY[i] ), self.shark_area)
		#pygame.Surface.blit( self.sharks_img (50,50))

