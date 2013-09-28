import threading

class Fish(threading.Thread):
	def __init__(self,ID,posX,posY,orient):
		threading.Thread.__init__(self)
		self.id=ID
		self.posX=posX
		self.posY=posY
		self.orient=orient

	def move(self):
		if (self.orient==0):
			self.posY-=3
			if(self.posY<=0):
				self.posY=800
		if(self.orient==1):
			self.posX-=3
			if(self.posX<=0):
				self.posX=600
		if (self.orient==2):
			self.posY+=3
			if(self.posY>=800):
				self.posY=0
		if(self.orient==3):
			self.posX+=3
			if(self.posX>=600):
				self.posX=0



	def run(self):
		while True:
			self.move();
