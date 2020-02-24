class Cyclic:
	p=0
	Z=[]
	def __init__(self,p):
		self.p=p
		i=0
		while(i<p):
			self.Z.append(i)
			i+=1
		#print(self.Z)
	def getGenerators(self):
		p=self.p
		Z=self.Z
		X=Z
		gen=[]
		for i in Z:
			res=[]
			for j in X:
				c = (i**j)%p
				res.append(c)
			resset= set(res)
			if(len(resset)==p-1):
				#print("Generator :",i)
				#print(res)
				gen.append(i)
		print(gen)

def main():
	z= Cyclic(1381)
	z.getGenerators()
if __name__ == '__main__':
	main()
