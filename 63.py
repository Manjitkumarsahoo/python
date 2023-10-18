
class Cricket:
	tscore=0
	def __init__(self,n,s):
		self.name=n
		self.score=s
		Cricket.tscore=Cricket.tscore+self.score
	def show(self):
		print("name=",self.name)
		print("score=",self.score)
	@classmethod
	def tshow(cls):
		print("team score=",cls.tscore);
c1=Cricket("vk",70)
c2=Cricket("rs",60)
c3=Cricket("ms",80)
c1.show()
c2.show()
c3.show()
Cricket.tshow()